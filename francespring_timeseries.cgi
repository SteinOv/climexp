#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "France spring frost study" "time series" nofollow

echo "<b>Time series, minimum Tmin conditioned on a GDD theshold.</b>"

for threshold in 150 250 350; do
cat <<EOF

<p>GDD &gt; $threshold: 
<a href="getindices.cgi?WMO=SpringData/ytmingdd${threshold}_EOBS&STATION=Tmin_EOBS_gdd${threshold}&TYPE=i&id=$EMAIL&NPERYEAR=1">E-OBS</a>,
<a href="getindices.cgi?WMO=SpringData/ytmingdd${threshold}_EURO-CORDEX_%%%&STATION=Tmin_EURO-CORDEX_gdd${threshold}&TYPE=i&id=$EMAIL&NPERYEAR=1">EUROCORDEX RCMs</a>.
EOF
done

. ./myvinkfoot.cgi
