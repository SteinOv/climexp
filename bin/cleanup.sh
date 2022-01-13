#!/bin/sh
echo `date`" cleanup: starting with "`find ./data/ -type f|wc -l`" files" >> log/log
rm /tmp/readdatfile*
find ./data/ -type f -size 0c -delete
find ./metadata/ -type f -size 0c -delete
find ./data/ -type f -atime +4 -delete
find ./data/ -type f -mtime +30 -delete
find ./data/ -type f -name 'g[0-9]*.dat.gz' -atime +1 -delete
find ./data/ -type f -name 'regionverification*.nc' -atime +1 -delete
find ./data/ -type f -name '*.inf' -mtime +10 -delete
find ./data/ -type f -name '*.info' -mtime +10 -delete
echo '<html><body>No access</body></html>' > data/index.html
for file in ./data/*.inf ./data/*.info
do
    datfile=`head -1 $file | sed -e 's/%%%/000/' -e 's/%%/01/'`
    if [ -n "$datfile" ]
    then
        dir=`dirname $datfile`
        if [ $dir = data -a ! -f "$datfile" ]
        then
	        rm -f "$file"
        fi
    fi
done
find ./atlas/maps/ -type f -atime +30 -delete
find ./atlas/series/ -type f -atime +90 -delete
find ./atlas/regr/ -type f -atime +90 -delete
find ./atlas/diff/ -type f -atime +90 -delete
find ./atlas -type d -empty -exec rmdir {} \;
find ./pid/ -type f -atime +1 -delete
find ./prefs/ -type f -mtime +7 -delete
find ./metadata/ -type f -name 'cache*' -mtime +7 -delete
find ./metadata/data -type f -mtime +7 -delete
find ./synthesis/ -type f -atime +30 -delete
fgrep -l "cannot" ./metadata/*.txt | xargs -n 20 rm -f
fgrep -l "cannot" ./metadata/*.txt.eval | xargs -n 20 rm -f
fgrep -l "does not exist" ./metadata/*.txt | xargs rm -f
fgrep -l "does not exist" ./metadata/*.txt.eval | xargs rm -f
#find /tmp/ -group apache -type f -atime +1 -delete
#find /var/tmp/ -group apache -type f -atime +1 -delete
#find /tmp/ -group www -type f -delete
#find /var/tmp/ -group www -type f -atime +1 -delete
#find /tmp/ -group www-data -type f -delete
#find /var/tmp/ -group www-data -type f -atime +1 -delete
echo `date`" cleanup: finished with "`find ./data/ -type f|wc -l`" files" >> log/log
