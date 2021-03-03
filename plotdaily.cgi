#!/bin/bash
#
# plot the last N days of a dailytime series, inspired by the CPC/NCEP graphs at 
# http://www.cpc.ncep.noaa.gov/products/global_monitoring/temperature/global_temp_accum.shtml
#
. ./init.cgi
. ./nosearchenginewithheader.cgi
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi
NPERYEAR="$FORM_NPERYEAR"
if [ $EMAIL = ec8907341dfc63c526d08e36d06b7ed8 ]; then
    lwrite=false # true
fi

TYPE="$FORM_TYPE"
WMO=`echo "$FORM_WMO" | tr -d '\\'`
STATION="$FORM_STATION"
station=`echo "$STATION" | tr '_' ' '`
NAME="$FORM_NAME"
name=`echo "$NAME" | tr '_' ' '`
if [ ! -s ./data/$TYPE$WMO.dat ]; then
    . ./myvinkhead.cgi "Error" "Cannot find file"
    echo "Cannot find file $TYPE$WMO.dat"
    . ./myvinkfoot.cgi
    exit
fi

# arguments trump remembered values
nday="$FORM_nday"
yr=$FORM_yr
mo=$FORM_mo
dy=$FORM_dy
cdf=$FORM_cdf
anom=$FORM_anom
climyear1=$FORM_climyear1
climyear2=$FORM_climyear2
whitelo=$FORM_whitelo
whitehi=$FORM_whitehi
ylo=$FORM_ylo
yhi=$FORM_yhi
if [ "$lwrite" = true ]; then
    echo "After argument processing nday=$nday<br>"
fi

arg_enddate=$FORM_enddate
if [ $EMAIL != someone@somewhere ]; then
    def=prefs/$EMAIL.plotdaily.$NPERYEAR
    if [ -f $def ]; then
        eval `egrep '^FORM_[a-z0-9]*=[a-zA-Z]*[-+0-9.%]*;$' $def`
    fi
fi

[ -z "$nday" ] && nday="$FORM_nday"
[ -z "$yr" ] && yr=$FORM_yr
[ -z "$mo" ] && mo=$FORM_mo
[ -z "$dy" ] && dy=$FORM_dy
[ -z "$cdf" ] && cdf=$FORM_cdf
[ -z "$anom" ] && anom=$FORM_anom
# do not use values from savefile if called with empty arguments from form
[ -z "$climyear1" -a "$arg_enddate" = last ] && climyear1=$FORM_climyear1
[ -z "$climyear2" -a "$arg_enddate" = last ] && climyear2=$FORM_climyear2
[ -z "$whitelo" ] && whitelo=$FORM_whitelo
[ -z "$whitehi" ] && whitehi=$FORM_whitehi
[ -z "$ylo" ] && ylo=$FORM_ylo
[ -z "$yhi" ] && yhi=$FORM_yhi
if [ "$lwrite" = true ]; then
    echo "After remembering last time nday=$nday<br>"
fi

eval `./bin/getunits ./data/$TYPE$WMO.dat`
[ -z "$nday" ] && nday=$NPERYEAR
if [ -n "$mo" -a "${mo#0}" = "$mo" ]; then
    [ $mo -le 9 ] && mo=0$mo
fi
if [ -n "$dy" -a "${dy#0}" = "$dy" ]; then
    [ $dy -le 9 ] && dy=0$dy
fi
enddate="$yr$mo$dy"
if [ -z "$enddate" -o "$arg_enddate" = last ]; then
    enddate=last
    last="Last "
else
    ending=" ending at $enddate"
fi

. ./nperyear2timescale.cgi
. ./myvinkhead.cgi "$last$nday ${month}s of $station $name" "" "noindex,nofollow"

if [ -n "$FORM_climyear1" -a -z "$FORM_climyear2" ]; then
    echo "Error: provide begin and end year of reference period"
    . ./myvinkfoot.cgi
    exit
fi
if [ -z "$FORM_climyear1" -a -n "$FORM_climyear2" ]; then
    echo "Error: provide begin and end year of reference period"
    . ./myvinkfoot.cgi
    exit
fi
if [ -z "$FORM_climyear1" -a -z "$FORM_climyear2" ]; then
    computed="computed with all data available"
    if [ "$anom" != zero ]; then
        period="all data"
    fi
    beginend=""
