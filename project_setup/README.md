# project-setup 
Demonstrates a suggested directory setup for running Python projects using 
SLURM.

## File descriptions 
* `pkgs.sh`: lists the shell commands for loading ACCRE packages
* `Makefile`: provides rules for building the conda environment, installing 
additional packages, testing the install, and cleaning up the environment
* `source_file.sh`: sources pkgs.sh and either creates or activates 
the conda environment

## Usage
`$ source source_file.sh [my_env_name]`
* First time, creates *my_env_name* or default
* Subsequent times, activates the conda environment
