#!/bin/bash
# Install necessary dependencies
cd ..
sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install -r /home/ubuntu/myapp/requirements.txt
cd myapp