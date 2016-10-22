#!/bin/bash

# This file either loads or creates an appropriate conda environment 


# Checks for more than one argument and throws an error
if [ $# -gt 1 ]; then
    (>&2 echo "Error: did not expect more than one argument.")
    (>&2 echo "    (Got $@)")
    return 1
fi

# Sets a default value for the environment name if not present
if [ -z "$1" ]; then
    MY_NAME="ipyparallel_env"
else
    MY_NAME="$1"
fi

# Loads necessary ACCRE packages
source pkgs.sh

# Checks if environment name is valid and, if so, exports name
if [[ "$MY_NAME" =~ ^[0-9A-Za-z_]+$ ]]; then
    export MY_CONDA_ENV=$MY_NAME ;
else
    echo "Invalid name $MY_NAME$";
    return 1
fi

# If the conda environment exists, then activates the environment
# else creates the new conda environment with the Makefile
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

