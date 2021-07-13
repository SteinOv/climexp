#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "France spring frost study" "Time series, minimum Tmin conditioned on a season or GDD threshold" nofollow

for variable in spring gdd150 gdd250 gdd350 "igdd150-250" "igdd250-350" "igdd350-450" SGSAT sgsat GSAT GMST gmst; do
    if [ $variable = spring ]; then
        echo "<p>April-July:"
    elif [ ${variable#i} != $variable ]; then
        echo "<p>GDD in ${variable#igdd} K dy:"
    elif [ $variable = SGSAT ]; then
        echo "<p>SGSAT (smoothed global mean near-surface temperature):"        
    elif [ $variable = GMST -o $variable = gmst ]; then
        echo "GMST:"
    elif [ $variable = sgsat -o $variable = GSAT ]; then
        echo "<!-- no new header needed for $variable-->"
    else
        echo "<p>GDD &gt; ${variable#gdd} K dy:"
    fi
    for dataset in BEAUCOUZE CHARMEIL CHARNAY-LES-MACON eobsee_dom \
        EURO-CORDEX_%%% EURO-CORDEX_BEAUCOUZE_%%% EURO-CORDEX_CHARMEIL_%%% EURO-CORDEX_CHARNAY-LES-MACON_%%% EURO-CORDEX_CHARNAY-LES-MACON_%%% \
        CMIP6SEL1_%%% CMIP6SEL1_anom_%%% IPSLCM6_%%% ipslbc_%%% IPSLCM6.%%% highresSST_%%% HighresMIP_%%% HighresMIP_anom_%%% HIRESMIP_%%%
    do
        name=$dataset
        case $dataset in
            BEAUCOUZE) name=Beaucouze;;
            CHARMEIL) name=Charmeil;;
            CHARNAY-LES-MACON) name=Charnay-les-Macon;;
            EURO-CORDEX_BEAUCOUZE_%%%) name="EURO-CORDEX at Beaucouze";;
            EURO-CORDEX_CHARMEIL_%%%) name="EURO-CORDEX at Charmeil";;
            EURO-CORDEX_CHARNAY-LES-MACON_%%%) name="EURO-CORDEX at Charnay-les-Macon";;
            EOBS|eobsee_dom) name="E-OBS";;
            EURO-CORDEX_%%%) name=EURO-CORDEX;;
            CMIP6SEL1_%%%) name="CMIP6 low-bias";;
            CMIP6SEL1_anom_%%%) name="CMIP6 low-bias anom";;
            IPSLCM6?%%%) name="IPSL-CM6";;
            IPSLCM6BC_%%%|ipslbc_%%%) name="IPSL-CM6 bias corrected";;
            highresSST_%%%) name="PRIMAVERA SST-forced bias-corrected";;
            HighresMIP_%%%) name="PRIMAVERA coupled bias-corrected";;
            HighresMIP_anom_%%%) name="PRIMAVERA coupled bias-corrected anom";;
            HIRESMIP_%%%) name="PRIMAVERA coupled bias-corrected anom (new)";;
        esac
        if [ $variable = SGSAT -o $variable = sgsat -o $variable = GMST -o $variable = gmst -o $variable = GSAT ]; then
            firstfile=SpringData/$variable.${dataset%.%%%}.001.dat
            file=$variable.${dataset%_%%%}.%%%
            if [ ! -s $firstfile ]; then
                firstfile=SpringData/$variable.${dataset%_%%%}.001.dat
                file=$variable.${dataset%_%%%}.%%%
            fi
            if [ ! -s $firstfile ]; then
                firstfile=SpringData/$variable.${dataset%_%%%}_001.dat
                file=$variable.${dataset%_%%%}_%%%
            fi
            part=${dataset%_%%%}
            if [ 0 = 1 -a $dataset = HIRESMIP_%%% ]; then
                echo "looking for $firstfile<br>"
                echo "comparing ${part%.%%%} = $part<br>"
            fi
            if [ -s $firstfile -a ${part%.%%%} = $part ]; then
                cat <<EOF
<a href="getindices.cgi?WMO=SpringData/$file&STATION=${variable}_${dataset}&TYPE=i&id=$EMAIL&NPERYEAR=1">$name</a>,
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
