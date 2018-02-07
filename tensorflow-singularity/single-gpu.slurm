#!/bin/bash
#SBATCH --account=<your_gpu_group>
#SBATCH --partition=pascal
#SBATCH --gres=gpu:1
#SBATCH --mem=10G
#SBATCH --time=12:00:00

# Set up environment
module load GCC Singularity git

# Clone tensorflow repo to run a tutorial
git clone https://github.com/tensorflow/models.git
singularity exec --nv docker://tensorflow/tensorflow:latest-gpu \
    python ./models/tutorials/image/mnist/convolutional.py