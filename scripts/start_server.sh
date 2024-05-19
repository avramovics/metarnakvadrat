#!/bin/bash
# Start the application server using Uvicorn
#cd /home/ubuntu/myapp
uvicorn main:app --host 0.0.0.0 --port 8000