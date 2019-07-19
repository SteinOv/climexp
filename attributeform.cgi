#!/bin/bash
. ./httpheaders_nocache.cgi
. ./init.cgi
. ./getargs.cgi

if [ -n "$FORM_field" ]; then
    . ./queryfield.cgi
    if [ -n "$FORM_TYPE" ]; then
        TYPE=$FORM_TYPE
    else
        TYPE=field
    fi
    station="$climfield"
    NAME="$kindname"
else
    TYPE="$FORM_TYPE"
    WMO="$FORM_WMO"
    listname=$WMO
    STATION="$FORM_STATION"
    station=` echo "$STATION" | tr '_%' ' +'`
    NAME="$FORM_NAME"
    prog=$NAME
    NPERYEAR="$FORM_NPERYEAR"
fi
if [ "$EMAIL" = oldenborgh@knmi.nl ]; then
    lwrite=false
fi

. ./nosearchengine.cgi

if [ $TYPE = gridpoints ]; then
  . ./myvinkhead.cgi "Trends in return times of extremes" "gridpoints of $kindname $climfield" "noindex,nofollow"
elif [ $TYPE = field ]; then
  . ./myvinkhead.cgi "Trends in return times of extremes" "$kindname $climfield" "noindex,nofollow"
elif [ $TYPE = set ]; then
  . ./myvinkhead.cgi "Trends in return times of extremes" "$station stations" "noindex,nofollow"
else
  . ./myvinkhead.cgi "Trends in return times of extremes" "$station $NAME ($WMO)" "noindex,nofollow"
fi

cat <<EOF
<a href="javascript:pop_page('help/empirical_event_attribution.shtml',568,480)"><img align="right" src="images/info-i.gif" alt="help" border="0"></a>

Compute the return times of an extreme in the distribution of the other values and in the 
climate of another year, assuming that the PDF shifts or scales with the covariate.

A few examples are given in the <a href="javascript:pop_page('help/empirical_event_attribution.shtml',568,480)">in the help page</a>.
<p>
EOF

DIR=`pwd`
c1=`echo "$WMO $file" | fgrep -c '%%'`
c2=`echo "$WMO $file" | fgrep -c '++'`
if [ $c1 -gt 0 -o $c2 -gt 0 ]; then
  ENSEMBLE=true
fi

if [ "$EMAIL" != somene@somewhere ]; then
  if [ -n "$DIR" ]; then
    def=$DIR/prefs/$EMAIL.histogramoptions
  else
    def=prefs/$EMAIL.histogramoptions
  fi
  if [ -s $def ]; then
    eval `egrep '^FORM_[a-z0-9]*=[a-zA-Z]*[-+0-9.%]*;$' $def`
  fi
  FORM_dgt=${FORM_dgt%%%}
  FORM_dgt=${FORM_dgt%%%}
fi

case ${FORM_fit:-none} in
poisson) fit_poisson="checked";;
gauss)   fit_gauss="checked";;
gamma)   fit_gamma="checked";;
gumbel)  fit_gumbel="checked";;
gev)     fit_gev="checked";;
gpd)     fit_gpd="checked";;
*)       fit_none="checked";;
esac

case $FORM_assume in
scale) assume_scale=checked;;
both)  assume_both=checked;;
*)     assume_shift=checked;;
esac

if [ -n "$FORM_changesign" ]; then
  changesign_checked="checked"
fi

if [ -n "$FORM_normsd" ]; then
  normsd_checked="checked"
fi

case ${FORM_restrain:-0} in
0.5) select05=selected;;
0.4) select04=selected;;
0.3) select03=selected;;
0.2) select02=selected;;
*)   select00=selected;;
esac

case ${FORM_var:-atr1} in
    atr2) atr2=checked;;
    atra) atra=checked;;
    *) atr1=checked;;
esac

