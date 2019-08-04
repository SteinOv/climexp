#!/bin/bash
echo 'Content-Type: text/html'
echo
echo

. ./init.cgi
. ./getargs.cgi
# check if a search engine, if so set user to anonymous
. ./searchengine.cgi
. ./checkemail.cgi

if [ $EMAIL = someone@somewhere ]; then
    . ./myvinkhead.cgi "Synthesis" "Error"
    echo "Please <a href=registerform.cgi>login or register</a> before using this routine."
    . ./myvinkheadfoot.cgi
fi
if [ $EMAIL = ec8907341dfc63c526d08e36d06b7ed8 ]; then
    lwrite=true # false
fi

[ ! -d synthesis/$EMAIL ] && mkdir synthesis/$EMAIL
prefs=prefs/$EMAIL.synthesis

if [ -n "$FORM_data" ]; then
    tmpfile=synthesis/$EMAIL/synthesis$$.txt
    echo "$FORM_data" | tr '\r' '\n' > $tmpfile
    c=`head -1 $tmpfile | fgrep -c '#'`
    if [ $c = 0 ]; then
        . ./myvinkhead.cgi "Synthesis" "Error"
        echo 'First line of the upload field should start with a # and contain the title.'
        . ./myvinkfoot.cgi
        exit
    fi
    title=`fgrep '#' $tmpfile | head -1 | sed -e 's/ *# *//'`
    file=synthesis/$EMAIL/synthesis_`date -u "+%Y%m%d_%H%M%S"`_$EMAIL.txt
    oldfile=`ls -t synthesis/$EMAIL/synthesis_*.txt | head -1`
    if [ -f "$oldfile" ]; then
        cmp -s $oldfile $tmpfile
        if [ $? = 0 ]; then
            file=$oldfile
            rm $tmpfile
        else
            mv $tmpfile $file
        fi
    else
        mv $tmpfile $file
    fi
    cat > $file.prefs << EOF
FORM_weighted=$FORM_weighted;
FORM_log=$FORM_log;
FORM_perc=$FORM_perc;
FORM_ref=$FORM_ref;
FORM_flipsign=$FORM_flipsign;
EOF
    useprefs=false
elif [ -n "$FORM_file" ]; then
    file=$FORM_file
    title=`fgrep '#' $file | head -1 | sed -e 's/ *# *//'`
    [ -f $file.prefs ] && prefs=$file.prefs
    useprefs=true
else
    file=
    title="New project"
    useprefs=true
    nocomputation=true
fi
if [ $useprefs = true ]; then
    if [ -f $prefs ]; then
        eval `egrep '^FORM_[a-z0-9]*=[a-zA-Z]*[-+0-9.%]*;$' $prefs`
    fi
fi

case "$FORM_weighted" in
    noave) noave_checked="checked";;
    weighted) weighted_checked="checked";;
    *) unweighted_checked="checked";;
esac
if [ -n "$FORM_log" ]; then
    log_checked=checked
fi
if [ -n "$FORM_perc" ]; then
    perc_checked=checked
fi
case "$FORM_ref" in
    CO2) CO2_checked="checked";;
    time) time_checked="checked";;
    none) none_checked="checked";;
    *) GMST_checked="checked";;
esac
if [ -n "$FORM_flipsign" ]; then
    flipsign_checked=checked
fi

. ./myvinkhead.cgi "Synthesis" "$title"

cat <<EOF
<font color=Red>This is the second test version, incompatible with the first. Use at your own risk. 
Please check results and report errors back.</font>

<div class='formheader'>Synthesis input</div>
<div class='formbody'>
<table style='width:100%' border='0' cellpadding='0' cellspacing='0'>
<form action="synthesis.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<tr><td colspan="2">
&nbsp;<textarea class="forminput" name="data" class="forminput" rows="8" cols="60">
EOF
if [ -z "$file" ]; then
    cat <<EOF
Overwrite with your own data in the format:
# Title of plot
yr0 yr1 bestfit lowbound highbound CI Name
yr0 yr1 bestfit lowbound highbound CI Name
..

A blank line should seperate observatiuon and models
EOF
else
    cat $file
fi
cat <<EOF
</textarea>
<tr><td>Weighting:<td>
<input type="radio" class="formradio" name="weighted" value="weighted" $weighted_checked>weighted.
<input type="radio" class="formradio" name="weighted" value="unweighted" $unweighted_checked>unweighted, or
<input type="radio" class="formradio" name="weighted" value="noave" $noave_checked>no average.
<tr><td>Logarithm:<td>
<input type=checkbox class=formcheck name=log $log_checked>data should be evaluated and plotted on a logarithmic axis (like PRs).
<tr><td>Percentiles:<td>
<input type=checkbox class=formcheck name=perc $perc_checked>values are given as percentiles.
<tr><td>Reference:<td>use 
<input type="radio" class="formradio" name="ref" value="GMST" $GMST_checked>GMST,
<input type="radio" class="formradio" name="ref" value="CO2" $CO2_checked>CO2,
<input type="radio" class="formradio" name="ref" value="time" $time_checked>time, or
<input type="radio" class="formradio" name="ref" value="none" $none_checked>nothing
to transform all begin dates to the earliest one.
<tr><td>Reverse:<td>
<input type=checkbox class=formcheck name=flipsign $flipsign_checked>compute deviations from the last date, not the first.
<tr><td>Plot range:<td>
<input type="$number" class="forminput" name="xmin" $textsize4 value="${FORM_xmin}"> - 
<input type="$number" class="forminput" name="xmax" $textsize4 value="${FORM_xmax}">
<tr><td colspan=2>
<input type="submit" class="formbutton" value="Make plot">
</table>
</div>
EOF

