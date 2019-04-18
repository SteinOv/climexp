#!/bin/bash
[ -z "$EOFID" ] && EOFID=$1
if [ -z "$EOFID" ]; then
  echo "$0: cannot find EOFID"
  echo "$0: cannot find EOFID" 1>&2
  exit -1
fi
if [ -n "$DEBUG" ]; then
    echo $0 $1 > /tmp/kill.log
    echo '-------------' >> /tmp/kill.log
    ps axw | fgrep 'stillcomputing.cgi' | fgrep -v 'kill_' >> /tmp/kill.log
    echo '-------------' >> /tmp/kill.log
    ps axw | fgrep 'stillcomputing.cgi' | fgrep -v 'kill_' | egrep " $EOFID" >> /tmp/kill.log
    echo '-------------' >> /tmp/kill.log
    ps axw | fgrep 'stillcomputing.cgi' | fgrep -v 'kill_' | egrep " $EOFID" | cut -d ' ' -f 1 >> /tmp/kill.log
    echo '-------------' >> /tmp/kill.log
fi
pid=`ps axw | fgrep 'stillcomputing.cgi' | fgrep -v 'kill_' | egrep " $EOFID" | cut -d ' ' -f 1`
if [ -z "$pid" ]; then
  echo "$0: cannot find pid"
  echo "$0: cannot find pid" 1>&2
  exit -1
fi
kill $pid > /dev/null 1>&2
