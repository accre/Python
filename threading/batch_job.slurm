#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=0-00:04:00
#SBATCH --mem=999M

setpkgs -a openmpi_1.8.4
setpkgs -a anaconda3
source activate mpi4py_env
echo $SLURM_JOB_NODELIST

# Runs the program 
./compute_pi.py 
date
