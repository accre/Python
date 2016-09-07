## vectorization_conda
This directory is adapted from the vectorization example, 
illustrating how to use Anaconda for managing package depencies.

The SLURM script assumes the existence of a conda environment called
`myenviroment`, which can be created with the bash command:
```bash
conda create --name myenvironment python=3.4 numpy
```

The SLURM script that can be submitted
to the ACCRE cluster by typing:
``` bash
sbatch python.slurm
```
from a cluster gateway. This job will run Python 3.4 on the
vectorization_py3_4.py file.
