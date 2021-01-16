#!/bin/bash
. ./httpheaders_nocache.cgi
. ./init.cgi

DIR=`pwd`
. ./getargs.cgi
# check email address
. ./checkemail.cgi
# no robots
. ./nosearchengine.cgi

echo `date` "$EMAIL ($REMOTE_ADDR) $FORM_field" >> log/log

# start real work
. ./queryfield.cgi
. ./myvinkhead.cgi "Plot field" "$kindname $climfield" "noindex,nofollow"

eval `bin/getunits.sh $file`

if [ $EMAIL != someone@somewhere ]; then
  def=prefs/$EMAIL.plotfield.$NPERYEAR
  if [ -f $def ]; then
    eval `egrep '^FORM_[a-z0-9]*=[a-zA-Z]*[-+0-9.]*;$' $def`
  fi
fi

case ${FORM_plotsum:-1} in
2) sum_2_selected=selected;;
3) sum_3_selected=selected;;
4) sum_4_selected=selected;;
5) sum_5_selected=selected;;
6) sum_6_selected=selected;;
7) sum_7_selected=selected;;
8) sum_8_selected=selected;;
9) sum_9_selected=selected;;
10) sum_10_selected=selected;;
11) sum_11_selected=selected;;
12) sum_12_selected=selected;;
13) sum_13_selected=selected;;
14) sum_14_selected=selected;;
15) sum_15_selected=selected;;
18) sum_18_selected=selected;;
19) sum_19_selected=selected;;
24) sum_24_selected=selected;;
30) sum_30_selected=selected;;
48) sum_48_selected=selected;;
60) sum_60_selected=selected;;
75) sum_75_selected=selected;;
90) sum_90_selected=selected;;
105) sum_105_selected=selected;;
120) sum_120_selected=selected;;
180) sum_180_selected=selected;;
240) sum_240_selected=selected;;
300) sum_300_selected=selected;;
360) sum_360_selected=selected;;
480) sum_480_selected=selected;;
600) sum_600_selected=selected;;
1200) sum_1200_selected=selected;;
*) sum_1_selected=selected;;
esac  

if [ -n "$FORM_plotanomaly" ]; then
  plotanomaly_checked=checked
fi

case ${FORM_plotanomalykind:-absolute} in
  relative) relative_selected=selected;;
  logrelative) logrelative_selected=selected;;
  *) absolute_selected=selected;;
esac

if [ -n "$FORM_year" ]; then
  y2=$FORM_year
  m2=$FORM_month
  case $m2 in
    1) mon2=Jan;;
    2) mon2=Feb;;
    3) mon2=Mar;;
    4) mon2=Apr;;
    5) mon2=May;;
    6) mon2=Jun;;
    7) mon2=Jul;;
    8) mon2=Aug;;
    9) mon2=Sep;;
    10) mon2=Oct;;
    11) mon2=Nov;;
    12) mon2=Dec;;
  esac
else
  dates=`./bin/describefield.sh $file | fgrep 'data available'`
  if [ -n "$dates" ]; then
    case $NPERYEAR in
    12)
      mon1=`echo "$dates" | cut -b 29-31`
        y1=`echo "$dates" | cut -b 32-35`
      mon2=`echo "$dates" | cut -b 40-42`
        y2=`echo "$dates" | cut -b 43-46`;;
   360)
      day1=`echo "$dates" | cut -b 30-31`
      mon1=`echo "$dates" | cut -b 32-34`
        y1=`echo "$dates" | cut -b 35-38`
      day2=`echo "$dates" | cut -b 43-44`
      mon2=`echo "$dates" | cut -b 45-47`
        y2=`echo "$dates" | cut -b 48-51`;;
   365)
      day1=`echo "$dates" | cut -b 30-31`
      mon1=`echo "$dates" | cut -b 32-34`
        y1=`echo "$dates" | cut -b 35-38`
      day2=`echo "$dates" | cut -b 43-44`
      mon2=`echo "$dates" | cut -b 45-47`
        y2=`echo "$dates" | cut -b 48-51`;;
   366)
      day1=`echo "$dates" | cut -b 30-31`
      mon1=`echo "$dates" | cut -b 32-34`
        y1=`echo "$dates" | cut -b 35-38`
      day2=`echo "$dates" | cut -b 43-44`
      mon2=`echo "$dates" | cut -b 45-47`
        y2=`echo "$dates" | cut -b 48-51`;;
   *) mon1="Jan";mon2="Dec";day1="01";day2="31";;
    esac
  fi
