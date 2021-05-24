#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "France spring frost study" "time series" nofollow

echo "<b>Time series, minimum Tmin conditioned on a season or GDD threshold.</b>"

for variable in spring gdd150 gdd250 gdd350 "igdd150-250" "igdd250-350" "igdd350-450"; do
    if [ $variable = spring ]; then
        echo "<p>April-July:"
    elif [ ${variable#i} != $variable ]; then
        echo "<p>GDD in ${variable#igdd} K dy:"
    else
        echo "<p>GDD &gt; ${variable#gdd} K dy:"
    fi
    cat <<EOF
<a href="getindices.cgi?WMO=SpringData/ytmin${variable}_BEAUCOUZE&STATION=Tmin_BEAUCOUZE_${variable}&TYPE=i&id=$EMAIL&NPERYEAR=1">Beaucouze</a>,
<a href="getindices.cgi?WMO=SpringData/ytmin${variable}_CHARMEIL&STATION=Tmin_CHARMEIL_${variable}&TYPE=i&id=$EMAIL&NPERYEAR=1">Charmeil</a>,
<a href="getindices.cgi?WMO=SpringData/ytmin${variable}_CHARNEY-LES-MACON&STATION=Tmin_CHARNEY-LES-MACON_${variable}&TYPE=i&id=$EMAIL&NPERYEAR=1">CHarney-Les-Macon</a>,
<a href="getindices.cgi?WMO=SpringData/ytmin${variable}_EOBS&STATION=Tmin_EOBS_${variable}&TYPE=i&id=$EMAIL&NPERYEAR=1">E-OBS</a>,
<a href="getindices.cgi?WMO=SpringData/ytmin${variable}_EURO-CORDEX_%%%&STATION=Tmin_EURO-CORDEX_${variable}&TYPE=i&id=$EMAIL&NPERYEAR=1">EUROCORDEX RCMs</a>.
EOF
done

. ./myvinkfoot.cgi
