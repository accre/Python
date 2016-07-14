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

setpkgs -a python3.4.2
setpkgs -a cudnn7.0-v3
setpkgs -a cuda7.0
source venv/bin/activate
python check.py
