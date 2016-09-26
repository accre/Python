#!/bin/bash
#SBATCH --account=accre_gpu
#SBATCH --partition=maxwell
#SBATCH --gres=gpu:2
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=1G
#SBATCH --time=0:10:00

source theano_env.sh theano_env

python simple.py
#python logistic_regression.py
#python logistic_regression_multi_gpu.py
