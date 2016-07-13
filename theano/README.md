# How to run GPU jobs using using SLURM
First, make your .bashrc and .theanorc look like the example ones included in this folder. Note that the lines for anaconda are unnecessary if you are using virtualenv.

Create a virtual environment. virtualenv and Anaconda both work, but we use virtualenv here.

	virtualenv venv

Activate it:

	source venv/bin/activate

Install theano & its dependencies.

	pip install theano

If theano is already installed, you don't need to do this.

Next, make a SLURM file similar to the one attatched (slurm_example.slurm). This file specifies information about your task and the instructions for running.

The instructions in our example script include activating your virtual environment and running the check.py script, which runs a simple job on the gpu:

	source venv/bin/activate
	python check.py

Try running the included script with sbatch:

	sbatch slurm_example.slurm

You should see a similar output to the log attached (slurm_example.log).
