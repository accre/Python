#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=0-00:04:00
#SBATCH --mem=16G

# Sets the anaconda3 package
module load Anaconda3

# Runs the program 
python compute_pi.py -n 10000000

# Prints the date to the output file
date
