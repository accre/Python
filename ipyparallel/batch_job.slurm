#!/bin/bash

#SBATCH --ntasks=14
#SBATCH --time=0-03:00:00
#SBATCH --mem=10G

# Sources the appropriate packages and conda environments
source source_file.sh

# Sets the profile and starts communication processes 
source launcher.sh
echo Using prfile $profile

# Creates output filename including timestamp
outfile=pi_estimate$(date +%Y%m%d_%H%M%S).txt
echo Using output file $outfile

# Runs the application
python compute_pi.py --profile ${profile} -n 1e12 -o $outfile 
