#!/bin/bash

. ./init.cgi
. ./getargs.cgi

lwrite=false
if [ "$EMAIL" = ec8907341dfc63c526d08e36d06b7ed8 ]; then
    lwrite=false # true
fi
if [ "$lwrite" = true ]; 
then
    echo "Content-Type: text/html"
    echo 
    echo
fi
export DIR=`pwd`

# defaults
FORM_dipole=no
[ -z "$FORM_minfac" ] && FORM_minfac=30

# filling out two blanks means the whole range
# filling out one blank means using one point.
if [ -z "$FORM_lon2" ]; then
    if [ -z "$FORM_lon1" ]; then
        FORM_lon1='0'
        FORM_lon2='360'
        name_lon="0-360"
    else
        FORM_lon2="$FORM_lon1"
        name_lon="$FORM_lon1"
    fi
else
    if [ -z "$FORM_lon1" -o "$FORM_lon1" = "$FORM_lon2" ]; then
        FORM_lon1="$FORM_lon2"
        name_lon="$FORM_lon2"
    else
        name_lon="${FORM_lon1}-${FORM_lon2}"
    fi
fi
if [ -z "$FORM_lat2" -o "$FORM_lat1" = "$FORM_lat2" ]; then
    if [ -z "$FORM_lat1" ]; then
        FORM_lat1='-90'
        FORM_lat2='90'
        name_lat="-90-90"
    else
        FORM_lat2="$FORM_lat1"
        name_lat="$FORM_lat1"
    fi
else
    if [ -z "$FORM_lat1" ]; then
        FORM_lat1="$FORM_lat2"
        name_lat="$FORM_lat1"
    else
        name_lat="${FORM_lat1}-${FORM_lat2}"
    fi
fi

if [ -n "$EMAIL" -a "$EMAIL" != someone@somewhere ]; then
    cat > ./prefs/$EMAIL.coordinates <<EOF
FORM_lat1=$FORM_lat1;
FORM_lat2=$FORM_lat2;
FORM_lon1=$FORM_lon1;
FORM_lon2=$FORM_lon2;
FORM_maskmetadata=$FORM_maskmetadata;
FORM_intertype=$FORM_intertype;
FORM_minfac=$FORM_minfac;
FORM_masktype=$FORM_masktype;
FORM_gridpoints=$FORM_gridpoints;
FORM_standardunits=$FORM_standardunits;
EOF
fi

. ./queryfield.cgi
FIELDNPERYEAR="$NPERYEAR"
FIELDFILE=$file

if [ -n "$ENSEMBLE" -a $FORM_gridpoints = true ]; then
    echo "Content-Type: text/html"
    echo
    echo
    . ./myvinkhead.cgi "Error" "combination of option and field type not supported"
    cat <<EOF
Sorry, the Climate Explorer can not yet generate sets of grid points in a region for an ensemble of fields. The work-around is to go back one page, at the bottom follow the link "analyse separately" for each ensemble member and generate the set of grid points.
EOF
    . ./myvinkfoot.cgi
    exit
fi

if [ -n "$FORM_maskmetadata" ]; then
    FORM_maskmetadata=data/`basename $FORM_maskmetadata`
    # using a polygon mask
    maskfile=`head -1 $FORM_maskmetadata`
    if [ ! -s $maskfile ]; then
        echo "Content-Type: text/html"
        echo
        echo
        . ./myvinkhead.cgi "Error" "Mask not found"
        cat <<EOF
Something went wrong, cannot locate $maskfile. Please reload it by following the link "add a mask to the list" on the previous page.
EOF
        . ./myvinkfoot.cgi
    fi
    basefile=`basename $maskfile .txt`
    maskname=`head -2 $FORM_maskmetadata |tail -n -1`
    masksp=`tail -n +1 $FORM_maskmetadata`
    if [ "$masksp" = on ]; then
        sp=sp
    else
        sp=""
    fi
    WMO=`basename ${FORM_field} ".$EMAIL.info"`
    WMO=`basename $WMO .ctl`
    WMO=`basename $WMO .nc |tr '%' '_'`_${basefile}$sp
    station="${kindname} ${climfield} $maskname"
else
    # using a rectangular box
    WMO=`basename ${FORM_field} ".$EMAIL.info"`
    WMO=`basename $WMO .ctl`
    WMO=`basename $WMO .nc |tr '%' '_'`_${name_lon}E_${name_lat}N_`echo $FORM_intertype|cut -b 1`
    station="${kindname} ${climfield} ${name_lon}E ${name_lat}N"
fi

if [ "$FORM_noisemodel" != "1" ]; then
    WMO=${WMO}$FORM_noisemodel
fi
if [ -n "$LSMASK" -a "$FORM_masktype" != "all" ]; then
    WMO=${WMO}_${FORM_masktype}
    station="${station} ${FORM_masktype}"
