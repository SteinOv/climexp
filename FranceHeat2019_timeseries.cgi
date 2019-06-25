#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "France 2019 heat wave study" "time series" nofollow

cat <<EOF
All daily data, take the 3-day average and June max yourself.

<p><b>Observations</b>
<br>France: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iensembles_025_tg_France_metropolitan_su&STATION=EOBS_TG_France">ECA&amp;D</a>,
<a href=getindices.cgi?FranceHeat2019/id=$EMAIL&WMO=FranceHeat2019/iberkeley_tavg_daily_full_France_metropolitan_su&STATION=Berkeley_TG_France">Berkeley</a>
<br>Toulouse: <a href="becatemp.cgi?id=$EMAIL&WMO=33&STATION=TOULOUSE-BLAGNAC">ECA&amp;D</a>

<p><b>Models</b>
<br>Frabce: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_France_metropolitan_su_%%&STATION=EC-Earth23_tas_France">16 EC-Earth 2.3</a>
<br>Toulouse: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_1.38E_43.62N_n_su_%%&STATION=EC-Earth23_tas_Toulouse">16 EC-Earth 2.3</a>
EOF

. ./myvinkfoot.cgi