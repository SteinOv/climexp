#!/bin/bash

# packages needed for the Climate Explorer
# based on what I installed in fink on macOS
# and honed while tryng to get the Climate Explorer up at SurfSARA
sudo apt-get install apache2
sudo apt-get install make git autoconf automake autotools-dev pkg-config man cron dos2unix
sudo apt-get install gfortran g++ gdb libnetcdff-dev libudunits2-dev hdf4-tools libgfortran3
sudo apt-get install cdo nco netcdf-bin bc # ncl-ncarg does not work
sudo apt-get install gnuplot-nox netpbm grads gdal-bin
sudo apt-get install libgsl-dev liblapack-dev libfftw3-dev
sudo apt-get install texlive-font-utils # installs all of tex as well.  Oh well.
sudo apt-get install r-base python-pip htdig
sudo apt-get install ufw
sudo pip install jinja2

sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

sudo apt-get install scsitools parted

if [ ! -d /data1 ]; then
sudo rescan-scsi-bus.sh
lsblk
sudo parted /dev/vdb <<EOF
mklabel gpt
mkpart primary 1 -1
EOF
sudo mkfs.ext4 /dev/vdb1
echo "/dev/vdb1 /data1 ext4 defaults 0 0" | sudo tee -a /etc/fstab > /dev/null
cat /etc/fstab 
sudo mkdir /data1
sudo mount -av
fi # -d /data1

cd $HOME
mkdir -p bin
mkdir -p etc
cat > bin/duck.sh <<EOF
#!/bin/sh
mkdir -p \$HOME/etc
/sbin/ifconfig | fgrep inet | fgrep netmask | fgrep -v 127.0.0  | fgrep 136. | fgrep -v 169.254 | head -1 | awk '{print $2}'> \$HOME/etc/ip.txt
ip=`cat \$HOME/etc/ip.txt | tr -d [:space:]`
echo \$ip
/sbin/ifconfig | fgrep inet6 | head -1 | awk '{print $2}' > \$HOME/etc/ip6.txt
ip6=`cat \$HOME/etc/ip6.txt | tr -d [:space:]`
echo \$ip6
echo url="https://www.duckdns.org/update?domains=climexp-test&token=c95cd5cf-fa84-4346-9ada-234566c9d38f&ip=\$ip&ipv6=\$ip6" | curl -s -k -o \$HOME/etc/duck.log -K -
EOF
chmod +x bin/duck.sh
bin/duck.sh


cd $HOME
mkdir -p src
cd src
wget https://doku.lrz.de/download/attachments/43321199/fgsl-1.3.0.tar.gz
tar zxf fgsl-1.3.0.tar.gz
cd fgsl-1.3.0
./configure
make
sudo make install

sudo useradd -m oldenbor
sudo mkdir -p ~oldenbor/.ssh
sudo cp ~/.ssh/authorized_keys ~oldenbor/.ssh/
sudo chmod 700 ~oldenbor/.ssh
sudo chmod 600 ~oldenbor/.ssh/authorized_keys
sudo mkdir -p ~oldenbor/climexp
sudo chmod 755 ~oldenbor
sudo chmod 755 ~oldenbor/climexp
sudo chown -R oldenbor ~oldenbor

cd /var/www
sudo ln -s ~oldenbor/climexp ./climexp
cd $HOME

mkdir ~/Downloads
cd ~/Downloads
wget https://www.earthsystemgrid.org/dataset/ncl.650.dap/file/ncl_ncarg-6.5.0-Debian8.11_64bit_gnu492.tar.gz
cd /usr/local/
pushd /usr/local
mkdir -p ncl-6.5.0
cd ncl-6.5.0
sudo tar zxf ~/Downloads/ncl_ncarg-6.5.0-Debian8.11_64bit_gnu492.tar.gz
cd ..
sudo rm -f ncl
sudo ln -s ncl-6.5.0 ncl
cd ../bin
sudo ln -s ../ncl/bin/ncl
cd $HOME

if [ ! -s apache2.conf.ubuntu.patch ]; then
    echo "$0: please provide apache2.conf.ubuntu.patch"; exit -1
fi
[ -f /etc/apache2/apache2.conf.orig ] && sudo mv /etc/apache2/apache2.conf.orig /etc/apache2/apache2.conf
sudo patch -b /etc/apache2/apache2.conf apache2.conf.ubuntu.patch

if [ ! -s 000-default.conf.patch ]; then
    echo "$0: please provide 000-default.conf.patch"; exit -1
fi
[ -f /etc/apache2/sites-available/000-default.conf.orig ] && sudo mv /etc/apache2/sites-available/000-default.conf.orig /etc/apache2/sites-available/000-default.conf
sudo patch -b /etc/apache2/sites-available/000-default.conf 000-default.conf.patch

if [ ! -s mime.conf.ubuntu.patch ]; then
    echo "$0: please provide mime.conf.ubuntu.patch"; exit -1
fi
[ -f /etc/apache2/mods-available/mime.conf.orig ] && sudo mv /etc/apache2/mods-available/mime.conf.orig /etc/apache2/mods-available/mime.conf
sudo patch -b /etc/apache2/mods-available/mime.conf mime.conf.ubuntu.patch

sudo a2ensite 000-default
sudo a2enmod cgid
sudo a2enmod headers
sudo apachectl start

