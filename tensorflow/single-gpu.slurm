#!/bin/bash
#SBATCH --account=<your_gpu_group>
#SBATCH --partition=maxwell
#SBATCH --gres=gpu:1
#SBATCH --mem=10G
#SBATCH --time=12:00:00

# Set up environment
setpkgs -a tensorflow_0.11.0rc0

# Run example
python fit-line.py