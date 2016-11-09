#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=0-00:02:00
#SBATCH --mem=25M

# Sources the appropriate packages and conda environments
source source_file.sh

# Runs the application
python foo.py
