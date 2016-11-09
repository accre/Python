SHELL := /bin/bash

# Creates the new conda environment
env: 
	conda create -n $(MY_CONDA_ENV) python=3.5 ;

# Installs any pip only packages
install:
	pip install PrettyTable  

# Tests that the install proceeded correctly
test:
	python -c "from prettytable import PrettyTable";

# Removes the created environment
clean:
	conda remove -n $(MY_CONDA_ENV) --all;
