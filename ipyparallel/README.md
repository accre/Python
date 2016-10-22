# threading 
Demonstrates basic functionality of  
[ipyparallel](https://ipyparallel.readthedocs.io/en/latest/) 
module in Python3.x to perform parallel operations on multiple threads,
possibly on multiple nodes

Includes a test script to ensure that ipyparallel is working and a 
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
$ salloc --partition=debug --nodes=2
```
