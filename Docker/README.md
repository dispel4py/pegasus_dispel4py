# dispel4py and Pegasus docker image

To build the image:

    git clone https://github.com/pegasus-isi/pegasus.git
    docker build -t pegasus_dispel4py .
    docker run -i -t pegasus_dispel4py bash

Inside the container:

    su tutorial
    cd pegasus_dispel4py/simple_experiment/
    python dax-dispel4py.py
    pegasus-plan --conf pegasusrc --dax dispel4py.dax --sites local --submit

Then watch progress of the job using the displayed job id, e.g.:

    pegasus-status -l /home/tutorial/pegasus_dispel4py/simple_experiment/tutorial/pegasus/dispel4py/20160318T215222+0000


# Run a cluster with Storm

Clone the docker composition:

    git clone https://github.com/dispel4py/storm-docker.git
    docker-compose up -d
    docker-compose scale supervisor=3
    
Note: This Storm-cluster has installed dispel4py, numpy, scipy, networkx, obspy python libraries

Then start the container with dispel4py, Storm client and Pegasus:

    docker-compose -p pegasus -f ./docker-pegasus.yml up -d

Log into the running Pegasus container:

    docker exec -i -t pegasus_pegasus_1 bash


# Run a cluster with MPI (OpenMPI + mpi4py)

Clone the docker composition:

    git clone https://github.com/dispel4py/docker.openmpi.git
    docker-compose up -d
    docker-compose scale mpi_node=16 mpi_head=1

Check the port that mpi_head is using:
    
    docker ps

Now you know the port, you can login to the mpi_head container. The username is mpirun.
It has been configured mpriun user to need password to login by ssh. However, id_rsa.mpi key might need to be indicated.
 
    chmod 400 ssh/id_rsa.mpi
    ssh -i ssh/id_rsa.mpi -p 23227 mpirun@localhost

Once logged in the MPI-cluster, you need to configure:

     export LD_LIBRARY_PATH=/usr/lib/openmpi/lib/

For testing an mpi4py example using the mpi_nodes:
	
	cd mpi4py_benchmarks
	create machines file from /etc/hosts (copy only the IP adresses, nothing else)
	mpirun -hostfile machines -np 3 python helloworld.py 	

For testing dispel4py with mpi mapping:
     
	mpiexec -n 6 dispel4py mpi dispel4py.examples.graph_testing.pipeline_test	

Note: This MPI-cluster has installed dispel4py, numpy, scipy, networkx, obspy python libraries

Then start the container with dispel4py, Storm client and Pegasus:

    docker-compose -p pegasus -f ./docker-pegasus.yml up -d

Log into the running Pegasus container:

    docker exec -i -t pegasus_pegasus_1 bash

Inside the Pegasus container, you can connect to the MPI-cluster like this:
   
    ssh -i docker.openmpi/ssh/id_rsa.mpi mpirun@mpi_head


