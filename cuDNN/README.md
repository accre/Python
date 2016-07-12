# How to run GPU jobs using dedicated box & using SLURM
First, make your .bashrc and .theanorc look like the example ones included in this folder. The lines for anaconda are unnecessary if you are using virtualenv.

For the dedicated box (ex. vmp843) first connect via ssh:

	ssh vmp843

Create a virtual environment. virtualenv and Anaconda both work, but we use virtualenv here.

	virtualenv venv

Activate it:

	source venv/bin/activate

Install theano & its dependencies.

	pip install theano

Now you should be able to run the test script:

	python check.py


For SLURM jobs, there's no need to connect to a dedicated box. Just make the virtual environment, activate it and install theano like above.

Next, make a SLURM file similar to the one attatched (slurm_example.slurm). Now run:

	sbatch slurm_example.slurm

You should see a similar output to the log attached (slurm_example.log).
