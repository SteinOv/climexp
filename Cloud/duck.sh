#!/bin/sh
/sbin/ifconfig | fgrep inet | fgrep netmask | fgrep -v 127.0.0  | fgrep 136. | fgrep -v 169.254 | head -1 | awk '{print $2}'> $HOME/etc/ip.txt
ip=`cat $HOME/etc/ip.txt | tr -d [:space:]`
echo $ip
echo url="https://www.duckdns.org/update?domains=climexp-test&token=c95cd5cf-fa84-4346-9ada-234566c9d38f&ip=$ip" | curl -s -k -o $HOME/etc/duck.log -K -