fi
if [ -n "$FORM_standardunits" ]; then
    WMO=${WMO}_su
fi
if [ "$FORM_minfac" != 30 ]; then
    WMO=${WMO}_${FORM_minfac}p
fi
if [ "$FORM_gridpoints" = min -o "$FORM_gridpoints" = max ]; then
    WMO=${WMO}_${FORM_gridpoints}        
fi
if [ -n "$ENSEMBLE" ]; then
    c3=`echo $file | fgrep -c '%%%'`
    if [ $c3 = 0 ]; then
        WMO=${WMO}_++
    else
        WMO=${WMO}_+++
    fi
    station="$station ensemble"
fi
STATION=`echo $station | tr ' ' '_'`
TYPE=i
if [ "$FORM_gridpoints" = min -o "$FORM_gridpoints" = max ]; then
    NAME="$FORM_gridpoints"
else
    NAME=mean
fi
NPERYEAR=${FIELDNPERYEAR:-12}
if [ -n "$LSMASK" -a -n "$FORM_masktype" ]; then
    mask="lsmask $LSMASK $FORM_masktype"
fi
if [ -n "$FORM_maskmetadata" ]; then
    # generate masknetcdf for this particular grid
    basefield=`basename ${WMO#\+*}`
    masknetcdf=data/mask_${basefile}_${basefield}.nc
    if [ -s $masknetcdf ]; then
        size=`cat $masknetcdf | wc -c`
    else
        size=0
    fi
    if [ $size -lt 500 ]; then
        [ -f $masknetcdf ] && rm $masknetcdf
    fi
    if [ ! -s $masknetcdf -o $masknetcdf -ot $maskfile ]; then
        # generate masknetcdf file including the land/sea mask
        onefile=`echo $file | sed -e 's/%%%/000/' -e 's/%%/00/'`
        onefile=`ls $onefile | head -1` # in case there are wildcards in the file name
        if [ ! -s "$onefile" ]; then
            onefile=`echo $file | sed -e 's/%%%/001/' -e 's/%%/01/'`
            onefile=`ls $onefile | head -1`
            if [ ! -s "$onefile" ]; then
                echo "Content-Type: text/html"
                echo
                echo
                . ./myvinkhead.cgi "Error" "Field not found"
                cat <<EOF
Something went wrong, cannot locate $onefile."
EOF
                . ./myvinkfoot.cgi
                exit
            fi
        fi
        polycommand="polygon2mask $onefile $maskfile $sp $mask $masknetcdf"
        echo `date` "$EMAIL ($REMOTE_ADDR) $polycommand" >> log/log
        if [ "$FORM_gridpoints" != field ]; then
            ($polycommand > /tmp/polygon2mask.log) 2>&1 &
        else
            ($polycommand > /tmp/polygon2mask.log) 2>&1
        fi
    fi
    PROG="get_index.sh $file mask $masknetcdf"
else
    PROG="get_index.sh $file $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 dipole $FORM_dipole"
fi

if [ "$FORM_gridpoints" != field ]; then

PROG="$PROG minfac $FORM_minfac $FORM_intertype $FORM_noisemodel $mask $NOMISSING $FORM_standardunits"
[ "$FORM_gridpoints" = max ] && PROG="$PROG max"
[ "$FORM_gridpoints" = min ] && PROG="$PROG min"
#
# try to make the site a bit more student-proof
#
shortprog=`echo $PROG | cut -b 1-100`
count=`ps axuw | fgrep "$shortprog" | fgrep -v fgrep | wc -l | tr -d '[:space:]'`
if [ "$count" -gt 1 ]; then
    echo 'Content-Type: text/html'
    echo 
    . ./myvinkhead.cgi "Try again later" "Multiple attempts to compute the same quantity"
    echo "The same computation seems to be already running, started either by you or another user. It does not make much sense to compute it twice."
    echo "Please try again after the original computation is finished. This can take up to 15 minutes for daily data."
    . ./myvinkfoot.cgi
    exit
fi

export WMO
export file
export TYPE
if [ "$FORM_gridpoints" != true ]; then
    outfile=data/$TYPE$WMO.dat
    if [ -z "$ENSEMBLE" ]; then
        if [ -s $outfile ]; then
            n=`cat $outfile | wc -l`
        else
            n=0
        fi
        if [ $n -gt 10 -a $outfile -nt $file ]; then
            PROG=""
        fi
    fi
    if [ "$splitfield" = true -a "$PROG" != "" ]; then
        warning='<font color="#ff0000">This may take a long time, more than an hour for daily data.</font>'
        if [ -z "$EMAIL" -o "$EMAIL" = someone@somewhere ]; then
            echo 'Content-Type: text/html'
            echo 
            . ./myvinkhead.cgi "Error" "Please register for this operation"
            . ./myvinkfoot.cgi
        fi
    fi
    . ./getdata.cgi