cat <<EOF
<form action="attribute.cgi" method="POST">
<input type="hidden" name="EMAIL" value="$EMAIL">
<input type="hidden" name="field" value="$FORM_field">
<input type="hidden" name="NAME" value="$NAME">
<input type="hidden" name="TYPE" value="$TYPE">
<input type="hidden" name="WMO" value="$WMO">
<input type="hidden" name="STATION" value="$STATION">
<input type="hidden" name="NPERYEAR" value="$NPERYEAR">
<input type="hidden" name="extraargs" value="$FORM_extraargs">
<input type="hidden" name="nbin" value="$FORM_nbin">
<input type="hidden" name="climate" value="$timescale $extraname$climate">
<input type="hidden" name="prog" value="$prog">
<input type="hidden" name="listname" value="$listname">
<input type="hidden" name="type" value="aatribute">
<div class="formheader">Covariate series</div>
EOF

# get units
# this still fails for sets of stations, but these do not need bias corrections...
if [ -n "$file" ]; then
    files=$file
else
    files=./data/$TYPE$WMO.dat
fi
if [ "$ENSEMBLE" = true ]; then
  firstfile=`echo $files | sed -e 's/%%%/000/' -e 's/+++/000/' -e 's/%%/00/' -e 's/++/00/'`
  if [ ! -s $firstfile ]; then
    firstfile=`echo $filest | sed -e 's/%%%/001/' -e 's/+++/001/' -e 's/%%/01/' -e 's/++/01/'`
  fi
else
  firstfile=$files
fi
if [ "$lwrite" = true ]; then
    echo '<pre>'
    echo "firstfile=$firstfile"
    ./bin/getunits $firstfile
    echo '</pre>'
fi
if [ -s $firstfile ]; then
    eval `./bin/getunits $firstfile`
fi

# we can handle time series at all time scales...
if [ $NPERYEAR -ge 360 ]; then
    nperyears="1 12 $NPERYEAR"
elif [ $NPERYEAR -ge 12 ]; then
    nperyears="1 12"
elif [ $NPERYEAR -ge 4 ]; then
    nperyears="1 4"
else
    nperyears="1"
fi

if [ "$EMAIL" != "someone@somewhere" -a -f ./prefs/$EMAIL.series ]; then
    series=`cat ./prefs/$EMAIL.series | head -1`
fi
save_nperyear=$NPERYEAR
for NPERYEAR in $nperyears
do
    if [ $NPERYEAR = 1 ]; then
        show_none=true
    else
        show_none=false
    fi
    . ./selecttimeseries.cgi | sed \
    -e 's;="'$series'";="'$series'" checked;' \
    -e 's/checkbox\" class=\"formcheck\" name/radio\" class=\"formradio\" name=\"timeseries\" value/' \
    -e 's/value=\"myindex[0-9]*\"//'
done
NPERYEAR=$save_nperyear

cat <<EOF
<div class="formheader">Plot</div>
<div class="formbody">
<table width="100%" border='0' cellpadding='0' cellspacing='0'>
EOF

justonemonth=true
ONLYONE=true
save_name=$NAME
NAME=series
###DECOR=true
INCLUDE_CUBE=true
INCLUDE_SQUARE=true
INCLUDE_TWOTHIRD=true
NORANGE=true
NOFILTERS=true
. ./commonoptions.cgi
NAME=$save_name

cat <<EOF
<tr><td>Demand at least<td><input type="$number" step=any name="minfac" value="$FORM_minfac" $textsize2>% valid points
<tr><td>Change sign:
<td><input type="checkbox" class="formcheck" name="changesign" $changesign_checked>study the low extremes<td><a href="javascript:pop_page('help/changesign.shtml',284,450)"><img align="right" src="images/info-i.gif" alt="help" border="0"></a>

