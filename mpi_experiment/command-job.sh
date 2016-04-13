#!/bin/bash
set -x
ssh -i /home/tutorial/docker.openmpi/ssh/id_rsa.mpi mpirun@mpi_head 'mpiexec -n 6 -hostfile machines dispel4py mpi dispel4py.examples.graph_testing.pipeline_test -i 10' 
