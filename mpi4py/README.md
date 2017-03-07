# mpi4py
Demonstrates basic functionality of mpi4py, a Python wrapper for MPI. 

## Getting started
To load/create a conda environment and its (ACCRE) package dependencies:
```bash
$ source source_file.sh [conda_enviroment_name]
```

### Batch mode
```bash
$ sbatch mpi_job.slurm
```

### Debug mode
```
$ salloc --partition=debug --nodes=2
```


## Notes
Dynamic process allocation fails.
