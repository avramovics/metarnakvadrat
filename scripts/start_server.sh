#!/bin/bash
# Start the application server using Uvicorn

# Define variables
APP_DIR=~/myapp
HOST="0.0.0.0"
PORT=8000
APP="main:app"

# Change to the application directory
cd $APP_DIR

# Check if the port is already in use
if lsof -i -P -n | grep -q ":$PORT (LISTEN)"; then
    echo "Server is already running on $HOST:$PORT"
else
    echo "Starting server on $HOST:$PORT"
    source ~/venv/bin/activate  # Activate the virtual environment
    uvicorn $APP --host $HOST --port $PORT  # Start the server
    deactivate  # Deactivate the virtual environment after starting the server
fi
