FROM centos:centos6

MAINTAINER Rajiv Mayani <mayani@isi.edu>

RUN yum -y update

RUN useradd  --create-home --password pegasus123 tutorial

RUN yum -y install which java-1.7.0-openjdk sudo mysql-devel postgresql-devel wget git

# Configure Sudo
RUN echo -e "tutorial ALL=(ALL)       NOPASSWD: /etc/init.d/sshd\n" >> /etc/sudoers

#
# Configure ulimit
#
# NOOOO ----> Limit max filesize      to 4MB
#
#RUN echo -e "ulimit -f 4000" >> /etc/bashrc

# Get Condor yum repo
RUN curl -o /etc/yum.repos.d/condor.repo http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel6.repo
RUN yum -y install --enablerepo=centosplus condor
RUN echo -e "TRUST_UID_DOMAIN = True\n" >> /etc/condor/condor_config.local
RUN echo -e "ALLOW_WRITE = *\n" >> /etc/condor/condor_config.local
RUN usermod -a -G condor tutorial
RUN chmod -R g+w /var/{lib,log,lock,run}/condor

# Get Pegasus yum repo
RUN curl -o /etc/yum.repos.d/pegasus.repo http://download.pegasus.isi.edu/wms/download/rhel/6/pegasus.repo
RUN yum -y install pegasus
#RUN yum -y install graphviz
#RUN rpm -ivh http://download.pegasus.isi.edu/pegasus/4.5.0/pegasus-4.5.0-1.el6.x86_64.rpm 

#RUN cp -rf  /usr/share/doc/pegasus/tutorial/* /home/tutorial/
#RUN chmod +x /home/tutorial/{generate_dax.py,plan_dax.sh} /home/tutorial/bin/*
ADD pegasus/doc/tutorial /home/tutorial/
RUN chown -R tutorial /home/tutorial/

# Configure SCP
RUN yum -y install openssh-server openssh-clients
RUN perl -pi -e 's/^#RSAAuthentication yes/RSAAuthentication yes/' /etc/ssh/sshd_config
RUN perl -pi -e 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
RUN perl -pi -e 's/^PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
RUN perl -pi -e 's/^#UsePAM no/UsePAM no/' /etc/ssh/sshd_config
RUN perl -pi -e 's/^UsePAM yes/#UsePAM yes/' /etc/ssh/sshd_config

#RUN chmod +r /etc/ssh/sshd_config

USER tutorial

RUN mkdir /home/tutorial/.ssh

RUN ssh-keygen -t rsa -C tutorial -b 1024 -f /home/tutorial/.ssh/id_rsa -N ''
RUN cat /home/tutorial/.ssh/id_rsa.pub > /home/tutorial/.ssh/authorized_keys2
RUN chmod 700 /home/tutorial/.ssh/authorized_keys2

RUN echo -e "condor_master > /dev/null 2>&1" >> /home/tutorial/.bashrc
RUN echo -e "sudo /etc/init.d/sshd start > /dev/null 2>&1" >> /home/tutorial/.bashrc

WORKDIR /home/tutorial