# real work

if [ -z "$nocomputation" ]; then

    args="$file $FORM_ref $FORM_weighted"
    [ -n "$FORM_log" ] && args="$args log"
    [ -n "$FORM_perc" ] && args="$args perc"
    [ -n "$FORM_flipsign" ] && args="$args flipsign"

    root=data/synthesis_`date -u "+%Y%m%d_%H%M%S"`_$EMAIL
    ofile=$root.txt

    [ "$lwrite" = true ] && echo "./bin/synthesis $args<br>"
    echo `date` "$EMAIL ($REMOTE_ADDR) synthesis $args" >> log/log
    ./bin/synthesis $args > $ofile
    if [ ! -s $ofile ]; then
        echo "Something went wrong in synthesis $args"
        . ./myvinkfoot.cgi
        exit
    fi
    version=`gnuplot --version | cut -b 9`
    if [ $version != "4" ]; then
        sed -e 's/@/\\\\@/g' ${root}.txt > /tmp/synthesis$$.txt
    else
        sed -e 's/@/\\@/g' ${root}.txt > /tmp/synthesis$$.txt
    fi
    mv /tmp/synthesis$$.txt ${root}.txt

    if [ -n "$FORM_log" ]; then
        setlogscaley="set logscale y"
    fi
    if [ -n "$FORM_xmin" ]; then
        xmin=$FORM_xmin
    else
        xmin="(STATS_min/10)"
    fi
    if [ -n "$FORM_xmax" ]; then
        xmax=$FORM_xmax
    else
        xmax="(SSTATS_max*1.1)"
    fi
    if [  -n "$FORM_log" ]; then
        line=1
    else
        line=0
    fi

    cat > ${root}.gnuplot <<EOF
#!/usr/bin/gnuplot
# generated by $0, do not edit
set term postscript eps enhanced color solid font "Helvetica"
set output "${root}.eps"
set ytics rotate 
set noxtics
set border 10 
set ylabel "$region $season"
stats '${root}.txt' using 7
set size ((STATS_records+2.)/20),1
SSTATS_max=STATS_max
stats '${root}.txt' using 6
set xrange[-0.5:(STATS_records-0.5)]
set yrange [$xmin:$xmax]
$setlogscaley
set linetype 1 lc rgb "#5252f0"
set linetype 2 lc rgb "blue"
set linetype 3 lc rgb "#f05252"
set linetype 4 lc rgb "red"
set linetype 5 lc rgb "#c000ff"
plot ${line} notitle w line lt 0, \
    '${root}.txt' using (\$0):(STATS_min):9 notitle with labels rotate right, \
    '${root}.txt' using (\$0):3:(\$0-0.22):(\$0+0.22):6:7:8 notitle with boxxyerrorbars fs solid 0 border -1 lw 2, \
    '${root}.txt' using (\$0):3:(\$0-0.2):(\$0+0.2):4:5:8 notitle with boxxyerrorbars fs solid 0.70 lc variable, \
    '${root}.txt' using (\$0):3:(0.2) notitle with xerrorbars lt -1 lw 5
quit
EOF
    gnuplot < ${root}.gnuplot >& /dev/null
    epstopdf ${root}.eps
    gs -q -r450 -dTextAlphaBits=4 -dNOPAUSE -sDEVICE=ppmraw -sOutputFile=- $root.eps -c quit | pnmcrop | pnmrotate -90 | pnmtopng > $root.png

    echo "<div class=bijschrift>Synthesis of "
    fgrep '#' $root.txt | sed -e 's/ *#//' -e 's/ *$/,/'
    echo 'Coloured bars denote natural variability, boxes also take representativity / model errors into account.'
    if [ $FORM_weighted = weighted ]; then
        echo "In the synthesis, the purple bar denotes the weighted average of observations and models, the box denotes the unweighted average."
    fi
    echo "(<a href=\"$root.eps\">eps</a>, <a href=\"$root.pdf\">pdf</a>, <a href=\"$root.gnuplot\">plot script</a>, <a href=\"$root.txt\">raw data</a>)</div>"
    pngfile="./$root.png"
    getpngwidth
    echo "<center><img src=\"$pngfile\" alt=\"synthesis $title\" width=\"$halfwidth\" border=0 class=\"realimage\" hspace=0 vspace=0></center>"

    cat > $prefs <<EOF
FORM_weighted=$FORM_weighted;
FORM_log=$FORM_log;
FORM_perc=$FORM_perc;
FORM_flipsign=$FORM_flipsign;
FORM_ref=$FORM_ref;
FORM_xmin=$FORM_xmin;
FORM_xmax=$FORM_xmax;
EOF
fi # nocomputation

echo '<p><table class="realtable" width="100%" border=0 cellspacing=0 cellpadding=0>'
echo '<tr><th>Old synthesis files'
for f in `ls -t ./synthesis/$EMAIL/synthesis_*.txt`; do
    if [ -s $f ]; then
        title=`fgrep '#' $f | head -1 | sed -e 's/ *# *//'`
        echo "<tr><td><a href=synthesis.cgi?id=$EMAIL&file=$f>$title</a>"
    fi
done
echo '</table>'

. ./myvinkfoot.cgi
