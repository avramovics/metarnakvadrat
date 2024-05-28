#!/bin/bash
# Restart the application server
pkill uvicorn
cd ~/myapp
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &