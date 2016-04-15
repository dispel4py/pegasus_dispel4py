#!/bin/bash
set -x
ssh -i /home/tutorial/docker.openmpi/ssh/id_rsa.mpi tutorial@mpi_head './command-preproces.sh' 
scp -i /home/tutorial/docker.openmpi/ssh/id_rsa.mpi tutorial@mpi_head:/home/tutorial/preprocess_data.zip .
