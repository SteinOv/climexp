#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Baltic November 2020 temperature anomaly study" "time series" nofollow

cat <<EOF

<p><i>Estonia</i><br>
<a href="getindices.cgi?WMO=Baltic/November_temp_Estonia&STATION=November_T_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Estonia_su_%%%&STATION=HadGEM3A_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,

<p><i>Latvia</i><br>
<a href="getindices.cgi?WMO=Baltic/avg_nov_temp_LV&STATION=November_T_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Latvia_su_%%%&STATION=HadGEM3A_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,

<p><i>Sweden</i><br>
<a href="getindices.cgi?WMO=Baltic/sweYrlyAnoms_monnr_11&STATION=November_T_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Sweden_su_%%%&STATION=HadGEM3A_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,

<p><i>Denmark</i><br>
<a href="getindices.cgi?WMO=Baltic/DMI_november_1874-2020&STATION=November_T_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Denmark_su_%%%&STATION=HadGEM3A_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
EOF

. ./myvinkfoot.cgi
