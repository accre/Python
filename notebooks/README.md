# iPython Notebooks on the ACCRE Cluster

Once this job launches, check the node it landed on with:

		squeue --user=vunetid

Then open tunnel from local machine with something like:

		ssh -L 9999:vmp506:7777 vunetid@login.accre.vanderbilt.edu

This binds port 9999 on localhost to port 7777 on vmp506. You should
replace vmp506 with the name of the node where your job is running, and
vunetid with your VUNetID.

Finally, point your local web browser to localhost:9999.
