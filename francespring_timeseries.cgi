#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "France spring frost study" "time series" nofollow

echo "<b>Time series, minimum Tmin conditioned on a season or GDD threshold.</b>"

for variable in spring gdd150 gdd250 gdd350 "igdd150-250" "igdd250-350" "igdd350-450" SGSAT GMST gmst; do
    if [ $variable = spring ]; then
        echo "<p>April-July:"
    elif [ ${variable#i} != $variable ]; then
        echo "<p>GDD in ${variable#igdd} K dy:"
    elif [ $variable = SGSAT ]; then
        echo "<p>SGSAT (smoothed global mean near-surface temperature):"        
    elif [ $variable = GMST -o $variable = gmst ]; then
        echo "GMST:"
    else
        echo "<p>GDD &gt; ${variable#gdd} K dy:"
    fi
    for dataset in BEAUCOUZE CHARMEIL CHARNAY-LES-MACON EOBS \
        EURO-CORDEX_%%% EURO-CORDEX_BEAUCOUZE_%%% EURO-CORDEX_CHARMEIL_%%% EURO-CORDEX_CHARNAY-LES-MACON_%%% EURO-CORDEX_CHARNAY-LES-MACON_%%% \
        CMIP6SEL1_%%% CMIP6SEL1_anom_%%% IPSLCM6_%%% IPSLCM6BC_%%% highresSST_%%% HighresMIP_%%% HighresMIP_anom_%%%
    do
        name=$dataset
        case $dataset in
            BEAUCOUZE) name=Beaucouze;;
            CHARMEIL) name=Charmeil;;
            CHARNAY-LES-MACON) name=Charnay-les-Macon;;
            EURO-CORDEX_BEAUCOUZE_%%%) name="EURO-CORDEX at Beaucouze";;
            EURO-CORDEX_CHARMEIL_%%%) name="EURO-CORDEX at Charmeil";;
            EURO-CORDEX_CHARNAY-LES-MACON_%%%) name="EURO-CORDEX at Charnay-les-Macon";;
            EOBS) name="E-OBS";;
            EURO-CORDEX_%%%) name=EURO-CORDEX;;
            CMIP6SEL1_%%%) name="CMIP6 low-bias";;
            CMIP6SEL1_anom_%%%) name="CMIP6 low-bias anom";;
            IPSLCM6_%%%) name="IPSL-CM6";;
            IPSLCM6BC_%%%) name="IPSL-CM6 bias corrected";;
            highresSST_%%%) name="PRIMAVERA SST-forced bias-corrected";;
            HighresMIP_%%%) name="PRIMAVERA coupled bias-corrected";;
            HighresMIP_anom_%%%) name="PRIMAVERA coupled bias-corrected anom";;
        esac
        if [ $variable = SGSAT -o $variable = GMST -o $variable = gmst ]; then
            firstfile=SpringData/$variable.${dataset%_%%%}.001.dat
            if [ -s $firstfile ]; then
                cat <<EOF
<a href="getindices.cgi?WMO=SpringData/$variable.${dataset%_%%%}.%%%&STATION=${variable}_${dataset}&TYPE=i&id=$EMAIL&NPERYEAR=1">$name</a>,
EOF
            fi
        else
            firstfile=`echo SpringData/ytmin${variable}_$dataset.dat | sed -e 's/%%%/001/'`
            if [ -s $firstfile ]; then
                cat <<EOF
<a href="getindices.cgi?WMO=SpringData/ytmin${variable}_$dataset&STATION=Tmin_${name}_${variable}&TYPE=i&id=$EMAIL&NPERYEAR=1">$name</a>,
EOF
            fi
        fi
        ###echo "firstfile=$firstfile<br>"
    done
done

. ./myvinkfoot.cgi
