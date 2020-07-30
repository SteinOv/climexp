#!/bin/bash
#
# select all values at a given date from a  file

export DIR=`pwd`
. ./init.cgi
. ./getargs.cgi

WMO="${FORM_WMO}_${FORM_month}"
[ -n "FORM_day" ] && WMO="${WMO}_${FORM_day}"
. ./month2string.cgi
if [ -z "$FORM_month" ]; then
    STATION="$seriesmonth $FORM_STATION"
    if [ -n "$FORM_day" ]; then
        STATION="$FORM_day $seriesmonth $FORM_STATION"
    fi
fi
TYPE=$FORM_TYPE
NPERYEAR=1
PROG="selectdate $DIR/data/$TYPE$FORM_WMO.dat $FORM_month $FORM_day"
export WMO
export file
export TYPE

if [ -n "$EMAIL" -a "$EMAIL" != someone@somewhere ]; then
  def=./prefs/$EMAIL.selectdate
  cat > $def << EOF
FORM_month=$FORM_month;
FORM_day=$FORM_day;
EOF
fi

. ./getdata.cgi
