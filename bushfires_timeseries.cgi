#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Australian fire risk study" "time series" nofollow

cat <<EOF
All time series are averaged over the South-East Australia bush fire region, land points in (155,-29) (150,-29) (144,-40) (155,-40).

<p><i><b>Heat (only reliable after 1910)</b></i><br> 
Monthly: <a href="getindices.cgi?WMO=SEAustralia/giss_temp_250_mask0_5lan_su&STATION=GISS250_bushfire&TYPE=i&id=$EMAIL">GISTEMP T2m</a>,
<a href="getindices.cgi?WMO=SEAustralia/berkeley_tavg_mask0_5lan_su_ext&STATION=t2m_Berkeley_bushfire&TYPE=i&id=$EMAIL">Berkeley T2m</a>,
<a href="getindices.cgi?WMO=SEAustralia/berkeley_tavg_mask0_5lan_su_ext&STATION=t2m_Berkeley_bushfire&TYPE=i&id=$EMAIL">Berkeley Tmax</a>
<br>
Daily fields:
<a href="select.cgi?id=$EMAIL&field=SEAustralia/TMAX_Daily_LatLong1_full_110-155E_-45--10N_su_extended.info">Berkeley Tmax</a>,
<br>
Annual time series:
<a href="getindices.cgi?WMO=SEAustralia/TMAX_Daily_LatLong1_full_110-155E_-45--10N_su_extended.info_4_max_7v_mask0_su&TYPE=i&id=$EMAIL&NPERYEAR=4">Berkeley Tmax</a><br>

<p><i><b>Drought</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/gpccall_10_mask0_su&STATION=GPCC_bushfire&TYPE=i&id=$EMAIL">GPCC</a>,

<p><i><b>Fire Weather Index</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/era5_yearly_seasmax_nsw&STATION=ERA5_FWI&TYPE=i&NPERYEAR=1&id=$EMAIL">ERA5 annual</a>

EOF

. ./myvinkfoot.cgi
