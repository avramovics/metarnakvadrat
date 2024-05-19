#!/bin/bash
# Install necessary dependencies
sudo apt-get update
sudo apt-get install -y python3-pip
pip3 install -r /home/ubuntu/myapp/requirements.txt