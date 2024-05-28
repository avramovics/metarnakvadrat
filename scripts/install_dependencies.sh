#!/bin/bash
# Install necessary dependencies
python3 -m venv venv
source myenv/bin/activate
sudo apt-get update
sudo apt-get install -y python3-pip
cd myapp
sudo pip install -r requirements.txt