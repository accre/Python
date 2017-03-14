# keras 
Demonstration of Keras functionality using the Theano backend 

## Installation 
For development and testing, you should request an interactive job on 
one of the GPU nodes using:
```bash
salloc --partition=maxwell --account=<mygroup_gpu> --time=0:30:00 --mem=2G --gres=gpu:1
```
*Note that keras will only execute on the maxwell partition at this time.*

Substituting your group `_gpu` account name.

If this is your first attempt at installation:
```bash
$ source source_file.sh
```

By default, keras tries to use the tensorflow backend, so copy the keras.json config file
to ~/.keras/keras.json.

The `pkgs.sh` file contains the ACCRE commmands for importing the gcc and CUDA packages, among
others. 


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

Using Theano on the ACCRE cluster requires that OpenBLAS is used rather MKL. This means that 
`numpy` and `scipy` must be installed with the `nomkl` option using conda (see `Makefile` for
details).
