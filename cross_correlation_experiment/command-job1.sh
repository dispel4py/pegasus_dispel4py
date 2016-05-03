#!/bin/bash
set -x
ssh -o StrictHostKeyChecking=no -i /home/tutorial/docker.openmpi/ssh/id_rsa.mpi tutorial@mpi_head './command-preprocess.sh' 
scp -o StrictHostKeyChecking=no -i /home/tutorial/docker.openmpi/ssh/id_rsa.mpi tutorial@mpi_head:/home/tutorial/preprocess_data.zip .
