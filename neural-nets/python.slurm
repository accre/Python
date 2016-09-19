#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=500M

setpkgs -a anaconda3 
source activate neural_nets

python two_layer.py