<tr><td valign=top>Use:<td>
<input type="radio" class="formradio" name="fit" value="gauss" $fit_gauss>Average and fit normal distribution<br>
<input type="radio" class="formradio" name="fit" value="gumbel" $fit_gumbel>Block maxima and fit Gumbel distribution<br>
<input type="radio" class="formradio" name="fit" value="gev" $fit_gev>Block maxima and fit GEV<br>
<input type="radio" class="formradio" name="fit" value="gpd" $fit_gpd>Peak over threshold
<input type="$number" class="forminput" name="dgt" value="${FORM_dgt:-80}" $textsize6>% and fit GPD<br>
<select class="forminput" name="restrain">
<option value="0" $select00>do not constrain shape
<option value="0.5" $select05>constrain shape to &plusmn;0.5
<option value="0.4" $select04>constrain shape to &plusmn;0.4
<option value="0.3" $select03>constrain shape to &plusmn;0.3
<option value="0.2" $select02>constrain shape to &plusmn;0.2
</select> of GEV and GPD
<tr><td>Assume:<td>the PDF <input type="radio" class="formradio" name="assume" value="shift" $assume_shift>shifts, <input type="radio" class="formradio" name="assume" value="scale" $assume_scale>scales or <input type="radio" class="formradio" name="assume" value="both" $assume_both>both with the covariate<td><a href="javascript:pop_page('help/assume.shtml',284,450)"><img align="right" src="images/info-i.gif" alt="help" border="0"></a>
EOF
if [ -n "$ENSEMBLE" -o $TYPE = set -o $TYPE = gridpoints ]; then
    cat <<EOF
<tr><td>Normalise:
<td><input type="checkbox" class="formcheck" name="normsd" $normsd_checked>all series to the same mean<td><a href="javascript:pop_page('help/normaliseseries.shtml',284,450)"><img align="right" src="images/info-i.gif" alt="help" border="0"></a>
EOF
fi
cat <<EOF
<tr><td>Return time:<td>year <input type="$number" min=1 max=2500 step=1 class="forminput" name="year" $textsize4 value="$FORM_year"> (with value <input class="forminput" name="xyear" $textsize6 value="$FORM_xyear">)
<tr><td>Compare:<td>return time if it had occurred in year <input type="$number" min=1 max=2500 step=1 class="forminput" name="begin2" $textsize4 value="$FORM_begin2">
<tr><td>Optionally plot:<td>return time if it had occurred in year <input type="$number" min=1 max=2500 step=1 class="forminput" name="end3" $textsize4 value="$FORM_end3">
<tr><td>Bias correction:<td>add
<input type="$number" class="forminput" name="biasmul" $textsize4 value="$FORM_biasmul">% and/or 
<input type="$number" class="forminput" name="biasadd" $textsize4 value="$FORM_biasadd"> $UNITS.
EOF

if [ "$TYPE" != setmap -a "$TYPE" != field ]; then
    cat <<EOF
<tr><td>Plot range:<td>X <input type="$number" step=any class="forminput" name="xlo" $textsize4 value="$FORM_xlo">:<input type="$number" step=any class="forminput" name="xhi" $textsize4 value="$FORM_xhi">,
Y <input type="$number" step=any class="forminput" name="ylo" $textsize4 value="$FORM_ylo">:<input type="$number" step=any class="forminput" name="yhi" $textsize4 value="$FORM_yhi">
<input type="hidden" name="var" value="$FORM_var">
EOF
elif [ "$TYPE" = setmap ]; then
    cat <<EOF
<tr><td>Plot variable:<td>
<input type="radio" class="formradio" name="var" value="atr1" $atr1>Return time at the time of the event,
<tr><td>&nbsp;<td>
<input type="radio" class="formradio" name="var" value="atr2" $atr2>Return time if it had occurred at the other time,
<tr><td>&nbsp;<td>
<input type="radio" class="formradio" name="var" value="atra" $atra>Log10(ratio) of the two.
<input type="hidden" name="xlo" value="$FORM_xlo">
<input type="hidden" name="xhi" value="$FORM_xhi">
<input type="hidden" name="ylo" value="$FORM_ylo">
<input type="hidden" name="yhi" value="$FORM_yhi">
EOF
fi    
cat <<EOF
<tr><td>Confidence interval:<td><input type="$number" step=any class="forminput" name="ci" $textsize4 value="${FORM_ci:-95}">%
EOF
if [ $TYPE = field ]; then
    . ./plotoptions.cgi
fi
cat <<EOF
<tr><td colspan="2"><input type="submit" class="formbutton" value="Compute">
</table>
</div>
</form>
EOF

FORM_listname=""
listname="" # otherwise the menu goes the wrong way
. ./myvinkfoot.cgi
