#!/bin/bash
lwrite=false
if [ -n "$EMAIL" -a "$EMAIL" = ec8907341dfc63c526d08e36d06b7ed8 ]; then
    lwrite=false # true
    ###set -x
fi
if [ -z "$DIR" ]; then
    DIR=`pwd`
fi
PROG=`basename $0 .sh`
if [ -z "$file" ]; then
    echo "error: \$file is undefined!"
    exit -1
fi
if [ -z "$TYPE$WMO" ]; then
    echo "error: \$TYPE\$WMO is undefined!"
    exit -1
fi
c1=`echo $file | fgrep -c '%%'`
c2=`echo $file | fgrep -c '++'`
c3=`echo $file | egrep -c '%%%|\+\+\+'`
c4=`echo $file | fgrep -c '@@'`
if [ "$c4" = 1 ]; then
    # one file with multiple ensemble members, the programs called from this script cannot handle that
    # convert to old-fashioned ensemble
    eval `getunits $file`
    iens=-1
    alloutfile=`echo $file | sed -e "s/@@/\+\+\+/"`
    touch $alloutfile
    while [ $iens -lt $NENS ]; do
        ((iens++))
        iiens=`printf %03i $iens`
        outfile=`echo $file | sed -e "s/\@\@/$iiens/"`
        echo -n $iens 1>&2
        if [ ! -s $outfile ]; then
            seriesensanomal $iens $file noanom > $outfile
            c=`fgrep -v '#' $outfile | wc -l`
            if [ $c -lt 10 ]; then
                rm $outfile
            fi
        fi
        if [ -s $outfile ]; then
            echo "# $outfile" >> $alloutfile
        fi
    done
    c3=1 # it is an old-fashioned ensemble now, quite a bit of redundant information...
    c2=1 # need both :-(
    file=$alloutfile
    WMO=`echo $WMO | sed -e "s/\@\@/\+\+\+/"`
    lwrite=true
fi
if [ $c1 -eq 0 -a $c2 -eq 0 ]
then
    outfile=data/$TYPE$WMO.dat
    allfiles=`echo $file | sed -e "s:\+\+\+:$ii:" -e "s:\%\%\%:$ii:" -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
    if [ "$splitfield" = true ]; then
        onefile=`ls -t $allfiles 2>&1 | head -1`
    else
        onefile=$allfiles
    fi
    if [ ! -s $outfile -o $outfile -ot $onefile ]; then
        if [ "$splitfield" != true ]; then
            [ $lwrite = true ] && echo "# $DIR/bin/$PROG $*"
            $DIR/bin/$PROG $*
        else
            outfile=/tmp/get_index.$$
            touch $outfile
            allfiles=`echo $file`
            for f in $allfiles; do
                args=`echo "$*" | sed -e "s@$file@$f@" -e "s@$allfiles@$f@"`
                [ "$lwrite" = true ] && echo "# $DIR/bin/$PROG $args" 1>&2
                $DIR/bin/$PROG $args >> $outfile
            done
            # collect all the metadata at the top. note it will give duplicate history etc attributes
            sed -e 's/^ *//' $outfile | sort | uniq
            rm $outfile
        fi
    else
        cat $outfile
    fi
else
    i=0
    if [ $c3 = 0 ]; then
        ii=00
        nmax=100
        format="%02i"
    else
        ii=000
        nmax=1000
        format="%03i"
    fi
    allfiles=`echo $file | sed -e "s:+++:$ii:" -e "s:\%\%\%:$ii:" -e "s:++:$ii:" -e "s:\%\%:$ii:"`
    if [ "$splitfield" = true ]; then
        ensfile=`ls -t $allfiles 2>&1 | head -1`
    else
        ensfile=$allfiles
    fi
    [ "$lwrite" = true ] && echo "log..." > /tmp/aap
    while [ $i -lt $nmax ]
    do

        [ "$lwrite" = true ] && echo "ensfile = $ensfile" >> /tmp/aap
        if [ -s "$ensfile" -o -s "data/$ensfile" ]
        then
            ensout=`echo data/$TYPE$WMO.dat | sed -e "s@+++@$ii@" -e "s@\%\%\%@$ii@" -e "s@++@$ii@" -e "s@\%\%@$ii@"`
            if [ ! -s $ensout ]; then
                touch $ensout.tmp$$
                [ "$lwrite" = true ] && echo "allfiles=$allfiles" >> /tmp/aap
                for ensfile in `echo $allfiles`
                do
                    [ "$splitfield" = true ] && echo "`basename $ensfile .nc`<p>" 1>&2
                    ensargs=`echo $* | sed -e 's/\@\@/\+\+\+/' | sed -e "s@$file@$ensfile@"`
                    [ "$lwrite" = true ] && echo "$DIR/bin/$PROG $ensargs >> $ensout.tmp$$" >> /tmp/aap
                    $DIR/bin/$PROG $ensargs >> $ensout.tmp$$
                    c=`fgrep -v '#' $ensout.tmp$$ | wc -l`
                    if [ $c = 0 ]; then
                        echo "<br>Something went wrong in bin/$PROG $ensargs" 1>&2
                        echo "<br>Retrying...<br>" 1>&2
                        $DIR/bin/$PROG $ensargs >> $ensout.tmp$$
                        c=`fgrep -v '#' $ensout.tmp$$ | wc -l`
                        if [ $c = 0 ]; then
                            echo "<br>Something again went wrong $c" 1>&2
                            echo "<br>Retrying...<br>"  1>&2
                            $DIR/bin/$PROG $ensargs >> $ensout.tmp$$
                            c=`fgrep -v '#' $ensout.tmp$$ | wc -l`
                            if [ $c = 0 ]; then
                                echo "<br>And again $c" 1>&2
                                echo "<br>Retrying for the last time...<br>"  1>&2
                                $DIR/bin/$PROG $ensargs >> $ensout.tmp$$
                                c=`fgrep -v '#' $ensout.tmp$$ | wc -l`
                                if [ $c = 0 ]; then
                                    rm $ensout.tmp$$
                                    echo "<br>$0: error in bin/$PROG $ensargs > $ensout.tmp$$<br>" 1>&2
                                fi
                            fi
                        fi
                    fi
                done
                # to prevent incomplete series if the process is interrupted (assuming the same pid dpes not come up)
                # also sort to collect all metadata at the top
                sed -e 's/^ *//' $ensout.tmp$$ | sort | uniq > $ensout
                rm $ensout.tmp$$
            fi
            echo "# $ensout"
        fi
        i=$((i+1))
        ii=`printf $format $i`
        allfiles=`echo $file | sed -e "s:\+\+\+:$ii:" -e "s:\%\%\%:$ii:" -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
        if [ "$splitfield" = true ]; then
            ensfile=`ls -t $allfiles 2>&1 | head -1`
            [ -z "$ensfile" ] && ensfile="bestaatniet"
        else
            ensfile=$allfiles
        fi
        [ "$lwrite" = true ] && echo "ensfile=$ensfile" >> /tmp/aap
        if [ $((i%100)) = 0 -a \( -s "$ensfile" -o -s "data/$ensfile" \) ]; then
            echo "Processing $i...<p>" 1>&2
        fi
    done
fi
