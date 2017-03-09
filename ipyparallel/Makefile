SHELL := /bin/bash

# Creates the new conda environment
env: 
	conda env create -f environment.yml ;

# Installs any pip only packages
install:
	pip install ipyparallel

# Tests that the install proceeded correctly
test:
	python -c "import ipyparallel";

# Removes the created environment
clean:
	conda remove -n $(MY_CONDA_ENV) --all;
