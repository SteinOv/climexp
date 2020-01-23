#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Australian fire risk study" "time series" nofollow

cat <<EOF
<i><b>Heat</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/igiss_temp_250_mask0_5lan_su&STATION=GISS250_bushfire&TYPE=i&id=$EMAIL">GISTEMP</a>,

<p><i><b>Drought</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/gpccall_10_mask0_su&STATION=GPCC_bushfire&TYPE=i&id=$EMAIL">GPCC</a>,

<p><i><b>Fire Weather Index</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/era5_yearly_seasmax_nsw&STATION=ERA5_FWI&TYPE=i&NPERYEAR=1&id=$EMAIL">ERA5 annual</a>

EOF

. ./myvinkfoot.cgi
