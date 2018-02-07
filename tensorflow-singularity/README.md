# tensorflow with singularity

Tensorflow is Google's neural network and deep learning framework that can be imported as a Python pacakge. 

Tensorflow is capable of running on NVIDIA GPUs, or on CPUs.

This repo illustrates how to run Tensorflow within a Singularity container on the ACCRE cluster. The image 
is pulled from DockerHub.

To run, just update the ```#SBATCH --account=``` line to point to your GPU group and submit using:

```
sbatch single-gpu.slurm
```

OR 

```
sbatch multi-gpu.slurm
```

If you develop and run some more sophisticated examples on the ACCRE cluster, please share with the community by submitting a pull request:

http://www.accre.vanderbilt.edu/?page_id=2735