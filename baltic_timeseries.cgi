#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Baltic November 2020 temperature anomly study" "time series" nofollow

cat <<EOF


<p><i>Estonia</i><br>
<a href="getindices.cgi?WMO=Baltic/T_Estonia&STATION=November_T_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
EOF

. ./myvinkfoot.cgi
