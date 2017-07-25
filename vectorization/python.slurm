#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=500M
#SSBATCH --output=python_job_slurm.out

module load Anaconda2

python < vectorization.py
