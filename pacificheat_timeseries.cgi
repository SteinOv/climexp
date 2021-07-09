#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Pacific Northwest heat" "Time series for the 2021 heat wave study" nofollow

for variable in tmax txx gmst sgsat
do
    echo "<h3>$variable</h3>"
    case $variable in
        tmax|txx) regions="index Portland Seattle Vancouver";;
        gmst|sgsat) regions=index;;
        *) echo "$0: error: cannot handle handle variable $variable yet"; exit -1;;
    esac
        
    for region in $regions
    do
        echo "<p>$region:"
        for dataset in ghcn ec era5 berkeley flor am2-5c360 ipsl-ehs \
            ACCESS-CM2 AWI-CM-1-1-MR CNRM-CM6-1-HR CNRM-CM6-1 CNRM-ESM2-1 CanESM5 EC-Earth3 \
            FGOALS-g3 GFDL-CM4 INM-CM4-8 INM-CM5-0 IPSL-CM6A-LR MIROC-ES2L MPI-ESM1-2-HR \
            MPI-ESM1-2-LR MRI-ESM2-0 NESM3
        do
            name=$dataset
            NPERYEAR=1
            case $dataset in
                era5|ghcn|ec|berkeley) ens=""
                    if [ $dataset = era5 ]; then
                        name=ERA5
                    elif [ $dataset = ghcn ]; then
                        name="GHCN-D"
                    elif [ $dataset = ec ]; then
                        name="Environment Canada"
                    elif [ $dataset = berkeley ]; then
                        name="Berkeley Earth"
                    fi
                    if [ $variable = tmax ]; then
                        NPERYEAR=366
                    elif [ $variable = gmst -o $variable = sgsat ]; then
                        NPERYEAR=12
                    elif [ $variable = txx ]; then
                        NPERYEAR=1
                    else
                        echo "$0: error: cannot handle variable $variable yet 2";exit -1
                    fi;;
                flor) name=FLOR;ens="_%%%";;
                am2-5c360) name=AM2.5C360P;ens="_%%%";;
            esac
            [ $dataset = none ] && echo "dataset=$dataset, name=$name<br>"
            file=PacificNWData/${variable}_${dataset}_${region}$ens.dat
            firstfile=`echo $file | sed -e 's/%%%/001/'`
            [ $dataset = none ] && echo "looking for $firstfile<br>"
            if [ ! -s $firstfile ]; then
                file=PacificNWData/${variable}_${dataset}_${region}_@@.nc
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
