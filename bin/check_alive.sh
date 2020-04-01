#!/bin/sh
# check whether a website (the climexp) is alive or not.
DEBUG=false
if [ -z "$1" ]; then
  url="http://climexp.knmi.nl/working.cgi"
else
  url=$1
fi
flag=/usr/people/oldenbor/climexp/log/climexp_down
if [ "$DEBUG" = true ]; then
  echo "$0: checking URL $url"
  echo "$0: flag file is $flag"
fi

string=`curl -m 30 -s -S -A checkrobot $url 2>&1`
if [ "$DEBUG" = true ]; then
  echo "$0: got string $string"
fi
if [ -f $flag ]; then
  echo `date`": $string" >> $flag
  if [ "$string" = "OK" ]; then
    if [ "$DEBUG" = true ]; then
      echo "$0: problem cleared, remove flag file, send out e-mail"
    fi
    mv $flag $flag.`date +"%Y-%m-%d-%H-%M"`
    echo "$string" | mail -s "climexp weer OK" oldenborgh@knmi.nl lunix@knmi.nl
  else
    if [ "$DEBUG" = true ]; then
      echo "$0: problem persisting"
    fi
  fi
else
  if [ "$string" != "OK" ]; then
    if [ "$DEBUG" = true ]; then
      echo "$0: flag file does not exist, problem arose, make flag file and send out mail"
    fi
    echo `date`": $string" > $flag
    echo "$string" | mail -s "climexp problemen" oldenborgh@knmi.nl lunix@knmi.nl
  else
    if [ "$DEBUG" = true ]; then
      echo "$0: everything is fine"
    fi
  fi
fi
# check WMO files, i.e., a few.
for file in ncdc_gl_1mean_80_trend_1850-1900.png heat700_global_1mean_80_trend.png maunaloa_f_1mean_80_trend.png
do
    url=http://climexp.knmi.nl/annual_overview_world_weather/$file
    c=`curl --head $url | fgrep -c -i png` 
    if [ $c != 1 ]; then
        echo "$0: error retrieving $url"
    fi
done
