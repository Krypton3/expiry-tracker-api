#!/bin/bash

# Ensure the script exits on any error
set -e

# Navigate to the application directory
cd /app

# Start the application
exec python app.py