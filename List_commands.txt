#!/bin/sh
unzip pegasus-tutorial.zip
cd pegasus-tutorail
git clone https://github.com/dispel4py/pegasus_dispel4py
cd pegasus_dispel4py/
cd docker-storm/
git clone https://github.com/dispel4py/storm-docker
cd storm-docker/
sudo docker-compose up -d
sudo docker-compose scale supervisor=3
cd ..
cd ..
git clone https://github.com/dispel4py/docker.openmpi.git
cd docker.openmpi/
sudo docker-compose scale mpi_node=3 mpi_head=1
sudo docker ps
chmod 400 ssh/id_rsa.mpi
cd ..
cd Docker/
sudo docker-compose -p pegasus -f ./docker-pegasus.yml up -d
sudo docker exec -i -t pegasus_pegasus_1 bash
