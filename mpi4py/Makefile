SHELL := /bin/bash

# creates the new conda environment
env: 
	conda env create -f environment.yml;

# Tests that the install proceeded correctly
test:
	python -c "import mpi4py";

# Removes the created environment
clean:
	conda remove -n $(MY_CONDA_ENV) --all;
