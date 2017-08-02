module load Anaconda3
conda create -n pycuda python=3.5 numpy
source activate pycuda
module load CUDA
module load GCC
module load Boost
pip install pycuda
