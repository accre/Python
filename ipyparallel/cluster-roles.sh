#!/bin/bash
# launcher.sh

if [[ "$#" -ne 1 ]]; then
  echo "USAGE: bash $0 ROLE" 
  exit 1
else
  ROLE=$1
fi

case $ROLE in 
  ("controller")
    echo "Launching controller"
    ipcontroller --ip="*" --profile=${PROFILE}
    ;;
  ("engine")
    sleep 5
    echo "Launching engines on $(hostname)"
    ipengine --profile=${PROFILE}
    ;;
esac
