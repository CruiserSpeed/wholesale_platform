#!/bin/bash

if [[ "$1" == "--test" || "$1" == "-t" ]]; then
    echo "Building tests"
    BACKEND_ADMIN_ENTRY_COMMAND="pytest -s" docker-compose up
else
    echo "Building app"
    BACKEND_ADMIN_ENTRY_COMMAND="python3 src/run.py" docker-compose up
fi
