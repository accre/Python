# theano
Demonstration of Theano functionality 

## Installation 
For development and testing, you should request an interactive job on 
one of the GPU nodes using:
```bash
salloc --partition=maxwell --account=<mygroup_gpu> --time=0:30:00 --mem=50G --gres=gpu:1
```
Substituting your group `_gpu` account name.

If this is your first attempt at installation:
```bash
$ cd /path/to/this/theano/demo
$ source theano_env.sh theano_env
```

## Known issues
If you receive a long error message during installation with the last line: 
```
AttributeError: ('The following error happened while compiling the node', GpuCAReduce{add}{1}(<CudaNdarrayType(float32, vector)>), '\n', "'module' object has no attribute '__file__'")
```
then you should (carefully!) clear out your ~/.theano directory, with
```bash
$ rm -rf ~/.theano
```
Then try the install again.
