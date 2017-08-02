#!/bin/bash
#SBATCH --mail-user=<your_email>@vanderbilt.edu
#SBATCH --account=<your_gpu_account>
#SBATCH --partition=maxwell
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=10G
#SBATCH --time=2:00:00
#SBATCH --output=slurm_example.log

module load Anaconda3 # this includes theano
module load CUDA
module load cuDNN
source venv/bin/activate
python check.py
