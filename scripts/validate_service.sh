#!/bin/bash
# Validate that the service is running
curl -f http://127.0.0.1 || exit 1