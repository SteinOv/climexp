#!/bin/bash
# show some metadata about the file from the netcdf global attributes
echo "Content-Type: text/html"
echo

. ./init.cgi
. ./getargs.cgi

if [ -n "$FORM_field" ]; then
    . ./queryfield.cgi
    . ./get_url.cgi
else
    TYPE=$FORM_TYPE
    WMO=$FORM_WMO
    file=data/$TYPE$WMO.dat
    station=`echo "$FORM_station" | tr '_' ' '`
fi

. ./myvinkhead.cgi "Metadata" "$station$kindname $climfield"

cat <<EOF
<table class="realtable" width="100%" cellspacing=0 cellpadding=0>
<tr><th colspan=2>References
EOF
file0=`echo "$file" | sed -e 's/%%%/000/' -e 's/%%/00/' -e 's/+++/000/' -e 's/++/01/'`
[ "$splitfield" = true ] && file0=`ls $file0 | head -n 1`
if [ ! -s $file0 ]; then
    file0=`echo "$file" | sed -e 's/%%%/001/' -e 's/%%/01/' -e 's/+++/001/' -e 's/++/01/'`
    if [ ! -s $file0 ]; then
        echo "Error: cannot find file $file"
        echo '</table>'
        . ./myvinkfoot.cgi
        exit
    fi
fi
if [ -z "$url" -a ${file0%.dat} != $file0 ]; then
    # in ascii time series files the URL is often in the comment on the top
    c=`fgrep -c href $file0`
    if [ $c != 0 ]; then
        url=`head -n 200 $file0 | fgrep href | sed -e 's/^.*href=//' -e 's/>.*$//' -e 's/["]//g' -e 's/ target=.*//'`
    fi
fi
if [ -n "$url" ]; then
    echo "<tr><td>official web page<td>"
    for oneurl in $url; do
        echo "<a href=$oneurl>$oneurl</a>"
    done
fi
if [ -n "$FORM_field" ]; then
    echo "<tr><td>Climate Explorer URL<td><a href=http://climexp.knmi.nl/select.cgi?$FORM_field>climexp.knmi.nl/select.cgi?$FORM_field<a/>"
else
    f=${file0%.dat}
    ce_url=`cat selectindex.cgi selectdailyindex.cgi selectannualindex.cgi \
        | tr ' ' '\n' | fgrep "/${WMO}&" \
        | sed -e 's/href=//' -e 's/>.*$//' -e 's/["]//g' -e 's/&id=$EMAIL//' -e 's/&TYPE=i//'`
    if [ -n "$ce_url" ]; then
        file=`echo "$ce_url" | sed -e 's/^.*WMO=//' -e 's/\&.*$//'`.dat
        file0=$file
        if [ ! -s $file0 ]; then
            file0=${file0%.dat}.nc
        fi
    fi
    if [ -z "$ce_url" ]; then
        prog=""
        case $TYPE in
            # GHCN-M
            pa) prog=getprcpall;;
            ta) prog=gettempall;;
            ma) prog=getminall;;
            xa) prog=getmaxall;;
            p) prog=getprcp;;
            t) prog=gettemp;;
            m) prog=getmin;;
            x) prog=getmax;;
            s) prog=getslp;;
            # GHCN-D
            xgdcn) prog=gdcntmax;;
            ngdcn) prog=gdcntmin;;
            vgdxn) prog=gdcntave;;
            pgdcn) prog=gdcnprcp;;
            pgdcngts) prog=gdcnprcpall;;
            fgdcn) prog=gdcnsnow;;
            dgdcn) prog=gdcnsnwd;;
            # KNMI data
            tg|tn|tx|t1|tw|dr|rr|rh|preciphom19??|rx|ev|pg|pn|px|dd|fh|fn|fx|dx|dy|td|ug|un|ux|ng|sq|sp|qq|vn|vx|sd|up|upx) 
                prog=getdutch$TYPE
                WMO=${WMO#$TYPE}
                ;;
            # ECA Data
            ceca) prog=ecaclou;;
            peca) prog=ecaprcp;;
            seca) prog=ecapres;;
            deca) prog=ecasnow;;
            teca) prog=ecatemp;;
            xeca) prog=ecatmax;;
            neca) prog=ecatmin;;
            bceca) prog=becaclou;;
            bpeca) prog=becaprcp;;
            bseca) prog=becapres;;
            bdeca) prog=becasnow;;
            bteca) prog=becatemp;;
            bxeca) prog=becatmax;;
            bneca) prog=becatmin;;
        esac
    fi
    if [ -n "$prog" ]; then
        ce_url="$prog.cgi?WMO=$WMO&STATION=$FORM_station"
    fi
    # I should check a few other obvious places...
    if [ -n "$ce_url" ]; then
        echo "<tr><td>Climate Explorer URL<td><a href=http://climexp.knmi.nl/$ce_url>climexp.knmi.nl/$ce_url<a/>"
    fi
