#!/bin/bash
#
# script to configure teh Climate Explorer, part that is independent of OS
# assumes user oldenbor has been created and ~oldenbor/climexp exists and is on a big disk
# runs as user oldenbor

chmod 755 $HOME

c=`fgrep -c 'ulimit -s unlimited' ~/.profile`
if [ -z "$c" ]; then
    echo "ulimit -s unlimited" > ~/.profile
elif [ $c = 0 ]; then
    echo "ulimit -s unlimited" >> ~/.profile
fi
c=`fgrep -c PVM_ARCH ~/.profile`
if [ "$c" = 0 ]; then
    name=`uname`
    case $name in
        Linux) export PVM_ARCH=LINUX;;
        Darwin) export PVM_ARCH=NEXT;;
        *) echo "$0: error: do not know uname $name"; exit -1;;
    esac
    echo "export PVM_ARCH=$PVM_ARCH" >> ~/.profile
fi

# get the source code
[ ! -f climexp/start.cgi ] && git clone git@gitlab.com:KNMI-OSS/climexp/climexp.git
[ ! -d climexp_numerical ] && git clone git@gitlab.com:KNMI-OSS/climexp/climexp_numerical.git
[ ! -d climexp_data ] && git clone git@gitlab.com:KNMI-OSS/climexp/climexp_data.git

# make directories that should be writable by apache.
cd climexp
for dir in data log prefs pid atlas metadata synthesis country_masks natvar
do
    mkdir -p $dir
    chmod go+w $dir
done
cd log
touch newlist log
chmod go+w newlist log
ln -s /var/log/apache2/error_log
ln -s /var/log/apache2/access_log
cd $HOME

# compile the Fortran (and a few C and C++ programs)
cd climexp_numerical
mkdir -p $PVM_ARCH
cd $PVM_ARCH
if [ $PVM_ARCH = LINUX ]; then
    ln -s ../Makefile.linux_gfortran_64 Makefile
elif [ $PVM_ARCH = NEXT ]; then
    ln -s ../Makefile.next_gfortran64 Makefile
fi
ln -s /usr/local/include/fgsl/fgsl.mod
cd ..
cd src
ln -s /usr/include/netcdf.inc
cd ..
make
make install
cd $HOME

cd $HOME/climexp
for dir in ../climexp_data/*; do
    if [ -d $dir ]; then
        ln -s $dir
    fi
done

if [ -d /usr/share/grads ]; then
    cp -r /usr/share/grads/* $HOME/climexp/grads/
fi

cd ~/climexp_numerical/$PVM_ARCH
R CMD SHLIB ../src/rkillfile.f
R CMD SHLIB ../src/rkeepalive.f
cd ~/climexp/r
ln -s ../../climexp_numerical/src/rkillfile.so 
ln -s ../../climexp_numerical/src/rkeepalive.so 
R <<EOF
install.packages("SpecsVerification")
install.packages("RNetCDF")
install.packages("evd")
install.packages("ismev")
install.packages("verification")
quit()
n
EOF

crontab - <<EOF
0 3 * * * curl -s http://localhost/cleanup.cgi > /dev/null
5,20,35,50 * * * * curl -s http://localhost/randomimage.cgi > /dev/null
EOF

