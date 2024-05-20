#!/bin/bash
# Validate that the service is running
curl -f http://0.0.0.0:8000/ || exit 1