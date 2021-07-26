#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Pacific Northwest heat" "Time series for the 2021 heat wave study" nofollow

for variable in tmax rx1day rx2day gmst
do
    echo "<h3>$variable</h3>"
    case $variable in
        tmax|rx1day) regions="ahrerft pool1 pool2";;
        tmax|rx2day) regions="meuse geul";;
        gmst|sgsat) regions=index;;
        *) echo "$0: error: cannot handle handle variable $variable yet"; exit -1;;
    esac
        
    for region in $regions
    do
        echo "<p>$region:"
        for dataset in eobs era5 regnie
        do
            name=$dataset
            NPERYEAR=1
            case $dataset in
                eobs|era5|regnie) ens=""
                    if [ $dataset = era5 ]; then
                        name=ERA5
                    elif [ $dataset = eobs ]; then
                        name="E-OBS"
                    elif [ $dataset = regnie ]; then
                        name="REGNIE"
                    fi
                    if [ $variable = tmax ]; then
                        NPERYEAR=366
                    elif [ $variable = gmst -o $variable = sgsat ]; then
                        NPERYEAR=12
                    elif [ $variable = rx1day -o $variable = rx2day ]; then
                        NPERYEAR=1
                    else
                        echo "$0: error: cannot handle variable $variable yet 2";exit -1
                    fi;;
                flor) name=FLOR;ens="_%%%";;
                am2-5c360) name=AM2.5C360P;ens="_%%%";;
            esac
            [ $dataset = none ] && echo "dataset=$dataset, name=$name<br>"
            file=ArdennenEifelData/${variable}_${dataset}_${region}$ens.dat
            firstfile=`echo $file | sed -e 's/%%%/001/'`
            [ $dataset = none ] && echo "looking for $firstfile<br>"
            if [ ! -s $firstfile ]; then
                file=ArdennenEifelData/${variable}_${dataset}_${region}_@@.nc
                firstfile=$file
            fi
            ###[ $dataset = era5 ] && echo "looking for $firstfile<br>"
            if [ -s $firstfile ]; then
                file=${file%.nc}
                cat <<EOF
<a href="getindices.cgi?WMO=${file%.dat}&STATION=${variable}_${dataset}_$region&TYPE=i&id=$EMAIL&NPERYEAR=$NPERYEAR">$name</a>,
EOF
            fi
        done
    done
done

. ./myvinkfoot.cgi
