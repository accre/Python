#!/bin/bash

#SBATCH --nodes=1
#SBATCH --constraint=skylake
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=500M
#SBATCH --output=python_job_slurm.out

module load Intel IntelMPI Python numpy

python vectorization.py
