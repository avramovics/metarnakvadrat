#!/bin/bash
# Install necessary dependencies
cd ~
python3 -m venv venv
source myenv/bin/activate
cd myapp
pip install -r requirements.txt
#deactivate