#!/bin/bash

#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=500M
#SBATCH --output=python_job_slurm.out

# Loads the Anaconda3 module, whose default python has numpy installed
module load Anaconda3

# Source the already existing conda environment
source activate myenvironment

# Execute the script
python vectorization.py
