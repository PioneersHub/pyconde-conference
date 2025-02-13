import sys
import os
import pandas as pd
import numpy as np
from pytanis import GSheetsClient, PretalxClient
from pytanis.pretalx import subs_as_df, reviews_as_df, speakers_as_df
from pytanis.google import mark_rows, gsheet_col
from pydantic import BaseModel
from pytanis.utils import implode
from pytanis.review import Col

# pass API key as input arg to the script or take from environment variable
pretalx_api_key = None
gsheet_client_secret_json = None
gsheet_spread_id = None
gsheet_worksheet_name = None

if len(sys.argv) > 1:
    pretalx_api_key = sys.argv[1]
    gsheet_client_secret_json = sys.argv[2]
    gsheet_spread_id = sys.argv[3]
    gsheet_worksheet_name = sys.argv[4]
else:
    pretalx_api_key = os.environ.get('PROGRAM_PRETALX_API_KEY')
    gsheet_client_secret_json = os.environ.get('PROGRAM_GSHEET_CLIENT_SECRET_JSON')
    gsheet_spread_id = os.environ.get('PROGRAM_GSHEET_SPREAD_ID')
    gsheet_worksheet_name = os.environ.get('PROGRAM_GSHEET_WORKSHEET_NAME')

if (pretalx_api_key is None) | (gsheet_client_secret_json is None) | (gsheet_spread_id is None) | (gsheet_worksheet_name is None):
    # determine which variable is missing
    if pretalx_api_key is None:
        raise('Pretalx API key not provided.')
    elif gsheet_client_secret_json is None:
        raise('Google Sheets client secret not provided.')
    elif gsheet_spread_id is None:
        raise('Google Sheets spread ID not provided.')
    elif gsheet_worksheet_name is None:
        raise('Google Sheets worksheet name not provided.')
    else:
        raise('One of the necessary config variables not provided.')

# Create google config file based on provided secret
f = open('client_secret.json', 'w')
f.write(gsheet_client_secret_json)
f.close() 

# Combined configuration for pretalx and gsheets. 
# TODO: Write jsons with secret and token
cfg = {
    'event_name': 'pyconde-pydata-2025',
    'selection_spread_id': gsheet_spread_id,
    'selection_work_name': gsheet_worksheet_name,
    'Pretalx': {
        'api_token': pretalx_api_key
    },
    'Google': {
        'client_secret_json': 'client_secret.json',
        'token_json': 'token.json',
        'service_user_authentication': True
    }
}

# TODO: Change back to using Config object exposed via pytanis (as part of the pipeline generate the config.toml file in the home based on the pipeline input)
class PretalxBasicModel(BaseModel):
    api_token: str | None = None

class GoogleBasicModel(BaseModel):
    client_secret_json: str | None = None
    token_json: str | None = None
    service_user_authentication: bool | None = None

class PytanisBasicConfigModel(BaseModel):
    Pretalx: PretalxBasicModel
    Google: GoogleBasicModel

v_cfg = PytanisBasicConfigModel.model_validate(cfg)

# Read Reviews and all Submissions
pretalx_client = PretalxClient(
    config=v_cfg, blocking=True)
subs_count, subs = pretalx_client.submissions(cfg['event_name'], params={'questions': 'all', 'limit': 1000})
spkrs_count, spkrs = pretalx_client.speakers(cfg['event_name'], params={'questions': 'all', 'limit': 1000})
revs_count, revs = pretalx_client.reviews(cfg['event_name'])
subs, revs, spkrs = list(subs), list(revs), list(spkrs)
subs_df = subs_as_df(subs, with_questions=True)
revs_df = reviews_as_df(revs)
spkrs_df = speakers_as_df(spkrs, with_questions=True)

# Join speakers and Submissions
subs_df = subs_df.explode([Col.speaker_code, Col.speaker_name])
subs_df = pd.merge(subs_df, spkrs_df.drop(columns=[Col.speaker_name, Col.submission]), on=Col.speaker_code)
subs_df = implode(subs_df, [col for col in spkrs_df if col not in [Col.submission]])

