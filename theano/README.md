# How to run GPU jobs using using SLURM
First, make your .theanorc look like the example ones included in this folder.

	cp example_theanorc.txt ~/.theanorc

Now, you have two choices: 1) use the installed python packages, or 2) use a virtual environment (virtualenv or anaconda). Using a virtual environment is, in my opinion, easier if you have packages that you need to install. If you're using a virtualenv, first create one:

	virtualenv venv

Activate it:

	source venv/bin/activate

Install theano & its dependencies.

	pip install theano

If you're using the already installed packages, you don't need to do this.

Next, make a SLURM file similar to the one attatched (slurm_example.slurm). This file specifies information about your task and the instructions for running.

The instructions in our example script include specifying packages, activating your virtual environment and running the check.py script, which runs a simple job on the gpu:

	module load Anaconda3 # this includes theano
	module load CUDA
	module load cuDNN

	source venv/bin/activate # not needed if you are using installed packages only

	python check.py

Try running the included script with sbatch:

	sbatch slurm_example.slurm

You should see a similar output to the log attached (slurm_example.log).
