[![Deploy Docs](https://github.com/PioneersHub/conference/actions/workflows/ci.yml/badge.svg)](https://github.com/PioneersHub/conference/actions/workflows/ci.yml)

# PyCon DE & PyData Conference Playbook & Guidelines & Helpful Scripts

This playbook is our public reference for how we run our volunteer-driven conference.
By sharing our experience we hope to help others to run their own conference.

We aim to update and refine this playbook continuously.
We always are motivated to share our knowledge and experience with others.

We are considerate in publishing guidelines and policies that could be misused and share them within the team (and
future teams) of our volunteer organisation in out protected workspace.
We act responsibly by not sharing confidential or private information,

## How To Use

Fork this repository and adapt the content to your needs.

👉 See the [full documentation](https://pioneershub.github.io/conference/)

## Attribution

This document draws on years of experience from organizing of running and co-organizing events since like
[PyCon DE](https://de.pycon.org/), [EuroPython](https://europython.eu), [EuroSciPy](https://euroscipy.org)
and [PyData Berlin](https://berlin.pydata.org).

These awesome people have contributed to content this documentation was built upon:

[Aeneas Christodoulou](https://github.com/AeneasChristodoulou): Video;
[Alexander CS Hendorf](https://github.com/alanderex): Program, Steering, Office;
[Alina Lenhardt](https://github.com/alina-lenhardt): Program, Communication;
[Anastasia](https://github.com/asamokhina): Communication;
[Anja Pilz](https://github.com/aplz): Program;
[Christopher Schultz](#): Program;
[Daniel Ringler](https://github.com/dringler): Infrastructure, Steering;
[Florian Wilhelm](https://github.com/florianwilhelm): Program;
[Julio Batista Silva](https://github.com/jbsilva): Diversity;
[Jurik Sommer](https://github.com/Jurik-001): Program;
[Kristian Rother](https://github.com/krother): On-Site;
[Lisa Andreevna Chalaguine](#): Program;
[Marisa Mohr](https://github.com/marisamohr): Program;
[Maryam Pourranjbar Mohr](#): Program;
[Matthias Hofmann](#): Program;
[Mihail Douhaniaris](https://github.com/mtdo): Video;
[Mojdeh Rastgoo](https://github.com/mrastgoo): Diversity;
[Naa Ashiorkor Nortey](https://github.com/7ashiorkor7): Diversity;
[Nils Mohr](https://github.com/FinkeNils): Program;
[Nydia Medina](https://github.com/nydiamedina): Diversity;
[Olakunle Olaniyi](https://github.com/rugging24): Communication;
[Paula González Avalos](https://github.com/pga99): Diversity;
[Ricardo Kawase](#): Program;
[Sabine Reisser](https://github.com/orgs/PYCONDE/people/sreisser): Video;
[Sebastian Neubauer Reisser](https://github.com/sebastianneubauer): Video, Steering;
[Shivam Singhal](https://github.com/championshuttler): On-Site;
[Theodore Meynard](https://github.com/orgs/PYCONDE/people/terezaif): Diversity, Swag;
[Valentina Scipione](https://github.com/astrovale): On-Site;

We missed mentioning you?   
We value all contributions to this project, including those made in the past. If you have contributed to
community-driven conferences or this playbook in the past and would like to be acknowledged:

1. Open a pull request titled "Add [Your Name] to Contributors".
2. In the pull request description, briefly describe your contribution. For example:
    - "I helped organize 2022 in program"
    - "I contributed the section on volunteer management of this playbook"

We'll review your pull request and merge it if appropriate.

## Documentation

The documentation is written in Markdown and rendered with MKDocs.

MKDocs is used to generate the documentation.  
[Read the documentation](https://pioneershub.github.io/conference/)

Extra features are added with the Material for MkDocs theme.  
[MKDocs Material](https://squidfunk.github.io/mkdocs-material/)

## Installation (Running the Python Scripts)

The easiest way to execute any python script that is provided within this repository, is by starting up the project within a devcontainer. After having cloned this repository:

1. Make sure to have a local installation of Docker and VS Code running.
2. Open VS Code and make sure to have the Dev Containers Extension from Microsoft installed.
3. Open the cloned project in VS Code and from the bottom right corner confirm to open the project to be opened within the Devcontainer.

If you miss any dependencies check out the devcontainer.json within the .devcontainer folder. Otherwise, all setup for the pixi environment (including the installation of the dependencies) is all done.

1. To execute scripts, activate the default environment with `pixi shell` and execute any python script with `python <script.py>` (this makes sure that all dependencies as specified in `pixi.toml` are known.)

## Community Playbooks by Pioneers Hub

This playbook was created by [Pioneers Hub](https://www.pioneershub.org/en/) based on the content of many awesome
people.
Pioneers Hub is an organization dedicated to building and nurturing communities of experts in tech and research.
The goal is to facilitate knowledge sharing, collaboration, and innovation.

Check out the [Pioneers Hub GitHub repository](https://github.com/PioneersHub) to check more templates and tools
like this to build and maintain healthy communities.

![Pioneers Hub Logo](docs/assets/images/Pioneers-Hub-Logo-vereinfacht-inline.svg)
