SHELL := /bin/bash

env: 
	conda create -y -n $(MY_CONDA_ENV) python=3.5 scipy numpy; 

install:
	pip install --upgrade https://github.com/Theano/Theano/archive/master.zip;\
	pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip

test:
	python -c "from theano.sandbox.cuda.dnn import dnn_available as d; print(d() or d.msg)"; \
	python -c "import lasagne";

clean:
	conda remove -n $(MY_CONDA_ENV) --all;
