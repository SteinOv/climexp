#!/bin/bash
#
# average an ensemble of time series, take min/max or take ensemble anomalies

export DIR=`pwd`
. ./getargs.cgi

if [ -n "$EMAIL" -a "$EMAIL" != someone@somewhere ]; then
  def=./prefs/$EMAIL.average_ensemble
  cat > $def << EOF
FORM_oper=$FORM_oper;
FORM_nens1=$FORM_nens1;
FORM_nens2=$FORM_nens2;
EOF
fi

[ -z "$FORM_oper" ] && FORM_oper=mean
if [ "$FORM_oper" = anomalies -o \( -z "$FORM_nens1" -a -z "$FORM_nens2" \) ]; then
    WMO=`echo "$FORM_wmo" | sed -e "s/\+\+\+/$FORM_oper/" -e "s/\+\+/$FORM_oper/" -e "s/@@/$FORM_oper/"`
    STATION="${FORM_station}_$FORM_oper"
else
    WMO=`echo "$FORM_wmo" | sed -e "s/\+\+\+/${FORM_oper}_${FORM_nens1}_${FORM_nens2}/" -e "s/\+\+/${FORM_oper}_${FORM_nens1}_${FORM_nens2}/" -e "s/@@/${FORM_oper}_${FORM_nens1}_${FORM_nens2}/"`
    STATION="$FORM_station $FORM_oper ${FORM_nens1}:${FORM_nens2}"
fi
TYPE="$FORM_type"
NAME="$FORM_name"
if [ "$FORM_oper" = anomalies ]; then
    WMO=${WMO}_@@
    PROG="seriesensanomal -1 data/$TYPE$FORM_wmo.dat"
else
    PROG="average_ensemble data/$TYPE$FORM_wmo.dat ens ${FORM_nens1:-0} ${FORM_nens2:-999} $FORM_oper"
fi

. ./getdata.cgi
