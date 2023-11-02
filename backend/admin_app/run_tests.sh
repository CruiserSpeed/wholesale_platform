#!/bin/bash

for i in "$@"; do
  case $i in
    -v|--vital)
      VITAL=1
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

if [[ ! $VITAL ]]; then
    flake8 src && echo -e "\033[0;32mFlake8 PASSED\033[0m" || exit 1
fi;

pytest -s