fi
case "$mon1" in
        Jan) m1=1; s1="selected";;
        Feb) m1=2; s2="selected";;
	Mar) m1=3; s3="selected";;
	Apr) m1=4; s4="selected";;
	May) m1=5; s5="selected";;
	Jun) m1=6; s6="selected";;
	Jul) m1=7; s7="selected";;
	Aug) m1=8; s8="selected";;
	Sep) m1=9; s9="selected";;
	Oct) m1=10; s10="selected";;
	Nov) m1=11; s11="selected";;
	Dec) m1=12; s12="selected";;
	DJF) m1=1; s1="selected";;
	MAM) m1=2; s2="selected";;
	JJA) m1=3; s3="selected";;
	SON) m1=4; s4="selected";;
esac
case "$mon2" in
	Jan) m2=1; ss1="selected";;
	Feb) m2=2; ss2="selected";;
	Mar) m2=3; ss3="selected";;
	Apr) m2=4; ss4="selected";;
	May) m2=5; ss5="selected";;
	Jun) m2=6; ss6="selected";;
	Jul) m2=7; ss7="selected";;
	Aug) m2=8; ss8="selected";;
	Sep) m2=9; ss9="selected";;
	Oct) m2=10; ss10="selected";;
	Nov) m2=11; ss11="selected";;
	Dec) m2=12; ss12="selected";;
	DJF) m2=1; ss1="selected";;
	MAM) m2=2; ss2="selected";;
	JJA) m2=3; ss3="selected";;
	SON) m2=4; ss4="selected";;
esac

if [ "$NX" -le 1 -a "$NZ" -gt 1 ]; then
    latlon="Level-lat"
elif [ "$NX" -le 1 -a "$NZ" -gt 1 ]; then
    latlon="Level-lon"
else
    latlon="Lat-lon"
fi
cat <<EOF
<div class="formheader">$latlon plot</div>
<div class="formbody">
<form action="plotfield.cgi" method="POST">
<input type="hidden" name="EMAIL" value="$EMAIL">
<input type="hidden" name="field" value="$FORM_field">
<input type="hidden" name="movie" value="no" checked>
<table style='width:100%' border='0' cellpadding='0' cellspacing='0'>
EOF
if [ $NPERYEAR != 0 ]; then
    echo "<tr><td>Time:<td>year: <input type=$number min=1 max=2500 step=1 name="year" $textsize4 value=\"$y2\">"
fi
if [ $NPERYEAR -ge 12 ]; then
periods=months
cat <<EOF
month: <select class="forminput" name="month">
<option value="1" $ss1>Jan
<option value="2" $ss2>Feb
<option value="3" $ss3>Mar
<option value="4" $ss4>Apr
<option value="5" $ss5>May
<option value="6" $ss6>Jun
<option value="7" $ss7>Jul
<option value="8" $ss8>Aug
<option value="9" $ss9>Sep
<option value="10" $ss10>Oct
<option value="11" $ss11>Nov
<option value="12" $ss12>Dec
</select>
EOF
elif [ $NPERYEAR -eq 4 ]; then
periods=seasons
cat <<EOF
month: <select class="forminput" name="month">
<option value="1" $ss1>DJF
<option value="2" $ss2>MAM
<option value="3" $ss3>JJA
<option value="4" $ss4>SON
</select>
EOF
else
  # GrADS needs a month
  echo "<input type=\"hidden\" name=\"month\" value=\"1\">"
