#!/bin/bash
# Start the application server using Uvicorn
cd ~/myapp

HOST="0.0.0.0"
PORT=8000
APP="main:app"

if lsof -i -P -n | grep -q ":$PORT (LISTEN)"; then
    echo "Server is already running on $HOST:$PORT"
else
    echo "Starting server on $HOST:$PORT"
    nohup uvicorn $APP --host $HOST --port $PORT &
fi