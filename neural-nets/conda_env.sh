#!/bin/bash
# Set the conda package
module load Anaconda3

# Create the conda virtual environment (if not already present)
conda create -n neural_nets python=3.4 numpy

# Activate conda environment
source activate neural_nets
