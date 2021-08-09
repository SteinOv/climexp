#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Ardennes Eifel Floods" "Time series for the 2021 extreme precipitation and floods study" nofollow

for variable in prcp rx1day rx2day gmst discharge
do
    variablename=$variable
    case $variable in
        prcp) regions="meuse ahrerft pool geul";variablename="Daily precipitation";;
        rx1day) regions="ahrerft pool";variablename="Apr-Sep Rx1day";;
        rx2day) regions="meuse geul pool";variablename="Apr-Sep Rx2day";;
        gmst|sgsat) regions=gmst;variablename="Global Mean Surface Temperature";;
        discharge) regions="meuse ahr erft geul";;
        *) echo "$0: error: cannot handle handle variable $variable yet"; exit -1;;
    esac
    echo "<h3>$variablename</h3>"
        
    for region in $regions
    do
        regionname=$region
        case $region in
            ahrerft) regionname="Ahr and Erft catchments combined";;
            meuse) if [ $variable = discharge ]; then
                    regionname="Meuse at Monsin / Eijsden"
                else
                    regionname="Belgium part of Meuse catchment upstream of Eijsden"
                fi;;
            geul) regionname="Geul catchment upstream of Valkenburg";;
            ahr) regionname="Ahr";;
            erft) regionname="Erft";;
            pool) regionname="Alps to Netherlands";;
        esac
        echo "<p>$regionname:"
        for dataset in eobs eobsprivate era5 regnie belgiumgridded rws racmo eurocordex ETH-COSMO-CPM2p2 UKMO-UM-CPM2p2 EC-EARTH-KIT HadGEM2-KIT MPI-ESM-KIT WRF-EUR-11-EURO-CORDEX WRF-ME-3km DWD-CCLM5-MIROC5 ALARO-0-rcp26 ALARO-0-rcp45 ALARO-0-rcp85 
        do
            name=$dataset
            NPERYEAR=1
            case $dataset in
                eobs*|era5|regnie|belgiumgridded|rws) ens=""
                    if [ $dataset = era5 ]; then
                        name=ERA5
                    elif [ $dataset = eobs ]; then
                        name="E-OBS"
                    elif [ $dataset = eobsprivate ]; then
                        name="E-OBS (private version)"
                    elif [ $dataset = regnie ]; then
                        name="REGNIE"
                    elif [ $dataset = belgiumgridded ]; then
                        name="Belgium gridded"
                    elif [ $dataset = rws ]; then
                        name="Rijkswaterstaat"
                    fi
                    ;;
                racmo) name=RACMO;ens="_%%%";;
                eurocordex) name="EURO-CORDEX (bias-corrected)";ens="_%%%";;
                ETH-COSMO-CPM2p2) name=ETH-COSMO-CPM2p2;ens="_%%%";;
		UKMO-UM-CPM2p2) name=UKMO-UM-CPM2p2;ens="_%%%";;
		EC-EARTH-KIT) name=EC-EARTH-KIT;ens="_%%%";;
                HadGEM2-KIT) name=HadGEM2-KIT;ens="_%%%";;
                MPI-ESM-KIT) name=MPI-ESM-KIT;ens="_%%%";;
                WRF-EUR-11-EURO-CORDEX) name=WRF-EUR-11-EURO-CORDEX;ens="_%%%";;
                WRF-ME-3km) name=WRF-ME-3km;ens="_%%%";;
                DWD-CCLM5-MIROC5) name=DWD-CCLM5-MIROC5;ens="_%%%";;
                ALARO-0-rcp26) name=ALARO-0-rcp26;ens="_%%%";;
                ALARO-0-rcp45) name=ALARO-0-rcp45;ens="_%%%";;
                ALARO-0-rcp85) name=ALARO-0-rcp85;ens="_%%%";;
            esac
            if [ $variable = prcp -o $variable = discharge ]; then
                NPERYEAR=366
            elif [ $variable = gmst -o $variable = sgsat ]; then
                NPERYEAR=12
            elif [ $variable = rx1day -o $variable = rx2day ]; then
                NPERYEAR=1
            else
                echo "$0: error: cannot handle variable $variable yet 2";exit -1
            fi
            [ $region = pool ] && ens="_%%%"
            [ $dataset = none ] && echo "dataset=$dataset, name=$name<br>"
            file=ArdennenEifelData/${variable}_${dataset}_${region}$ens.dat
            firstfile=`echo $file | sed -e 's/%%%/001/'`
            if [ ! -s $firstfile ]; then
                firstfile=${firstfile%dat}nc
            fi
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
