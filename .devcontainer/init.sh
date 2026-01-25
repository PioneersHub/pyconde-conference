#!/bin/bash

set -e  # Terminates the script in case of errors
set -u  # Terminates the script if an unset variable is used
set -o pipefail  # Terminates the script if a command in a pipe fails

# Install Python Version
conda install -y python=3.12

# Install uv as package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync