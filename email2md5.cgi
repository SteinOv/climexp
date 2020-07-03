#!/bin/bash
# move information from the old email-based log/list to the new md5-based newlist
if [ `uname = Darwin` ]; then
    md5=`echo $EMAIL | md5`
else
    md5=`echo $EMAIL | md5sum | cut -f 1 -d ' '`
fi
username=`fgrep "$EMAIL" ./log/list|cut -f 2 -d ' '|tail -1`
institute=`fgrep "$EMAIL" ./log/list|cut -f 3 -d ' '|tail -1`
echo "^$EMAIL $username $institute $md5 `date`" >> ./log/newlist
for file in prefs/$EMAIL.*; do
    if [ -f $file ]; then
        f=${file#prefs/}
        newfile=prefs/$md5${f#$EMAIL}
        mv $file $newfile
    fi
done
for file in data/*$EMAIL.inf; do
    if [ -f $file ]; then
        f=${file%$EMAIL.inf}
        newfile=$f$md5.inf
        mv $file $newfile
    fi
done
for file in data/*$EMAIL.info; do
    if [ -f $file ]; then
        f=${file%$EMAIL.info}
        newfile=$f$md5.info
        mv $file $newfile
    fi
done
EMAIL=$md5
