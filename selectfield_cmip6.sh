#!/bin/bash
# constructs automatically but off-line the HTML file for the CMIP6 ensemble field selection.
timescale="$1"
if [ -z "$timescale" ]; then
    echo "usage: $0 monthly|annual"
    exit -1
fi
# get the list of vars and models from concatenate_years.sh
server=/data/climexp_cmip6/CE
if [ $timescale = "monthly" ]; then
    vars1="tas tasmin tasmax pr  psl" # prw clwvi # evspsbl pme hurs taz
    namevars1="<tr><th colspan=$((2+nvarmax))><a name=surface></a>Surface variables"
    if [ 0 = 1 ]; then
        vars2="rlds rlus rlut rsds rsus rsdt rsut hfss hfls"
        namevars2="<tr><th colspan=$((2+nvarmax))><a name=radiation></a>Radiation variables"
        vars3="mrso mrro mrros snc snd sic tos z200 z500"
        namevars3="<tr><th colspan=$((2+nvarmax))><a name=ocean></a>Land, Ocean, Sea Ice variables"
    fi
    models="one ens `ls $server/`"
elif [ $timescale = 'annual' ]; then
    echo "annual not yet ready."; exit -1
    vars1="altcdd csdi altcwd dtr fd gsl id tr prcptot"
    namevars1="<tr><th colspan=$((2+nvarmax))><a name=mix></a>mixed variables"
    vars2="r1mm r10mm r20mm r95p r99p rx1day rx5day sdii su"
    namevars2="<tr><th colspan=$((2+nvarmax))><a name=prcp></a>precipitation extremes"
    vars3="tn10p tn90p tnn tnx tx10p tx90p txn txx wsdi"
    namevars3="<tr><th colspan=$((2+nvarmax))><a name=temp></a>temperature extremes"
else
    echo "$0: error: unknown timescale $timescale"
    exit -1
fi

nvarmax=5
exps="ssp126 ssp245 ssp370 ssp585"

for table in 1 # 2 3
do
    case $table in
        1) vars=$vars1;echo $namevars1;;
        2) vars=$vars2;echo $namevars2;;
        3) vars=$vars3;echo $namevars3;;
    esac

    nmodel=-3
    for model in one ens $models
    do
    	pmax_prescribed=1
    	fmax_prescribed=1
        case $model in
            onemean) modelname="CMIP6 mean (one member per model)";;
            modmean) modelname="CMIP6 mean";;
            modmedian) modelname="CMIP6 median";;
            mod)     modelname="all models";;
            one)     modelname="one member per model";;
            ens)     modelname="all members";;
            *)       modelname=$model
                if [ -d $server/$model/r1i1p3f1 ]; then
                    pmax_prescribed=3
                elif [ -d $server/$model/r1i1p2f1 ]; then
                    pmax_prescribed=2
                fi
                if [ -d $server/$model/r1i1p1f3 ]; then
                    fmax_prescribed=3
                elif [ -d $server/$model/r1i1p1f2 ]; then
                    fmax_prescribed=2
                fi
                ;;
        esac
        p=0
        while [ $p -lt $pmax_prescribed ]
        do
        	((p++))
			if [ $pmax_prescribed != 1 ]; then
				modelname="${model} p$p"
				modelp=${model}_p${p}
			else
				modelp=$model
			fi
            f=0
            while [ $f -lt $fmax_prescribed ]
            do
                ((f++))
			    if [ $fmax_prescribed != 1 ]; then
                    modelname="${model} f$f"
                    modelp=${model}_f${f}
                fi
                nmodel=$((nmodel+1))
                nthree=$(( (nmodel-1)/3 ))
                n=$(( nmodel - 3*nthree ))
                if [ $nmodel = -4 -o $n = 1 ]; then
                    echo "<tr><th>model<th>exp"
                    for var in $vars
                    do
                        case $var in
                            tasmin)  varname="tas<br>min";;
                            tasmax)  varname="tas<br>max";;
                            evspsbl) varname="evsp<br>sbl";;
                            rx1day)  varname="rx1<br>day";;
                            rx5day)  varname="rx5<br>day";;
                            *)       varname=$var;;
                        esac
                        echo "<th>$varname"
                    done
                fi
                nexp=0
                for exp in $exps
                do
                    hasdata=false
                    for var in $vars; do
                        case $var in
                            ?os) type=Omon;;
                            mr*) type=Lmon;;
                            sic) type=OImon;;
                            sn?) type=LImon;;
                             cdd|altcdd|csdi|cwd|altcwd|dtr|fd|gsl|id|prcptot|r1mm|r10mm|r20mm|r95p|r99p|rx1day|rx5day|sdii|su|tn10p|tn90p|tnn|tnx|tx10p|tx90p|txn|txx|wsdi) type=yr;;
                             tr) type=yr;;
                            *) type=Amon;;
                        esac
                        if [ $nmodel -lt 0 ]; then
                            oldfile="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_gn_185001-210012_00.nc"
                        else
                            oldfile="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_i1p${p}f${f}_gn_??????-??????+??????-??????_CEmerged_00.nc"
                        fi
                        file=${oldfile%.nc}0.nc
                        ###echo "looking for $file"
                        if [ -e $file -o -L $file -o -s $oldfile -o -L $oldfile ]; then
                            hasdata=true
                        fi
                    done
                    if [ $hasdata = true ]; then
                        nexp=$((nexp+1))
                        if [ $nexp = 1 ]; then
                            echo "<tr><td>$modelname"
                        else
                            echo "<tr><td>&nbsp;"
                        fi
                        echo "<td>$exp"
                        for var in $vars
                        do
                            case $var in
                                ?os) type=Omon;;
                                mr*) type=Lmon;;
                                sic) type=OImon;;
                                sn?) type=LImon;;
                                cdd|altcdd|csdi|cwd|altcwd|dtr|fd|gsl|id|prcptot|r1mm|r10mm|r20mm|r95p|r99p|rx1day|rx5day|sdii|su|tn10p|tn90p|tnn|tnx|tx10p|tx90p|txn|txx|wsdi|tr) type=yr;;
                                *) type=Amon;;
                            esac
                            if [ $nmodel -lt 0 ]; then
                                oldfile="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_gn_185001-210012_00.nc"
                            else
                                oldfile="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_i1p${p}f${f}_gn_??????-??????+??????-??????_CEmerged_00.nc"
                            fi
                            file=${oldfile%.nc}0.nc
                            if [ -e $file -o -L $file -o -e $oldfile -o -L $oldfile ]; then
                                if [ -e $file -o -L $file ]; then
                                    thefile=$file
                                else
                                    thefile=$oldfile
                                fi
                                files=`echo $thefile | sed -e 's/_000/_???/' -e 's/_00/_??/'`
                                n=`echo $files | wc -w`
                                if [ $nmodel -lt 0 ]; then
                                    ipf=""
                                else
                                    ipf=_i1p${p}f${f}
                                fi
                                echo "<td><input type=radio class=formradio name=field value=cmip6_${var}_${type}_${model}_${exp}${ipf}><small>${n}</small>"
                            else
                                echo "<td>&nbsp;<!-- cannot find $thefile -->"
                            fi
                        done # vars
                    fi # hasdata
                done # exp 
			done # f
		done # p
    done # model
done # table


