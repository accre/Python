#!/bin/bash

#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10G
#SBATCH --time=0-03:00:00

# Sources the appropriate packages and conda environments
source job-env.sh

# Start the controller and engines 
srun -l --multi-prog cluster.conf &


# Runs the application
${APP}
