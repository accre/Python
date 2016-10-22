#!/bin/bash

#SBATCH --ntasks=24
#SBATCH --time=0-00:10:00
#SBATCH --mem=10G

# Sources the appropriate packages and conda environments
source source_file.sh

# Sets the profile and starts communication processes 
source launcher.sh

# Runs the program 
python compute_pi.py --profile ${profile} -n 80000000

# Prints timestamp
echo
date
