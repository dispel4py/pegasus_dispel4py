#!/bin/sh
set -x
# Note1: You might not need root rights for executing docker commands in your machine. 
# Note2: If you have already cloned the pegasus_dispel4py repository inside pegasus-tutorial
# directory, you not need to execute the first four steps
################# Pegasus Container #####################################

#Step 1
unzip pegasus-tutorial.zip
#Step 2
cd pegasus-tutorial
#Step 3
git clone https://github.com/dispel4py/pegasus_dispel4py
#Step 4
cd pegasus_dispel4py/
################ Storm Cluster Container ##############
cd docker-storm/
git clone https://github.com/dispel4py/storm-docker
cd storm-docker/
sudo docker-compose up -d
sudo docker-compose scale supervisor=16
cd ..
cd ..


################ MPI Cluster Container ##############
git clone https://github.com/dispel4py/docker.openmpi.git
cd docker.openmpi/
sudo docker-compose scale mpi_node=16 mpi_head=1
sudo docker ps
chmod 400 ssh/id_rsa.mpi
cd ..
cd Docker/

################ Composing the Pegasus Container with Storm and MPI ##############
sudo docker-compose -p pegasus -f ./docker-pegasus.yml up -d
sudo docker exec -i -t pegasus_pegasus_1 bash
