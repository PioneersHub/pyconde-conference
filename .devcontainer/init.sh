#!/bin/bash

set -e  # Terminates the script in case of errors
set -u  # Terminates the script if an unset variable is used
set -o pipefail  # Terminates the script if a command in a pipe fails

# Install Python Version
conda install -y python=3.12

# Install pixi as package manager and workflow tool
curl -fsSL https://pixi.sh/install.sh | bash

# Replace the current shell process with (a new instance of) bash (to make pixi known)
exec bash

# Install dependencies
pixi install