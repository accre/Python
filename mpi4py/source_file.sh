#!/bin/bash

# This file loads a conda environment or creates one 


# Checks input arguments for one optional environment name 
case "$#" in
  (0)
    MY_NAME="mpi4py_env"
    ;;
  (1)
    MY_NAME="$1"
    ;;
  (*)
    (>&2 echo "Error: did not expect more than one argument.")
    (>&2 echo "    (Got $@)")
    exit 1
    ;;
esac

# Checks if environment name is valid and, if so, exports name
if [[ "$MY_NAME" =~ ^[0-9A-Za-z_]+$ ]]; then
    export MY_CONDA_ENV=$MY_NAME ;
else
    echo "Invalid name $MY_NAME$";
    exit 1
fi

# Loads necessary ACCRE packages
setpkgs -a openmpi_1.10.2
setpkgs -a anaconda3


# If the conda environment exists, then activates the environment
# else creates the new conda environment with the Makefile
if $(conda env list | grep -q $MY_CONDA_ENV); then
    echo "Found existing conda environment $MY_CONDA_ENV" 
    source activate $MY_CONDA_ENV 
else
    echo "Creating conda environment $MY_CONDA_ENV";
    make env
    source activate $MY_CONDA_ENV 
    make test
fi
