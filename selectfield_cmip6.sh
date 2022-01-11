#!/bin/bash
# constructs automatically but off-line the HTML file for the CMIP6 ensemble field selection.
timescale="$1"
lwrite=false # true
if [ -z "$timescale" ]; then
    echo "usage: $0 monthly|annual"
    exit -1
fi
# get the list of vars and models from concatenate_years.sh
server=/data/climexp_cmip6_new/CEeth
nvarmax=6
exps="ssp126 ssp245 ssp370 ssp585"

if [ $timescale = "monthly" ]; then
    vars1="tas tasmin tasmax pr rsds psl" # prw clwvi # evspsbl pme hurs taz
    namevars1="<tr><th colspan=$((2+nvarmax))><a name=surface></a>Surface variables"
    if [ 0 = 1 ]; then
        vars2="rlds rlus rlut rsds rsus rsdt rsut hfss hfls"
        namevars2="<tr><th colspan=$((2+nvarmax))><a name=radiation></a>Radiation variables"
        vars3="mrso mrro mrros snc snd sic tos z200 z500"
        namevars3="<tr><th colspan=$((2+nvarmax))><a name=ocean></a>Land, Ocean, Sea Ice variables"
    fi
    models=`cd $server/tas; ls`
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

for table in 1 # 2 3
do
    case $table in
        1) vars=$vars1;echo $namevars1;;
        2) vars=$vars2;echo $namevars2;;
        3) vars=$vars3;echo $namevars3;;
    esac

    nmodel=-6
    nmodelold=999
    for model in onemean modmean ensmean one mod ens $models
    do
    	pmax_prescribed=1
    	fmax_prescribed=1
        case $model in
            onemean) modelname="CMIP6 mean (one member per model)";;
            modmean) modelname="CMIP6 mean";;
            ensmean) modelname="CMIP6 mean over all members";;
            modmedian) modelname="CMIP6 median";;
            one)     modelname="one member per model";;
            mod)     modelname="all models";;
            ens)     modelname="all members";;
            *)       modelname=$model
                if [ -d $server/pr/$model/r1i1p3f1 ]; then
                    pmax_prescribed=3
                elif [ -d $server/pr/$model/r1i1p2f1 ]; then
                    pmax_prescribed=2
                fi
                if [ -d $server/pr/$model/r1i1p1f3 ]; then
                    fmax_prescribed=3
                elif [ -d $server/pr/$model/r1i1p1f2 ]; then
                    fmax_prescribed=2
                fi
                [ "$lwrite" = true ] && echo "@@@ pmax_prescribed=$pmax_prescribed"
                [ "$lwrite" = true ] && echo "@@@ fmax_prescribed=$fmax_prescribed"
                ;;
        esac
        p=0
        while [ $p -lt $pmax_prescribed ]
        do
        	((p++))
			if [ $pmax_prescribed != 1 ]; then
				modelname="${model} p$p"
				modelp=${model}-p${p}
			else
				modelp=$model
			fi
            f=0
            while [ $f -lt $fmax_prescribed ]
            do
                ((f++))
			    if [ $fmax_prescribed != 1 ]; then
                    modelname="${model} f$f"
                    modelp=${model}-f${f}
                fi
                nmodel=$((nmodel+1))
                nthree=$(( (nmodel-1)/3 ))
                n=0
                if [ $nmodel -gt 0 ]; then
                    n=$(( nmodel - 3*nthree ))
                fi
                [ "$lwrite" = true ] && echo "@@@ nmodel model = $nmodel $modelp p$p f$f"
                if [ $nmodel = -5 -o $nmodel = -2 -o \( $n = 1 -a $nmodel != $nmodelold \) ]; then
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
                nmodelold=$nmodel
                nexp=0
                hasdatas[1]=true
                hasdatas[2]=true
                hasdatas[3]=true
                hasdatas[4]=true
                expfirst=0
                for exp in $exps
                do
                    ((nexp++))
                    hasdata=false
                    for var in $vars; do
                        case $var in
                            ?os) type=Omon;;
                            mr*) type=Lmon;;
                            sic) type=OImon;;
                            sn?) type=LImon;;
                             cdd|altcdd|csdi|cwd|altcwd|dtr|fd|gsl|id|prcptot|r1mm|r10mm|r20mm|r95p|r99p|rx1day|rx5day|sdii|su|tn10p|tn90p|tnn|tnx|tx10p|tx90p|txn|txx|wsdi) type=yr;;
                             tr) type=yr;;
                            *) type=mon;;
                        esac
                        [ "$lwrite" = true ] && echo "@@@ nmodel model = $nmodel $model"
                        if [ $nmodel -le -3 ]; then
                            file="CMIP6/$timescale/$var/${var}_${type}_${model%mean}_${exp}_192_ave.nc"
                            file_alt="CMIP6/$timescale/$var/${var}_${type}_${model%mean}_${exp}_ave.nc"
                        elif [ $nmodel -le 0 ]; then
                            file="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_192_000.nc"
                            file_alt="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_000.nc"
                        else
                            file="CMIP6/$timescale/$var/${var}_${type}_${modelp}_${exp}_192_000.nc"
                            file_alt="CMIP6/$timescale/$var/${var}_${type}_${modelp}_${exp}_000.nc"
                        fi
                        [ "$lwrite" = true ] && echo "@@@ looking for $file"
                        if [ -e $file -o -L $file ]; then
                            hasdata=true
                        else
                            [ "$lwrite" = true ] && echo "@@@ looking for $file_alt"
                            if [ -e $file_alt -o -L $file_alt ]; then
                                hasdata=true; file=$file_alt
                            fi
                        fi
                    done
                    hasdatas[$nexp]=$hasdata
                    if [ $hasdata = true ]; then
                        if [ $expfirst = 0 ]; then
                            expfirst=1
                            if [ $nmodel -gt 0 ]; then
                                echo "<tr><td>$nmodel $modelname"
                            else
                                echo "<tr><td>$modelname"                            
                            fi
                        else
                            echo "<tr><td>&nbsp;"
                        fi
                        echo "<td>$exp"
                        for var in $vars
                        do
                            hasdata=false
                            case $var in
                                ?os) type=Omon;;
                                mr*) type=Lmon;;
                                sic) type=OImon;;
                                sn?) type=LImon;;
                                cdd|altcdd|csdi|cwd|altcwd|dtr|fd|gsl|id|prcptot|r1mm|r10mm|r20mm|r95p|r99p|rx1day|rx5day|sdii|su|tn10p|tn90p|tnn|tnx|tx10p|tx90p|txn|txx|wsdi|tr) type=yr;;
                                *) type=mon;;
                            esac
                            [ "$lwrite" = true ] && echo "@@@ nmodel model = $nmodel $model"
                            if [ $nmodel -le -3 ]; then
                                file="CMIP6/$timescale/$var/${var}_${type}_${model%mean}_${exp}_192_ave.nc"
                                file_alt="CMIP6/$timescale/$var/${var}_${type}_${model%mean}_${exp}_ave.nc"
                            elif [ $nmodel -le 0 ]; then
                                file="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_192_000.nc"
                                file_alt="CMIP6/$timescale/$var/${var}_${type}_${model}_${exp}_000.nc"
                            else
                                file="CMIP6/$timescale/$var/${var}_${type}_${modelp}_${exp}_192_000.nc"
                                file_alt="CMIP6/$timescale/$var/${var}_${type}_${modelp}_${exp}_000.nc"
                            fi
                            [ "$lwrite" = true ] && echo "@@@ looking for $file"
                            if [ -e $file -o -L $file ]; then
                                hasdata=true
                            else
                                [ "$lwrite" = true ] && echo "@@@ looking for $file_alt"
                                if [ -e $file_alt -o -L $file_alt ]; then
                                    hasdata=true; file=$file_alt
                                fi
                            fi

                            if [ $hasdata = true ]; then
                                files=`echo $file | sed -e 's/_000/_[0-9][0-9][0-9]/'`
                                n=`echo $files | wc -w`
                                echo "<td><input type=radio class=formradio name=field value=cmip6_${var}_${type}_${modelp}_${exp}><small>${n}</small>"
                            else
                                echo "<td>&nbsp;<!-- cannot find $file -->"
                            fi
                        done # vars
                    fi # hasdata
                done # exp
                [ "$lwrite" = true ] && echo "@@@ hasdatas=${hasdatas[1]}${hasdatas[2]}${hasdatas[3]}${hasdatas[4]}"
                if [ ${hasdatas[1]} = false -a ${hasdatas[2]} = false -a ${hasdatas[3]} = false -a ${hasdatas[4]} = false ]; then
                    [ "$lwrite" = true ] && echo "@@@ ((nmodel--))"
                    ((nmodel--))
                fi
			done # f
		done # p
    done # model
done # table