fi
if [ $NPERYEAR -gt 12 ]; then
  if [ $NPERYEAR = 360 -o $NPERYEAR = 365 -o $NPERYEAR = 366 ]; then
    periods=days
  else
    periods=periods
  fi
  echo "day: <select class=\"forminput\" name=\"day\">"
  dy=0
  while [ $dy -lt 31 ]
  do
      dy=$((dy+1))
      if [ $dy = "$FORM_day" ]; then
	  echo "<option selected>$dy"
      else
	  echo "<option>$dy"
      fi
  done
  echo "</select>"
  if [ $NPERYEAR -ge 1440 ]; then
    cat <<EOF
hour: <select class="forminput" name="hour">
<option value="03">00-06
<option value="09">06-12
<option value="15">12-18
<option value="21">18-24
</select>
EOF
  fi
fi
cat <<EOF
<!--
The movie option has bugs and has been disabled for the time being.
<input type="radio" name="movie" value="yes">Movie from 
year: <input type="$number" min=1 max=2500 step=1 class="forminput" name="year1" size="4" style="width: 5em;" value="$y1">
month: <select class="forminput" name="month1">
<option value="1" $s1>Jan
<option value="2" $s2>Feb
<option value="3" $s3>Mar
<option value="4" $s4>Apr
<option value="5" $s5>May
<option value="6" $s6>Jun
<option value="7" $s7>Jul
<option value="8" $s8>Aug
<option value="9" $s9>Sep
<option value="10" $s10>Oct
<option value="11" $s11>Nov
<option value="12" $s12>Dec
</select>
to
year: <input type="$number" min=1 max=2500 step=1 class="forminput" name="year2" size="4" style="width: 5em;" value="$y2">
month: <select name="month2">
<option value="1" $ss1>Jan
<option value="2" $ss2>Feb
<option value="3" $ss3>Mar
<option value="4" $ss4>Apr
<option value="5" $ss5>May
<option value="6" $ss6>Jun
<option value="7" $ss7>Jul
<option value="8" $ss8>Aug
<option value="9" $ss9>Sep
<option value="10" $ss10>Oct
<option value="11" $ss11>Nov
<option value="12" $ss12>Dec
</select>
<br>
Computing a 10 year movie takes 5 minutes and results in a 1MB animated GIF
<br>
-->
EOF
if [ $NPERYEAR -ge 4 ]; then
cat <<EOF
<tr><td>&nbsp;<td>average over <select class="forminput" name="plotsum">
<option $sum_1_selected>1
<option $sum_2_selected>2
<option $sum_3_selected>3
<option $sum_4_selected>4
EOF
if [ $NPERYEAR -ge 12 ]; then
cat <<EOF
<option $sum_5_selected>5
<option $sum_6_selected>6
<option $sum_7_selected>7
<option $sum_8_selected>8
<option $sum_9_selected>9
<option $sum_10_selected>10
<option $sum_11_selected>11
<option $sum_12_selected>12
<option $sum_13_selected>13
<option $sum_14_selected>14
<option $sum_18_selected>18
<option $sum_19_selected>19
<option $sum_24_selected>24
<option $sum_36_selected>36
<option $sum_48_selected>48
<option $sum_60_selected>60
EOF
if [ $NPERYEAR -gt 12 ]; then
cat <<EOF
<option $sum_15_selected>15
<option $sum_18_selected>18
<option $sum_24_selected>24
<option $sum_30_selected>30
<option $sum_60_selected>60
<option $sum_60_selected>60
<option $sum_75_selected>75
<option $sum_105_selected>105
<option $sum_120_selected>120
<option $sum_180_selected>180
<option $sum_240_selected>240
<option $sum_300_selected>300
<option $sum_360_selected>360
<option $sum_480_selected>480
<option $sum_600_selected>600
<option $sum_1200_selected>1200
EOF
fi
fi
echo "</select>$periods<br>"
fi
cat <<EOF
<tr><td>Anomalies:<td>
<input type="checkbox" class="formcheck" name="plotanomaly" $plotanomaly_checked><select class="forminput" name="plotanomalykind"><option $absolute_selected>absolute<option $relative_selected>relative<option $logrelative_selected>logrelative</select>anomalies wrt to
<input type="$number" min=1 max=2500 step=1 class="forminput" name="climyear1" size="4" style="width: 5em;" value="$FORM_climyear1">:
<input type="$number" min=1 max=2500 step=1 class="forminput" name="climyear2" size="4" style="width: 5em;" value="$FORM_climyear2"> (default: all data)
EOF
intable=TRUE
latlononly=true
NEWUNITS=$UNITS # to kill the unit-changing option, which has not been implemented
. ./plotoptions.cgi
echo "<tr><td colspan=2><input type=\"submit\" class=\"formbutton\" value=\"Plot\"></table></form></div>"

