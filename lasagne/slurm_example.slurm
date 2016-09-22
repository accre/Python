#!/bin/bash
#SBATCH --account=<my_group>_gpu
#SBATCH --partition=maxwell
#SBATCH --gres=gpu:2
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=1G
#SBATCH --time=0:10:00

source bake_lasagne.sh lasagne_env

python mnist.py cnn 50
