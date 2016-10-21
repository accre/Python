# threading 
Demonstrates basic functionality of Python 
[threading](https://docs.python.org/3.5/library/threading.html) 
module in Python3.x to perform parallel operations on a single node (following
the SMP paradigm). 

Includes a test script to ensure that multithreading is working and a 
`compute_pi.py` script illustrating estimating pi. 

## Getting started
To load/create a conda environment and its (ACCRE) package dependencies:
```bash
$ source source_file.sh [conda_enviroment_name]
```

### Batch mode
```bash
$ sbatch batch_job.slurm
```

### Debug mode
```
$ salloc --partition=debug --nodes=1
```
