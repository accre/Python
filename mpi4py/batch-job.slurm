#!/bin/bash

#SBATCH --ntasks=8   # total MPI processes
#SBATCH --cpus-per-task=1     
#SBATCH --mem-per-cpu=100M  
#SBATCH --time=0-00:10:00

source source_file.sh 

# srun is SLURM's version of mpirun/mpiexec
srun --mpi=pmi2 python echo.py 
date
