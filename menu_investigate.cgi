#!/bin/bash
[ -z "$NAME" ] && NAME=$FORM_NAME
name=`echo $NAME | tr ' +' '_%'`
wmo=` echo $WMO | tr ' +' '_%'`
STATION=`echo $STATION | tr ' +' '_%'`

cat <<EOF
<div class="menukopje">Investigate this time series</div>
EOF
if [ "${NPERYEAR:-12}" = '12' ]; then
  cat << EOF
<div class="menulink">View per <a href="plotseries.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&KIND=month">month</a>, <a href="plotseries.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&KIND=season">season</a>, <a href="plotseries.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&KIND=half">half year</a> or full year (<a href="plotseries.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&KIND=yr0">Jan-Dec</a> or <a href="plotseries.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&KIND=yr1">Jul-Jun</a>)</div>
<div class="menulink">View last 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=12&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">1</a>, 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=60&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">5</a>, 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=120&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">10</a>,
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=${NPERYEAR:-12}&enddate=last">N</a>
years</div>
EOF
elif [ "${NPERYEAR:-12}" -ge 360 ]; then
  cat << EOF
<div class="menulink">View last 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=30&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">30</a>, 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=90&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">90</a>, 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=365&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">365</a>,
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=${NPERYEAR:-12}&enddate=last">N</a>
days</div>
EOF
elif [ "${NPERYEAR#-}" = 1 ]; then
  cat << EOF
<div class="menulink">View per <a href="plotseries.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&KIND=yr">year</a></div>
<div class="menulink">View last 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=10&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">10</a>, 
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=20&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">20</a>,
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&nday=50&climyear1=1991&climyear2=2020&NPERYEAR=${NPERYEAR:-12}&enddate=last">50</a>,
<a href="plotdaily.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=${NPERYEAR:-12}&enddate=last">N</a>
years</div>
EOF
fi
cat <<EOF
<div class="menulink"><a href="corseries.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Correlate with other time series</a></div>
<div class="menulink"><a href="corfield.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Correlate with a field (correlation, regression, composite)</a>
<div class="menulink"><a href="corfield_obs.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">only observations</a></div>
<div class="menulink"><a href="corfield_rea.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">only reanalyses</a></div>
<div class="menulink"><a href="corfield_sea.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">only seasonal forecasts</a></div>
<div class="menulink"><a href="corfield_cmip5.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">only scenario runs</a></div>
<div class="menulink"><a href="corfield_use.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">only user-defined fields</a></div>
</div>
<div class="menulink"><a href="verificationform.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Verify against another time series</a></div>
<div class="menulink"><a href="periodform.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Spectrum, autocorrelation function</a></div>
<div class="menulink"><a href="waveform.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Wavelet</a></div>
<div class="menulink"><a href="runningmomentsform.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Running mean/s.d./skew/curtosis</a></div>
<div class="menulink"><a href="attributeform.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Trends in return times of extremes</a></div>
<div class="menulink"><a href="histogramform.cgi?id=$EMAIL&TYPE=$TYPE&WMO=$wmo&STATION=$STATION&NAME=$name&NPERYEAR=$NPERYEAR">Plot and fit distribution</a></div>
EOF