# Balance reviews by their personal mean (remove evaluation bias)
user_means = revs_df.groupby([Col.pretalx_user], group_keys=False)[[Col.review_score]].mean().reset_index()
revs_df["Avg Review Score"] = pd.merge(revs_df[[Col.pretalx_user]], user_means, on=Col.pretalx_user, how='left')[Col.review_score]
revs_df["Debiased Review Score"] = revs_df[Col.review_score] - revs_df["Avg Review Score"]

# Join with submissions
avg_scores = pd.merge(subs_df, revs_df[[Col.submission, Col.review_score, "Debiased Review Score"]], on=Col.submission, how='left')
avg_scores = avg_scores.groupby([Col.submission]).agg(**{Col.review_score: (Col.review_score, lambda x: x.tolist()),
                                                         "Avg Review Score": (Col.review_score, 'mean'), 
                                                         "Debiased Review Score": ("Debiased Review Score", lambda x: [f"{n:.2}" for n in x.tolist()]), 
                                                         "Avg Debiased Review Score": ("Debiased Review Score", "mean"), 
                                                         Col.nreviews: (Col.review_score, 'count')})

subs_df = pd.merge(subs_df, avg_scores, on=Col.submission)

# Restructure the Sheet
subs_df.drop(columns=['Q: Link to talk slides',
                    #   'Q: X / Twitter handle',
                      'Q: Mastodon',
                      'Q: I have read and agree to the Code of Conduct', 
                      'Created',
                      'Q: Picture',
                      'Q: Public link to supporting material, e.g. videos, Github, etc.',
                      'Q: Abstract as a tweet (X) or toot (Mastodon)',
                      'Submission type id']
            , inplace=True)

subs_df.rename(columns={'Q: Expected audience expertise: Python': 'Python expertise',
                        'Q: Expected audience expertise: Domain': 'Domain expertise',
                        'Q: I identify as a member of an underrepresented group': 'Underrepresented',
                        'Q: Country of residence': 'Country',
                        'Q: Github': 'Github',
                        'Q: LinkedIn': 'LinkedIn',
                        'Q: Homepage': 'Homepage',
                        'Q: Company / Institute': 'Affiliation',
                        'Q: Position / Job': 'Position',
                        'Q: I will present my talk on site': 'Onsite talk',
                        'Q: Notes for reviewers only': 'Reviewer notes',
                        'Q: I hereby declare that this proposal is my own original work': 'Original work',
                        'Q: Did you use an LLM, e.g. ChatGPT, to help you with this proposal?': 'ChatGPT used',
                        'Q: How should we address you?': 'Pronouns',
                        'Q: I am open to receiving invitations from meet-up organizers to showcase my work at local meet-ups.': 'Meetup interested',
                        'Q: City of residence': 'City'},
              inplace=True)

# Split track in main and subtrack
subs_df.insert(2, 'Main track', subs_df[Col.track].map(lambda x: x.split(":")[0] if not pd.isna(x) else x))
subs_df[Col.track] = subs_df[Col.track].map(lambda x: x.split(":")[-1] if not pd.isna(x) else x)

# Have "Pending state" second but last column
col = subs_df.pop("Pending state")
subs_df = pd.concat([subs_df, col.to_frame()], axis=1)
# Have "State" second but last column
col = subs_df.pop("State")
subs_df = pd.concat([subs_df, col.to_frame()], axis=1)

# avoid multi-lines cells in GSheet
subs_df['Reviewer notes'] = subs_df['Reviewer notes'].str.replace('\n', ' ')

# subs_df.sort_values("Votes Sum > 1", inplace=True, ascending=False)
subs_df.reset_index(inplace=True, drop=True)


