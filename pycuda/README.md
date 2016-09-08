# pycuda
Demonstrates basic gpu functions using PyCUDA.

## conda environment
This example assumes the existence of a conda virtual environment named
`cuda`. To create this environment, run the bash command `source create_env.sh`. The environment will be created in your /home directory and only
needs to be created once.

## SLURM file
Replace `<mygroup>` with your group name (appended with _gpu).

## pycuda\_eg.py
Contains functions to test the CPU v. GPU speed of 
an element-wise operation on a 1-d array 
