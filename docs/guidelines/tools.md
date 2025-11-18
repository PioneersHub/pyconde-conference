---
title: Toolzoo
icon: fontawesome/solid/hippo
---
# Tools Guidelines
Tools and intersections used in open source community events.

1. [GitHub](https://github.com/)
    - public documentation: https://github.com/PioneersHub/conference and https://pioneershub.github.io/pyconde25-conference/
    - website
2. [Tito](https://ti.to) for ticketing
3. [pretalx](https://pretalx.com) for CfP (Call for Proposals)
    - collect & review proposals and create schedule
4. [Pytanis](https://github.com/PioneersHub/pytanis) as interface to pretalx
5. Validation Service: REST API for participant info (TODO: add link)
    - validate conference participants via ticket ID and name
    - validate if email address is a participant
6. [Discord](https://discord.com/) as conference communication platform
7. Discord Bot: https://github.com/PYCONDE/discord/tree/main
    - registration service: user authentification via ticket ID and name using the Validation Service. Adds the required discord roles to the user
    - program notifications: send notifications to the program in the discord channel
    - job board: send job offers from the sponsors automatically to the job board (currently works with csv file import and should be updated to read from google forms directly)
8. [pytube](https://github.com/PioneersHub/pytube) for YouTube video publishing
9. [Certificate of attendance](https://github.com/PioneersHub/participation_certificate) for PDF document creation
10. [Team page helper app](https://github.com/PioneersHub/team_page_helper_app) for adding team members to the website
    - creates json and makes a PR on the conference website

# External Tools and Services

1. Mailgun for transactional emails.
