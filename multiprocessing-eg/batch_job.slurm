#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=0-00:04:00
#SBATCH --mem=500M

# Sets the anaconda3 package
setpkgs -a anaconda3

# Runs the program 
python compute_pi.py -n 1000000000 

# Prints the date to the output file
date
