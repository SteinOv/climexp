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
    for dataset in BEAUCOUZE CHARMEIL CHARNEY-LES-MACON EOBS EURO-CORDEX_%%%
    do
        name=$dataset
        case $dataset in
            BEAUCOUZE) name=Beaucouze;;
            CHARMEIL) name=Charmeil;;
            CHARNEY-LES-MACON) name=Charney-les-Macon;;
            EOBS) name="E-OBS";;
            EURO-CORDEX_%%%) name=EURO-CORDEX;;
        esac
        firstfile=`echo SpringData/ytmin${variable}_$dataset.dat | sed -e 's/%%%/001/'`
        if [ -s $firstfile ]; then
            cat <<EOF
<a href="getindices.cgi?WMO=SpringData/ytmin${variable}_$dataset&STATION=Tmin_${name}_${variable}&TYPE=i&id=$EMAIL&NPERYEAR=1">$name</a>,
EOF
        fi
    done
done

. ./myvinkfoot.cgi
