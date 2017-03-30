#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --mem=2G
#SBATCH --time=0-04:00:00      # 4 hours
#SBATCH --output=notebook.out

# Once this job launches, check the node it landed on with:
#      squeue --user=userid
# Then open tunnel from local machine with something like:
#      ssh -L 9999:vmp506:7777 frenchwr@login.accre.vanderbilt.edu
# This binds port 9999 on localhost to port 7777 on vmp506
# Finally, point your local browser to localhost:9999

PORT=7777
echo To open a tunnel from local machine, 
echo Execute in a new terminal window:
echo "ssh -L 9999:$HOSTNAME:$PORT $(whoami)@login.accre.vanderbilt.edu"
printf '=%.0s' {1..80}
echo

setpkgs -a anaconda2
jupyter notebook --no-browser --ip='*' --port=${PORT} Example.ipynb 