# Get public voting results and join
votes_df = pd.read_csv(
    f"https://pretalx.com/{cfg['event_name']}/schedule/export/public_votes.csv", 
    storage_options = {
        'Authorization': f'Token {pretalx_api_key}',
        'Content-Type': 'text/plain'
    }
)
votes_df = votes_df.rename(columns={'code': Col.submission, 'score': Col.vote_score})
votes_df = votes_df.groupby(Col.submission).aggregate({Col.vote_score: lambda x: x.tolist()}).reset_index()

# add a few informative columns
votes_df[Col.nvotes] = votes_df[Col.vote_score].str.len()
votes_df["Votes Sum > 1"] = votes_df[Col.vote_score].map(lambda votes: sum([vote for vote in votes if vote > 1]))
votes_df["Avg Vote Score"] = votes_df[Col.vote_score].map(lambda x: np.mean(x))

subs_df = pd.merge(subs_df, votes_df, on=Col.submission, how='left')

## Save it to GSheet
# make subsmission code a hyperlink
subs_df[Col.submission] = subs_df[Col.submission].map(lambda sub: f'=HYPERLINK("https://pretalx.com/orga/event/{cfg["event_name"]}/submissions/{sub}", "{sub}")')

gsheet_client = GSheetsClient(config=v_cfg, read_only=False)

gsheet_client.save_df_as_gsheet(subs_df, cfg['selection_spread_id'], cfg['selection_work_name'], resize=False)

# do some formatting
from gspread_formatting import set_frozen, set_row_height, format_cell_range, cellFormat

worksheet = gsheet_client.gsheet(cfg['selection_spread_id'], cfg['selection_work_name'])
set_frozen(worksheet, rows=1, cols=1);

set_row_height(worksheet, "1:500", 50);

for idx, col in enumerate(subs_df.columns):
    if col not in {'Title', 'Track', 'Speaker name', 'ChatGPT used', 'Reviewer notes', 'Biography', 'Position', 'LinkedIn', 'Github', 'Affiliation', 'Homepage'}:
        continue
    col_id = gsheet_col(idx)

    fmt = cellFormat(
        horizontalAlignment='LEFT',
        wrapStrategy='WRAP'
        )

    format_cell_range(worksheet, col_id, fmt)

# NOTE: The google sheets API has changed and now needs RBG instead of RGB color definitions. While I am creating a PR in the supporting webcolor package to fix the problem for pytanis, I am using the following workaround.
from webcolors import name_to_rgb

mask = (subs_df["State"] == 'rejected') | (subs_df["State"] == 'withdrawn') | (subs_df["State"] == 'canceled')
firebrick_rgb_color = name_to_rgb('firebrick')
mark_rows(worksheet, mask, [firebrick_rgb_color.red / 255, firebrick_rgb_color.green / 255, firebrick_rgb_color.blue / 255])

mask = (subs_df["State"] == 'confirmed')
green_rgb_color = name_to_rgb('green')
mark_rows(worksheet, mask, [green_rgb_color.red / 255, green_rgb_color.green / 255, green_rgb_color.blue / 255])

mask = (subs_df["State"] == 'accepted')
limegreen_rgb_color = name_to_rgb('limegreen')
mark_rows(worksheet, mask, [limegreen_rgb_color.red / 255, limegreen_rgb_color.green / 255, limegreen_rgb_color.blue / 255])

mask = (subs_df["Pending state"] == 'rejected')
lightcoral_rgb_color = name_to_rgb('lightcoral')
mark_rows(worksheet, mask, [lightcoral_rgb_color.red / 255, lightcoral_rgb_color.green / 255, lightcoral_rgb_color.blue / 255])

mask = (subs_df["Pending state"] == 'accepted')
greenyellow_rgb_color = name_to_rgb('greenyellow')
mark_rows(worksheet, mask, [greenyellow_rgb_color.red / 255, greenyellow_rgb_color.green / 255, greenyellow_rgb_color.blue / 255])


print('Updated', len(subs_df), 'submissions.')