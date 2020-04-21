#!/bin/bash
# script to configure a CentOS instance at teh EWC for use with teh Climate Explorer
# I assume that the climexp code itself and all data are on a persistent data disk

# packages needed for the Climate Explorer
# based on what I installed in fink on macOS
# and honed while tryng to get the Climate Explorer up at SurfSARA
sudo yum -y install httpd
sudo yum -y install gcc-gfortran netcdf-fortran-devel udunits2-devel
sudo yum -y install proj cdo nco bc dos2unix
# this fails on cdo because it is not signed, force
file=`ls -t /var/cache/yum/*/packages/cdo-*.x86_64.rpm | head -1`
sudo rpm --install $file
sudo yum -y install gnuplot netpbm grads gdal
sudo yum -y install lapack-devel fftw-devel
sudo yum -y install R python2-pip # htdig no longer exists
# R also requires all of texlive...
# FGSL is outside the official package repositories, according to 
# https://doku.lrz.de/display/PUBLIC/FGSL+-+A+Fortran+interface+to+the+GNU+Scientific+Library 
# this is the proper way to get it.
sudo rpm -Uvh http://lvserver.ugent.be/yum/xmi-repo-key-7.0-1.el7.noarch.rpm
sudo yum install fgsl fgsl-devel fgsl-doc

if [ ! -s httpd.conf.centos.patch ]; then
    echo "Need file httpd.conf.centos.patch"
    exit -1
fi
if [ -s /etc/httpd/conf/httpd.conf.orig ]; then
    sudo mv /etc/httpd/conf/httpd.conf.orig /etc/httpd/conf/httpd.conf
fi
sudo patch -b /etc/httpd/conf/httpd.conf httpd.conf.centos.patch



pip install jinja2 # already installed

sudo useradd -m oldenbor
sudo mkdir -p ~oldenbor/.ssh
if [ -n "$fixed_this" ]; then
    sudo cat > ~oldenbor/.ssh/authorized_keys <<EOF
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEA05Zxuj4pmrDvyrYIdGfV1jbzqyGdbvdfS8Gynyo4ucz7d9WqIg3haSSlE0d6vQj/tSJT+GPJtctL53kMRCbnkH5mfZYrO+/xaImdPgSWWv4dkHI2762nwp7295/JAPqvwFyOc+b0MlwI4zrDXr7FxX/+ijm9NuTME9NvSJPTXQ0= gj@gatotkaca.local
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAs6ihlDm+M/MrM70W6cLa7axGSz/G7q+dmcgsk1FtI4NVSFnBPPxFzohhGisZZMnNTaMuoqXAonXeLrkkAdXBAJYkRZWbaWtq9mwexA85tMIYmcBlStMszDgDLdCy0q12ViqrThJF5KXysYw28osfYCMGPbeWhsoz9wd42IcNnKU= oldenbor@bsgi33.knmi.nl
EOF
else
    sudo cp ~/.ssh/authorized_keys ~oldenbor/.ssh/
fi
sudo chmod 700 ~oldenbor/.ssh
sudo chmod 600 ~oldenbor/.ssh/authorized_keys
sudo chown -R oldenbor ~oldenbor/.ssh

# open port 80 in the firewall
sudo firewall-cmd --zone=public --add-port=2888/tcp --permanent
sudo firewall-cmd --reload