if [ $NPERYEAR != 0 ]; then
cat <<EOF
<p>
<div class="formheader">Hovmuller (time-space) plot</div>
<div class="formbody">
<form action="plotfield.cgi" method="POST">
<input type="hidden" name="EMAIL" value="$EMAIL">
<input type="hidden" name="field" value="$FORM_field">
<input type="hidden" name="hovmuller" value="yes" checked>
<table style='width:100%' border='0' cellpadding='0' cellspacing='0'>
<tr><td>Time:<td>From year: <input type="$number" min=1 max=2500 step=1 class="forminput" name="year" $textsize4 value="$y1">
EOF
if [ $NPERYEAR -ge 12 ]; then
    cat <<EOF
month: <select class="forminput" name="month">
<option value="1" $s1>Jan
<option value="2" $s2>Feb
<option value="3" $s3>Mar
<option value="4" $s4>Apr
<option value="5" $s5>May
<option value="6" $s6>Jun
<option value="7" $s7>Jul
<option value="8" $s8>Aug
<option value="9" $s9>Sep
<option value="10" $s10>Oct
<option value="11" $s11>Nov
<option value="12" $s12>Dec
</select>
<br>
EOF
fi
cat <<EOF
to year: <input type="$number" min=1 max=2500 step=1 class="forminput" name="year2" size="4" style="width: 5em;" value="$y2">
EOF
if [ $NPERYEAR -ge 12 ]; then
    cat <<EOF
month: <select class="forminput" name="month2">
<option value="1" $ss1>Jan
<option value="2" $ss2>Feb
<option value="3" $ss3>Mar
<option value="4" $ss4>Apr
<option value="5" $ss5>May
<option value="6" $ss6>Jun
<option value="7" $ss7>Jul
<option value="8" $ss8>Aug
<option value="9" $ss9>Sep
<option value="10" $ss10>Oct
<option value="11" $ss11>Nov
<option value="12" $ss12>Dec
</select>
</td></tr><tr><td>Anomalies:</td><td>
<input type="checkbox" class="formcheck" name="plotanomaly"> 
<select class="forminput" name="plotanomalykind"><option>absolute<option>relative<option>logrelative</select>anomalies wrt to
<input type="$number" min=1 max=2500 step=1 class="forminput" name="climyear1" size="4" style="width: 5em;">:
<input type="$number" min=1 max=2500 step=1 class="forminput" name="climyear2" size="4" style="width: 5em;"> (default: all data)
EOF
fi

intable=TRUE
NEWUNITS=$UNITS # to kill the unit-changing option, which has not been implemented
. ./plotoptions.cgi
echo "<tr><td colspan=2><input type=\"submit\" class=\"formbutton\" value=\"Plot\"></table></form></div>"
fi # NPEREYAR != 0

. ./myvinkfoot.cgi
