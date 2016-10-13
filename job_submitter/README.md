Small python script for submitting batch jobs programmatically. For more help on options try:

    python accre_job_submitter -h

usage: accre_job_submitter [-h] --command COMMAND [COMMAND ...]
                           [--starting-dir STARTING_DIR] [--log-dir LOG_DIR]
                           [--name NAME] [--slurm-file SLURM_FILE]
                           [--memory MEMORY] [--nodes NODES] [--ntasks NTASKS]
                           [--time TIME] [--print-host-info] [--dont-submit]
                           [--group GROUP] [--print-time] [--email EMAIL]

Submit jobs to the ACCRE slurm grid

optional arguments:
  -h, --help            show this help message and exit
  --command COMMAND [COMMAND ...]
                        command to be submitted
  --starting-dir STARTING_DIR
                        Directory to start script in. Default=`pwd`
  --log-dir LOG_DIR     Directory to write log files to. Default=`pwd`/logs/
  --name NAME           Name for script. Default=current time
  --slurm-file SLURM_FILE
                        File to save SLURM file to. Default=Don't save
  --memory MEMORY       Memory required for the cluster. Default=4G
  --nodes NODES         Number of nodes default=1
  --ntasks NTASKS       Number of processes default=1
  --time TIME           Amount of walltime to request in dd-hh:mm:ss
  --print-host-info     Print out information about which machine you are on
  --dont-submit         Don't submit the job. Just write the slurm file
  --group GROUP         Which ACCRE group to use Default=None
  --print-time          print the time at job begin and end
  --email EMAIL         Email address, defualt=None
