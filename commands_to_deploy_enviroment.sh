#!/bin/sh
set -x
#if you have already clone the pegasus_dispel4py repository inside pegasus-tutorial
#directory, you do not need to do the first three steps

################# Pegasus Container #####################################

#Step 1
unzip pegasus-tutorial.zip
#Step 2
cd pegasus-tutorail
#Step 3
git clone https://github.com/dispel4py/pegasus_dispel4py

################ Storm Cluster Container ##############
cd pegasus_dispel4py/
cd docker-storm/
git clone https://github.com/dispel4py/storm-docker
cd storm-docker/
sudo docker-compose up -d
sudo docker-compose scale supervisor=3
cd ..
cd ..


################ MPI Cluster Container ##############
git clone https://github.com/dispel4py/docker.openmpi.git
cd docker.openmpi/
sudo docker-compose scale mpi_node=3 mpi_head=1
sudo docker ps
chmod 400 ssh/id_rsa.mpi
cd ..
cd Docker/

################ Composing the Pegasus Container with Storm and MPI ##############
sudo docker-compose -p pegasus -f ./docker-pegasus.yml up -d
sudo docker exec -i -t pegasus_pegasus_1 bash
