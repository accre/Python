#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=500M
#SBATCH --output=python_job_slurm.out

# Sets the anaconda package and activates the existing virtual environment.
setpkgs -a anaconda3
source activate myenvironment

# Set any other packages here, since source activate changes PATH

# Execute the script
python vectorization.py