else
    computed="computed over the period ${FORM_climyear1}:${FORM_climyear2}"
    if [ "$anom" != zero ]; then
        period="${FORM_climyear1}:${FORM_climyear2}"
    fi
    beginend="begin ${FORM_climyear1} end ${FORM_climyear2}"
fi

eval `./bin/getunits ./data/$TYPE$WMO.dat`
root=data/plot${nday}last$TYPE$WMO$KIND${FORM_climyear1}${FORM_climyear2}_$enddate
if [ "$anom" = zero ]; then
    anomarg=anom
    root=data/plot${nday}last$TYPE$WMO${KIND}_$enddate
else
    root=data/plot${nday}last$TYPE$WMO$KIND${FORM_climyear1}${FORM_climyear2}_$enddate
fi
if [ -z "$cdf" ]; then
    if [ "$NEWUNITS" = "mm/day" -o "$TYPE" = p ]; then
        cdf=on
    else
        cdf=off
    fi
fi
if [ $cdf = on ]; then
    cdfarg=cdf
else
    cdfarg=""
fi

echo `date` "$EMAIL ($REMOTE_ADDR) plotdaily ./data/$TYPE$WMO.dat $nday $enddate $cdfarg $beginend $anomarg" >> log/log
[ "$lwrite" = true ] && echo "./bin/plotdaily ./data/$TYPE$WMO.dat $nday $enddate $cdfarg $beginend $anomarg<br>"
(./bin/plotdaily ./data/$TYPE$WMO.dat $nday $enddate $cdfarg $beginend $anomarg > $root.txt) 2>&1
c=`egrep -v '^#' $root.txt | grep '[0-9]' | wc -l`
if [ $c = 0 ] ; then
    echo "No valid output, maybe the date $enddate is beyond the end date of the series, or the climatology interval before the beginning of the series?"
else
    lastdate=`egrep -v '^#' $root.txt | grep '[0-9]' | tail -n 1 | cut -b 1-8`
    [ -z "$yr" -o "$arg_enddate" = last ] && yr=`echo "$lastdate" | cut -b 1-4`
    [ -z "$mo" -o "$arg_enddate" = last ] && mo=`echo "$lastdate" | cut -b 5-6`
    [ -z "$dy" -o "$arg_enddate" = last ] && dy=`echo "$lastdate" | cut -b 7-8`
    lastdate=$((lastdate+1))
    firstdate=`fgrep -v '#' $root.txt | grep '[0-9]' | head -n 1 | cut -b 1-8`
    [ "$lwrite" = true ] && echo "firstdate,lastdate = $firstdate,$lastdate<br>"
    if [ "$anom" != zero ]; then
        with="with climatology $computed"
    fi
    echo "<div class=\"bijschrift\">$last$nday ${month}s of $name observations at $station$ending $with"
    echo "(<a href=\"$root.eps\">eps</a>, <a href="ps2pdf.cgi?file=$root.eps">pdf</a>, <a href=\"$root.txt\">raw data</a>)</div>"
    if [ "$NPERYEAR" -ge 360 ]; then
        timefmt="'%Y%m%d'"
    else
        timefmt="'%Y%m'"
    fi
    if [ \( \( "$NEWUNITS" = "mm/day" -o "$NEWUNITS" = "mm/dy" \) \
            -a "${VAR#ev}" = "$VAR" -a "${VAR#nt}" = "$VAR" -a "${VAR#precipitation_def}" = "$VAR" \) \
            -o "$VAR" = "soilw" -o "$VAR" = "dis24" ]; then
        above=3
        below=1
    else
        above=1
        below=3
    fi
    if [ -n "$ylo" -o -n "$yhi" ]; then
        setyrange="set yrange [${ylo}:${yhi}]"
    fi
    if [ -n "$whitehi" ]; then
        threehi="($whitehi)"
    else
        threehi=3
    fi
    if [ -n "$whitelo" ]; then
        threelo="($whitelo)"
    else
        threelo=3
    fi

    wmo_=`echo "$WMO" | tr '_' ' '`
    var_=`echo "$VAR" | tr '_' ' '`
    title="$name $station ($wmo_)"
    [ -n "$period" -a "$anom" != zero ] && title="$title wrt $period"
    plotfile=data/plotdaily$$.gnuplot
    cat > $plotfile << EOF
