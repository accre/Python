#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=500M
#SSBATCH --output=python_job_slurm.out

setpkgs -a python2.7.8

python < vectorization.py
