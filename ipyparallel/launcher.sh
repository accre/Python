#!/bin/bash

profile=job_${SLURM_JOB_ID}_$(hostname)

echo "Creating profile ${profile}"
ipython profile create ${profile}

echo "Launching controller"
ipcontroller --ip="*" --profile=${profile} & 
sleep 10

echo "Launching engines"
srun ipengine --profile=${profile} --location=$(hostname) &
sleep 25 
