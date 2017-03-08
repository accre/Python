#!/bin/bash
# cluster-roles.sh


if [[ "$#" -ne 1 ]]; then
  echo "USAGE: BASH $0 ROLENAME" 
  exit 1
else
  ROLENAME="$1"
fi

case $ROLENAME in 
  ("controller")
    echo "Launching controller"
    ipcontroller --ip="*" --profile=${PROFILE} & 
    sleep 10
    ;;
  ("engine")
    echo "Launching engine on $(hostname)"
    ipengine --profile=${PROFILE} --location=$(hostname) &
    sleep 25
    ;;
  (*)
    (>2& echo "Unknown ROLENAME [$ROLENAME]")
    exit 1
esac
