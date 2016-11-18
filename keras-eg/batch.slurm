#!/bin/bash
#SBATCH --account=accre_gpu
#SBATCH --partition=maxwell
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=2G
#SBATCH --time=0:10:00

source source_file.sh 

python mnist_mlp.py
