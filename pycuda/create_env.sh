setpkgs -a anaconda3
conda create -n pycuda python=3.5 numpy
source activate pycuda
setpkgs -a cuda7.0
setpkgs -a boost
pip install pycuda
