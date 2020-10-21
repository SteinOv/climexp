#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo 'Content-Type: text/html'
echo
echo
# in order not to break bookmarks to this entry point allow QUERY_STRING (with some checking)
# do not allow / in email address
. ./searchengine.cgi
. ./checkemail.cgi
. ./myvinkhead.cgi "Starting point" "" "index,follow"

if [ "$EMAIL" != someone@somewhere ]; then
    FORM_username=`fgrep "$EMAIL" ./log/newlist | cut -f 2 -d ' ' | tail -1 | sed -e 's/+/ /g'`
    FORM_institute=`fgrep "$EMAIL" ./log/newlist | cut -f 3 -d ' ' | tail -1 | sed -e 's/+/ /g'`
    echo "<div class=\"alineakop\">Welcome, $FORM_username from $FORM_institute</div>"
    if [ -s data/randomimage.png ]; then
        randomimage=data/randomimage.png
    else
        tmpfile=/tmp/start$$.txt
        list=`ls -t data/ | fgrep .png | egrep '(^[dghR])|(.*corr.*)' | egrep -v 'kml|tmp' `
        for file in $list; do
            if [ -z "$randomimage" -a -s data/$file ]; then
                randomimage=data/$file
            fi
        done
    fi
    bijschrift=""
else
    echo "<div class=\"alineakop\">Welcome, anonymous user</div>"
    number=`date +%M | cut -b 2`
    case $number in
        1|2) file=iera5_t2m_gl_yr0.png
            bijschrift="Global mean 2m temperature anomalies wrt 1981-2010 [&deg;C] with 10-yr running mean";source="ERA5";;
        3|4) file=igiss_al_gl_m_yr0.png
            bijschrift="Global mean SST/T2m anomalies wrt 1981-2010 [&deg;C] with 10-yr running mean";source="GISTEMP";;
        5|6|7]) file=prcp_gpcc_;ext="_frac";range1="47-49";range2="50-53"
            bijschrift="Relative precipitation anomalies wrt 1981-2010 [fraction] in";source="GPCC";;
        *) file=t2m_ecmwf_w_;ext="";range1="49-51";range2="52-55"
            bijschrift="2m temperature anomalies wrt 1981-2010 [&deg;C] in";source="ERA5";;
    esac
    if [ -n "$range1" ]; then
        randomimage=`ls -t monthly_overview_world_weather/202?/$file[a-z]??20??$ext.png | head -1`
        mon=`echo $randomimage | cut -b $range1`
        year=`echo $randomimage | cut -b $range2`
    else
        randomimage=monthly_overview_world_weather/$file
    fi
    case $mon in
        jan) month=January;;
        feb) month=February;;
        mar) month=March;;
        apr) month=April;;
        may) month=May;;
        jun) month=June;;
        jul) month=July;;
        aug) month=August;;
        sep) month=September;;
        oct) month=October;;
        nov) month=November;;
        dec) month=December;;
        *) month=$mon;;
    esac
    bijschrift="$bijschrift $month $year (source: $source). More under \"World weather\""

    cat <<EOF
<p>The KNMI Climate Explorer is a tool to investigate the climate.  Start by selecting a class of climate data from the right-hand menu. After you have selected the time series or fields of interest, you will be able to investigate it, correlate it to other data, and generate derived data from it.
EOF
fi

if [ "$EMAIL" = someone@somewhere ]; then
    echo "<p>Some restrictions are in force: the site does not remember how you filled out the forms, you cannot define your own indices, nor upload data into the Climate Explorer or handle large datasets. If you want to use these features please <a href=\"registerform.cgi\">log in or register</a>."
fi

. ./check_ie.cgi

if [ "$EMAIL" != someone@somewhere ]; then
    touch ./prefs/$EMAIL.news
fi

pngfile=$randomimage
getpngwidth
cat <<EOF
<div class="bijschrift">$bijschrift</div>
<center>
<img src="$randomimage" alt="random image" border=0 class="realimage" hspace=0 vspace=0 width=$halfwidth>
</center>
EOF

echo '<table class="realtable" width="100%" border=0 cellpadding=0 cellspacing=0>'
echo '<tr><th colspan="2">News</th></tr>'
head -6 news.html | sed -e "s/FORM_EMAIL/$EMAIL/"
echo "<tr><td><a href=\"news.cgi?id=$EMAIL&all=all\">more...</a></td><td>&nbsp;</td></tr></table>"

. ./myvinkfoot.cgi