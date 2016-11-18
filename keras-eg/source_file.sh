#!/bin/bash

if [ $# -gt 1 ]; then
    (>&2 echo "Error: did not expect more than one argument.")
    (>&2 echo "    (Got $@)")
    return 1
fi

if [ -z "$1" ]; then
    MY_NAME="keras_env"
else
    MY_NAME="$1"
fi

export THEANORC="./.theanorc"

source pkgs.sh

if [[ "$MY_NAME" =~ ^[A-Za-z_]+$ ]]; then
    export MY_CONDA_ENV=$MY_NAME ;
else
    echo "Invalid name $MY_NAME$";
    return 1
fi


if $(conda env list | grep -q $MY_CONDA_ENV); then
    echo "Found existing conda environment $MY_CONDA_ENV" 
    source activate $MY_CONDA_ENV 
else
    echo "Creating conda environment $MY_CONDA_ENV";
    make env
    source activate $MY_CONDA_ENV 
    make install
    make test
fi