$gnuplot_init
set size 0.8,0.6
set datafile missing "-999.900"
set zero 1e-40
set xzeroaxis
set term png $gnuplot_png_font_hires
set output "./$root.png"
set xdata time
set timefmt $timefmt
set format x $timefmt
$setyrange
set xrange ["$firstdate":"$lastdate"]
set ylabel "$var_ [$UNITS]"
set title "$title"
plot "./$root.txt" using 1:2:$threehi notitle with filledcurves above lt $above, \
     "./$root.txt" using 1:2:$threelo notitle with filledcurves below lt $below, \
     "./$root.txt" using 1:2 notitle with lines lt -1, \
     "./$root.txt" using 1:3 notitle with lines lt -1

set term postscript epsf color solid
set output "./$root.eps"
replot
quit
EOF
    if [ "$lwrite" = true ]; then
        echo '<pre>'
        cat $plotfile
        echo '</pre>'
    fi
    gnuplot < $plotfile

    pngfile="./$root.png"
    getpngwidth
    echo "<center><img src=\"$pngfile\" alt=\"last $nday ${months}s of $name at $station\" width="$halfwidth" border=0 class=\"realimage\" hspace=0 vspace=0></center>"
fi

if [ "$cdf" = on ]; then
    cdf_checked=checked
else
    cdf_unchecked=checked
fi
if [ "$anom" = zero ]; then
    zero_checked=checked
else
    range_checked=checked
fi

if [ $EMAIL != someone@somewhere ]; then
    cat > $def <<EOF
FORM_nday=$nday;
FORM_yr=$yr;
FORM_mo=$mo;
FORM_dy=$dy;
FORM_cdf=$cdf;
FORM_anom=$anom;
FORM_climyear1=$climyear1;
FORM_climyear2=$climyear2;
FORM_ylo=$FORM_ylo;
FORM_yhi=$FORM_yhi;
EOF
fi

cat <<EOF
<div class="formbody">
<form action="plotdaily.cgi" method="POST">
<input type="hidden" name="EMAIL" value="$EMAIL">
<input type="hidden" name="TYPE" value="$TYPE">
<input type="hidden" name="WMO" value="$WMO">
<input type="hidden" name="STATION" value="$STATION">
<input type="hidden" name="NAME" value="$NAME">
<input type="hidden" name="NPERYEAR" value="$NPERYEAR">
<table style='width:100%' border='0' cellpadding='0' cellspacing='0'>
<tr><td>Replot: 
<td><input type="$number" class=forminput min="1" max="1000" step=1 name="nday" $textsize3 value="$nday">
${month}s with end date
<input type="$number" class=forminput min="1" max="2400" step=1 name="yr" $textsize4 value="$yr">
EOF
if [ ${NPERYEAR:-12} -gt 1 ]; then
    echo "<input type="$number" class=forminput min="1" max="12" step=1 name="mo" $textsize2 value="$mo">"
fi
if [ ${NPERYEAR:-12} -gt 12 ]; then
    echo "<input type="$number" class=forminput min="1" max="31" step=1 name="dy" $textsize2 value="$dy">"
fi
cat <<EOF
<tr><td>Plot:
<td>
<input type=radio class=formradio name="cdf" value="off" $cdf_unchecked>observations
<input type=radio class=formradio name="cdf" value="on" $cdf_checked>cumulatives
<tr><td>Compare with:
<td>
<input type=radio class=formradio name="anom" value="range" $range_checked>climatology
<input type="$number" class=forminput min="1" max="2400" step=1 name="climyear1" $textsize4 value="$climyear1">
-
<input type="$number" class=forminput min="1" max="2400" step=1 name="climyear2" $textsize4 value="$climyear2">
<br>
<input type=radio class=formradio name="anom" value="zero" $zero_checked>zero, data are already anomalies
<tr><td>
White centre<td>leave white values between
<input type="$number" class=forminput name="whitelo" $textsize4 value="$whitelo">
and
<input type="$number" class=forminput name="whitehi" $textsize4 value="$whitehi">
<tr><td>
Y axis<td>
<input type="$number" class=forminput name="ylo" $textsize4 value="$ylo">
-
<input type="$number" class=forminput name="yhi" $textsize4 value="$yhi">
<tr><td>
<input type="submit" class="formbutton" value="plot">
</table>
</form>
</div>
EOF

. ./myvinkfoot.cgi
