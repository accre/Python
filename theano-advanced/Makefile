SHELL := /bin/bash

env: 
	conda create -y -n $(MY_CONDA_ENV) python=3.5; 

install:
	conda install nomkl scipy numpy;
	pip install --upgrade https://github.com/Theano/Theano/archive/master.zip;

test:
	python -c "from theano.sandbox.cuda.dnn import dnn_available as d; print(d() or d.msg)"; 

clean:
	conda remove -n $(MY_CONDA_ENV) --all;
