---
title: CfP with Pretlax
icon: fontawesome/solid/person-walking-dashed-line-arrow-right
---

# CfP with Pretalx

!!! warning
    This document is a work in progress. Please check back later for updates.

---

This is our set-up for the Call for Proposals (CfP) using Pretalx with best practices
to help you get the most out of your CfP.

Our guidelines are based upon our experience made with a team of:

- 2-3 program chairs
- 10 committee members
- 30-50 reviewers

Pretalx is actively being developed and provides [documentation](https://docs.pretalx.org/user/) on it's own. While this
documentation does not describe all functionality it should be consulted if something in this document is outdated and
no longer working.

## Creating the Event

A super-admin creates the event.

The _super-admin_ is an account with our roof organization, the [Python Softwareverband e.V.](https://pysv.org)  
They can see all events and all data. They can also create new events and assign other admins to them.

!!! tip "Best Practice"
    We copy the event from the previous year and adapt to our learning and needs.

!!! tip "The team handles it directly"
    We do not want the _super admin_ to manage other CfP related tasks to avoid bottlenecks.
    The committee handles everything else directly: The super-admin added the [admins](#admins) 
    who are part of the committee. They get the rest of the team on board: committee members and reviewers.

## Inviting the Team

Due to our team size, we assign different roles to your team members:

The super-admin invites the initial [admins](#admins) to the event.

!!! tip "Group readability"
    We run a yearly event and use the year as prefix for all groups for readability,
    e.g., '2025-Admins' or '2025-Reviewers'

Go to [Organiser/Event/Teams/](https://pretalx.com/orga/organiser/pyconde/teams/)

### Admins

The **committee chairs** are the **admins**, as they know best about the team and the process.

Set-up by super-admin.

- [x] Restrict the permissions to the respective event (select the event in the drop-down list).

- [x] Can change teams and permissions
- [x] Can change organiser settings
- [x] Can change event settings

**Not** checked:

- [ ] Can create events
- [ ] Is a reviewer _(this is an implicit role anyway)_

!!! tip "Delegating Tasks to Committee Members" 
    Some menus/configurations are only available to admins (e.g., managing tracks). If this task is delegated to a member of the program committee besides the chairs, admin rights are required.


### Program Committee

These are the people who will review and decide on the submissions.
Committee members also work with invited talks like keynotes and add or edit content in the system.

Set-up by [admins](#admins).

:fontawesome-solid-magnifying-glass: Check the permissions are restricted to the respective event already.

- [x] Can change event settings
- [x] Can work with and change proposals
- [x] Is a reviewer

**Not** checked:

- [ ] Can create events
- [ ] Can change teams and permissions
- [ ] Can change organiser settings

Review settings - **not** checked:

- [ ] Always hide speaker names

!!! tip "Hiding speaker names / blind review"
    It is good practice for the program committee members to see the names of the submitters, but **not** the reviewers.  
    Remember: the proposals are just a text, other references will help determine if the submitter is qualified (and not
    just good at prompting chatbots).  
    Culture beats restrictions: Openly communicate conflicts (‘submitter is a close friend’) of interest to the team and
    refrain from reviewing these submissions.

### Reviewers

These are the people who will review the submissions. They can see the submissions, review them, and leave comments.

:fontawesome-solid-magnifying-glass: Check the permissions are restricted to the respective event already.

Set-up by [admins](#admins).


The only items checked are:

- [x] Is a reviewer

Review settings:

- [x] Always hide speaker names

### Data Protection

For data protection, it's a best practice to only add the people to the current event and remove them after the event is
over.

## Content

We provide concise instructions about the CfP with information what the event is looking for.

We make sure the information is consistent with the [Call for Proposals (CfP)](call-for-proposals.md) published e.g., on
the website.

!!! tip "CfP description"
    It's not easy to navigate conciseness and a lot of information. We consider linking outside sources.

## Editor

We always give concise instructions what should be added in each field.

We point to where the information is used or not :("will be displayed on the website" or "will never be published")

We set the field lengths in Content, tab "_Fields_".

!!! tip "Field lengths"
    We made a plan where we want to use information collected in the CfP.  
    It's easier to re-use information than to ask for or edit it later.  
    For example, it's handy to have a short description that works well for social media.

### Proposal Title

We use a limit of 100 characters for readability in other context (e.g., the schedule).  
Platforms as YouTube have a 100-character limit for titles, and it'd be hard to shorten titles later.

### Session Type

[See below](#session-types).

### Proposal Abstract

- The abstract should give a concise overview of the talk.
- Ranges from 200 to 1,500 characters are work well.
- Point to not include speaker names or affiliations.

### Proposal Description

- Ranges from 400 to 5,000 characters are work well, consider tutorials might need more space.
- Point to put detailed outline here
- Point to it will be published on the website
- Point to not include speaker names or affiliations.

### Notes

- Point to it will be published on the website and is only visible to the program committee not including the reviewers.

### Recording opt-out

Make sure to have a policy in place if you want to allow recording opt-out.

### Session Image

If your website does not create event branded images this might be useful.

### Duration

Allowing custom durations adds a lot of complexity to the schedule, better to have fixed durations handle via
the [session types](#session-types).

### Custom Questions

Custom questions help to bring more context to the proposal. They are also helpful to filter and sort the proposals.

Always include who will see the information and if it will be published.

!!! tip "Custom Questions"
    Consider which information you actually need, answering many questions can be exhausting for the submitter.  
    On the other hand, it's hard to collect required information later.  

!!! tip "Not all information is required now"
    No need to collect all information now, consider which information is not required for the review process and will be collected later anyway.    
    For example, dietary restrictions of a speaker are not required for the review process and is usually collected via the tickets.  
    


We add the following questions to the proposals (1).
{ .annotate }

1. There are also custom questions to be added for the speaker profile.

#### Expected audience expertise: Domain

> The domain expertise your audience should have to follow along.

- Novice
- Intermediate
- Advanced

Visible to: :fontawesome-solid-globe: world

#### Expected audience expertise: Python

> How experienced should the audience be in Python programming?

- Novice
- Intermediate
- Advanced

Visible to: :fontawesome-solid-globe: world

#### Prerequisites

> Things the attendees should know before visiting for the talk

We want to promote speakers spend the talk time on the content and not start on the basics.

Visible to: :fontawesome-solid-globe: world

---

####  Abstract as a tweet (X) or toot (Mastodon)

> Short description of your abstract one could tweet
 
Text to promote the session on social media. Maybe LLMs can do this for us in the future.

Visible to: :fontawesome-solid-globe: world

---

#### Notes for reviewers only

> Anything you like to share with the reviewers only - will not be published. Do not include any personal information.

Text

Visible to: :fontawesome-solid-user-secret: committee members and reviewers only

#### Public link to supporting material, e.g., videos, GitHub, etc.

Optional, material to support the proposal.

Visible to: :fontawesome-solid-globe: world

#### Link to talk slides

Optional, material to support the proposal.

Visible to: :fontawesome-solid-user-secret: committee members and reviewers only

---

#### Fresh content

- [Y/N] Was this proposal presented already and recorded?

We try to avoid repeating content that is already available.
This is not a strict policy, depending on the topic the on-site discussion might be valuable.

Visible to: :fontawesome-solid-user-secret: committee members and reviewers only

#### Honor-code original work

- [x] I hereby declare that this proposal is my own original work

> Confirmation of being original content

Quality assurance: presenting other people's blog posts or work is not considered original content.

Visible to: :fontawesome-solid-user-secret: committee members and reviewers only

#### No-Remote

- [x] I will present my talk on site

> Accepted speakers are required to present on site.

Double-confirmation to manage expectations.

Visible to: :fontawesome-solid-user-secret: committee members and reviewers only

#### Code of Conduct

- [x] I have read and agree to the Code of Conduct

> This is a must to attend the conference. Must be accepted.

Visible to: :fontawesome-solid-user-secret: committee members and reviewers only

---

### Speakers

Speakers need to answer questions only once.

Speaker questions are simple questions.

#### Private Questions

All text answers except where noted, visible to: :fontawesome-solid-user-secret: committee members and reviewers only

- How should we address you? (pronouns)
- Company / Institution
- Job title
- Country of residence
- City of residence
- Do you identify as a member of an underrepresented group?
- [x] Are you a first-time speaker?
- Community contributions (organizer, open-source, etc.)
- Age, ranges:
    - 18-25
    - 26-35
    - 36-45
    - 46-55
    - 56-65
    - 66 and older

#### Public Questions

All text answers, visible to: :fontawesome-solid-globe: world

- Name
- Biography
- Homepage
- LinkedIn 
- X
- GitHub
- BlueSky
- Threads
- Mastodon


## Session Types

We use the following descriptive session types (duration is displayed by Pretalx on default and should not be part of the name):

|             |   duration |
|-------------|-----------:|
| talk        | 30 minutes |
| talk (long) | 45 minutes |
| tutorial    | 90 minutes |

Some sessions are invited or organized not via the CfP. 

Private types are:

|                           |   duration |
|---------------------------|-----------:|
| keynote                   | 45 minutes |
| sponsored talk            | 30 minutes |
| sponsored talk (long)     | 45 minutes |
| sponsored talk (keystone) | 90 minutes |
| sponsored tutorial        | 90 minutes |
| panel                     | 60 minutes |

To prevent these session types from being selected in the CfP, the 'Require access code' option must be selected when creating the session type.

## Sponsored Talks

Sponsored talks are a great way to support the conference and get your message as a sponsor out.

The Program Committee will work actively with the sponsors to ensure the content is valuable to the attendees.

Sponsored content is moderate and accounts for about 10% of the overall program.

## Managing Invited Talks with Access Codes
Access codes allow sessions to be created outside of the regular CfP. Those provided with a code can create new
proposals even after the deadline has expired or for session types that are not available as part of the normal CfP.
The session creation process itself is identical for the end user to the normal CfP.

New access codes can be crated at the bottom of the "Call for Proposals" menu. Following procedure is considered good
practice:

- For personalized access codes (e.g., sponsors) individual access codes should be created for each individual entity 
    with a "Maximum uses" set to one.
- Changing the beginning of the access code to something descriptive (e.g., "\<Sponsorname\>RestOfTheCode") allows 
    easier tracking of who already has used their code.
- Access codes should be as restrictive as possible, at minimum the session type must be selected.

!!! tip "Finding talks created via an access code"
    If an access code has been used, opening the editing view of the access code provides a link to the talk(s) created with this code. If no talks are displayed, they have been deleted.

---