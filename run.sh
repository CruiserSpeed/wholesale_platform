#!/bin/bash

for i in "$@"; do
  case $i in
    -v|--vital)
      VITAL=1
      shift
      ;;
    -t|--test|--tests)
      TESTS=1
      shift
      ;;
    -*|--*)
      echo "Unknown option $i"
      exit 1
      ;;
    *)
      ;;
  esac
done

if [[ $TESTS || $VITAL ]]; then
    echo "Running tests"
    if [[ $VITAL ]]; then
        BACKEND_ADMIN_ENTRY_COMMAND="./run_tests.sh --vital" docker-compose up
    else
        BACKEND_ADMIN_ENTRY_COMMAND="./run_tests.sh" docker-compose up
    fi;
else
    echo "Running app"
    BACKEND_ADMIN_ENTRY_COMMAND="python3 src/run.py" docker-compose up
fi
