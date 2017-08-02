#!/bin/bash
#SBATCH --account=accre_gpu
#SBATCH --partition=maxwell
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=1G
#SBATCH --output=python_job_slurm.out

module load Anaconda3
source activate pycuda
module load CUDA
module load GCC
module load Boost

python < pycuda_eg.py
