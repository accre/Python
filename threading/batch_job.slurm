#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=0-00:04:00
#SBATCH --mem=999M

# Sources the appropriate packages and conda environments
source source_file.sh 

echo $SLURM_JOB_NODELIST

# Runs the program 
./compute_pi.py 
date