fi
if [ "$file0" = "$file" ]; then
    echo "<tr><td>Climate Explorer filename<td>$file0"
else
    echo "<tr><td>Climate Explorer filename<td>$file"
    echo "<tr><td>first ensemble member<td>$file0"
fi
if [ ${file0#data} != $file0 ]; then
    echo "(temporary, will be deleted 3 days after last use)"
fi
eval `./bin/getunits $file0`
echo "<tr><th colspan=2>Variable"
echo "<tr><td>name<td>$VAR"
echo "<tr><td>units<td>$UNITS"
[ -n "$LVAR" ] && echo "<tr><td>long_name<td>$LVAR"
[ -n "$SVAR" ] && echo "<tr><td>standard_name<td>$SVAR"

if [ ${file0%.dat} != $file0 ]; then
    echo "<tr><th colspan=2>Ascii global metadata"
    if [ "$file0" != "$file" ]; then
        echo "of first ensemble member"
    fi
    echo '<tr><td>description<td>'
    head -n 200 $file0 | egrep '^#' | egrep -v -i '( :: )|(jan *feb)' | grep -v '^ *$' | sed -e 's/^#//' -e 's/^.#//' -e 's/$/,/' -e 's/^ *, *//' | tr '_' ' ' | sed -e 's/antieke wrn/antieke_wrn/'
    head -n 200 $file0 | fgrep ' :: ' | sed \
        -e 's/^# */\<tr\>\<td\>/' \
        -e 's/:: */\<td\>/' \
        -e 's/\n,/\<br\>/g' \
        -e 's/\\n,/\<br\>/g' \
        -e 's/\n/\<br\>/g' \
        -e 's/\\n/\<br\>/g' \
        -e 's@http://\([^ ")]*\)@<a href=http://\1>\1</a>@' \
        -e 's@https://\([^ ")]*\)@<a href=https://\1>\1</a>@' \
        -e 's@ftp://\([^ ")]*\)@<a href=ftp://\1>\1</a>@' \
        -e 's@doi:\([^ ]*\)@<a href=https://doi.org/\1>doi:\1</a>@g'
else
    echo "<tr><th colspan=2>Netcdf global metadata"
    if [ "$file0" != "$file" ]; then
        echo "of first ensemble member"
    fi
    # sed only accepts lines up to about 15000 chars in Fedora 28
    ncdump -h $file0 | cut -b 1-10000 | sed \
        -e '/{/,/global attributes/d' \
        -e 's/^[ \t]*:/\<tr\>\<td\>/' \
        -e 's/ = */\<td\>/' \
        -e 's/ ;//' \
        -e 's/"//g' \
        -e 's/\n,/\<br\>/g' \
        -e 's/\\n,/\<br\>/g' \
        -e 's/\n/\<br\>/g' \
        -e 's/\\n/\<br\>/g' \
        -e 's/^}//' \
        -e 's@http://\([^ ")]*\)@<a href=http://\1>\1</a>@' \
        -e 's@https://\([^ ")]*\)@<a href=https://\1>\1</a>@' \
        -e 's@ftp://\([^ ")]*\)@<a href=ftp://\1>\1</a>@' \
        -e 's@doi:\([^ ]*\)@<a href=https://doi.org/\1>doi:\1</a>@'
fi
echo "</table>"

. ./myvinkfoot.cgi
