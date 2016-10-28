SHELL := /bin/bash

# Creates the new conda environment
env: 
	conda create -n $(MY_CONDA_ENV) python=3.5 numpy ipyparallel;

# Installs any pip only packages
install:

# Tests that the install proceeded correctly
test:
	python -c "import numpy; import ipyparallel";

# Removes the created environment
clean:
	conda remove -n $(MY_CONDA_ENV) --all;
