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

    git clone https://github.com/fhussonnois/docker-storm.git

Then start zookeeper and the Storm cluster with nimbus:
    
    docker-compose -p storm -f docker-storm/docker-zookeeper.yml up -d
    docker-compose -p storm -f docker-storm/docker-storm.yml up -d 
    
Then start the container with dispel4py, Storm client and Pegasus:

    docker-compose -p pegasus -f ./docker-pegasus.yml up -d