else
    STATION=""
    FORM_field=`basename $FORM_field`
    PROG="$PROG gridpoints $FORM_field"
    if [ -n "$FORM_maskmetadata" ]; then
        m=`basename $maskfile .nc`
        m=`basename $maskfile .txt`
        listname=data/grid_${m}.txt
    else
        listname=data/grid_${FORM_field}_${FORM_lon1}:${FORM_lon2}_${FORM_lat1}:${FORM_lat2}_${FORM_masktype}.txt
    fi
    echo 'Content-Type: text/html'
    echo 
    echo
    . ./myvinkhead.cgi "Set of grid points" "$timese $kindname $climfield"
    ###echo ./bin/$PROG
    echo `date` "$EMAIL ($REMOTE_ADDR) $PROG > $listname" >> log/log
    ( ./bin/$PROG > $listname ) 2>&1
    FORM_climate=`echo "$kindname $climfield" | tr ' ' '_'`
    prog="grid$FORM_field"
    NAME=`basename $listname`
    WMO=grid$WMO
    . ./getstations.cgi
fi

else # subset a field

    cat <<EOF
Content-type: text/html


EOF
    . ./myvinkhead.cgi "Computing subset field" "$kindname $climfield" "noindex,nofollow"
    outfile=`basename $file .ctl`
    outfile=`basename $outfile .nc`
    if [ -n "$FORM_maskmetadata" ]; then
        outfile=data/${outfile}_${basefile}
        newkindname=${kindname}_${basefile}
    else
        outfile=data/${outfile}_${name_lon}E_${name_lat}N
        newkindname=${kindname}_${name_lon}E_${name_lat}N
    fi
    if [ -n "$FORM_standardunits" ]; then
        outfile=${outfile}_su
    fi
    if [ -n "$splitfield" ]; then
        outfile=`echo $outfile | sed -e 's:??*-??*::'`
    fi
    if [ -z "$ENSEMBLE" ]; then
        if [ -f $outfile.nc -a $outfile.nc -nt $file ]; then
            echo "Field already exists<br>"
        else
            if [ -n "$FORM_maskmetadata" ]; then
                if [ 0 = 1 ]; then
                    [ "$lwrite" = true ] && echo cdo maskregion,$maskfile $file $outfile.nc
                    cdo maskregion,$masknetcdf $file $outfile.nc
                else
                    # there still are .ctl files...
                    [ "$lwrite" = true ] && echo ./bin/get_index $file mask $masknetcdf $FORM_standardunits outfield $outfile.nc
                    ./bin/get_index $file mask $masknetcdf $FORM_standardunits outfield $outfile.nc 2>&1 | fgrep -v '# '
                fi
                if [ -n "$LSMASK" -a -s "$LSMASK" ]; then
                    outmask=data/lsmask_`basename $outfile`
                    [ "$lwrite" = true ] && echo ./bin/get_index $LSMASK mask $masknetcdf outfield $outmask.nc
                    ./bin/get_index $LSMASK mask $masknetcdf outfield $outmask.nc 2>&1
                    LSMASK=$outmask.nc
                fi
            else
                [ "$lwrite" = true ] && echo ./bin/get_index $file $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 $FORM_standardunits outfield $outfile.nc
                ./bin/get_index $file $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 $FORM_standardunits outfield $outfile.nc 2>&1
                if [ -n "$LSMASK" -a -s "$LSMASK" ]; then
                    outmask=data/lsmask_`basename $outfile`
                    [ "$lwrite" = true ] && echo ./bin/get_index $LSMASK $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 outfield $outmask.nc
                    ./bin/get_index $LSMASK $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 outfield $outmask.nc 2>&1
                    LSMASK=$outmask.nc
                fi
            fi
            if [ ! -s $outfile.nc ]; then
                . ./myvinkfoot.cgi
                exit
            fi
        fi
    else
        c3=`echo $file | egrep -c '%%%|\+\+\+'`
        i=0
        if [ $c3 = 0 ]; then
            ii=00
            nmax=100
            format=%02i
        else
            ii=000
            nmax=1000
            format=%03i
        fi
        allfiles=`echo $file | sed -e "s:\+\+\+:$ii:" -e "s:\%\%\%:$ii:" -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
        while [ $i -lt $nmax ]; do
            [ "$lwrite" = true ] && echo "i=$i, checking for $ensfile"
            if [ "$splitfield" = true ]; then
                ensfile=`ls -t $allfiles 2>&1 | head -1`
            else
                ensfile=$allfiles
            fi
            if [ -f $ensfile -o -f data/$ensfile ]; then
                [ ! -s $ensfile ] && ensfile=data/$ensfile # I think
                ensout=`echo $outfile | sed -e "s:\+\+\+:$ii:" -e "s:\%\%\%:$ii:" -e "s:\+\+:$ii:" -e "s:\%\%:$ii:" -e 's:??*-??*::'`
                if [ -f $ensout.nc -a $ensout.nc -nt $ensfile ]; then
                    echo "Ensemble member $ii already exists<br>"
                else
                    if [ -n "$FORM_maskmetadata" ]; then
                        if [ 0 = 1 ]; then
                            cdo maskregion,$masknetcdf $ensfile $ensout.nc
                        else
                            if [ "$splitfield" != true ]; then
                                ./bin/get_index $ensfile mask $masknetcdf 5lan $FORM_standardunits outfield $ensout.nc 2>&1 | fgrep -v '# ' 
                            else
                                j=0
                                ensoutfiles=""
                                for ensfile in `echo $allfiles`; do
                                    ((j++))
                                    if [ ! -s ${ensout}_$j.nc -o ${ensout}_$j.nc -ot $ensfile ]; then
                                        echo "`basename $ensfile .nc`<p>"
                                        [ "$lwrite" = true ] && echo "./bin/get_index $ensfile mask $masknetcdf $FORM_standardunits outfield ${ensout}_${j}_$$.nc 2>&1 | fgrep -v '# ' <p>"
                                        ./bin/get_index $ensfile mask $masknetcdf $FORM_standardunits outfield ${ensout}_${j}_$$.nc 2>&1 | fgrep -v '# ' 
                                        mv ${ensout}_${j}_$$.nc ${ensout}_$j.nc
                                    fi
                                    ensoutfiles="$ensoutfiles ${ensout}_$j.nc"
                                done
                                echo "Concatenating partial results...<p>"
                                cdo -r -f nc4 -z zip copy $ensoutfiles ${ensout}_$$.nc 2>&1
                                echo "<br>"
                                mv ${ensout}_$$.nc $ensout.nc
                                rm $ensoutfiles
                            fi
                        fi
                        subsetname="mask $maskname"
                    else # not a mask, hence a rectangular box
                        if [ "$splitfield" != true ]; then
                            [ "$lwrite" = true ] && echo ./bin/get_index $ensfile $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 $FORM_standardunits $ensout.nc
                            echo "generating ensemble member $ii...<p>"
                            ./bin/get_index $ensfile $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 $FORM_standardunits outfield $ensout.nc 2>&1
                        else
                            j=0
                            ensoutfiles=""
                            for ensfile in `echo $allfiles`; do
                                ((j++))
                                if [ ! -s ${ensout}_$j.nc -o ${ensout}_$j.nc -ot $ensfile ]; then
                                    echo "`basename $ensfile .nc`<p>"
                                    ./bin/get_index $ensfile $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 $FORM_standardunits outfield ${ensout}_${j}_$$.nc 2>&1
                                    mv ${ensout}_${j}_$$.nc ${ensout}_$j.nc
                                fi
                                ensoutfiles="$ensoutfiles ${ensout}_$j.nc"
                            done
                            echo "Concatenating partial results...<p>"
                            cdo -r -f nc4 -z zip copy $ensoutfiles ${ensout}_$$.nc 2>&1
                            mv ${ensout}_$$.nc $ensout.nc
                            rm $ensoutfiles
                        fi
                        subsetname="${FORM_lat1}N-${FORM_lat2}N,${FORM_lon1}E-${FORM_lon2}E"
                    fi
                fi
            fi
            i=$((i+1))
            ii=`printf $format $i`
            allfiles=`echo $file | sed -e "s:\+\+\+:$ii:" -e "s:\%\%\%:$ii:" -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
        done
        if [ -n "$LSMASK" -a -s "$LSMASK" ]; then
            outmask=data/lsmask_`basename $outfile | tr '%' '0'`
            if [ -n "$FORM_maskmetadata" ]; then
                [ "$lwrite" = true ] && echo ./bin/get_index $LSMASK mask $masknetcdf outfield $outmask.nc
                ./bin/get_index $LSMASK mask $masknetcdf $FORM_standardunits outfield $outmask.nc 2>&1
            else
                [ "$lwrite" = true ] && echo ./bin/get_index $LSMASK $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 $FORM_standardunits outfield $outmask.nc
                ./bin/get_index $LSMASK $FORM_lon1 $FORM_lon2 $FORM_lat1 $FORM_lat2 outfield $outmask.nc 2>&1
            fi
            LSMASK=$outmask.nc
        fi
    fi
    infofile=$outfile.$EMAIL.info
    cat > $infofile <<EOF
$outfile.nc
NPERYEAR=$NPERYEAR
LSMASK=$LSMASK
$newkindname
$climfield
EOF
    FORM_field="$infofile"
    splitfield=false # no longer a split field
    STATION="" # otherwise the series menu pops up...
    kindname=$newkindname
    . ./select.cgi

fi
