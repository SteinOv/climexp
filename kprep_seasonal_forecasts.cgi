#!/bin/bash
. ./init.cgi
echo 'Content-Type: text/html'
echo
echo

DIR=`pwd`
. ./getargs.cgi
if [ -z "$EMAIL" ]; then
  EMAIL=someone@somewhere
fi
if [ -z "$FORM_internal" ]; then
# only use saved preferences when the script is called without the hidden variable "internal"
  if [ "$EMAIL" != someone@somewhere ]; then
    def=./prefs/$EMAIL.forecastverification
    if [ -s $def ]; then
      eval `egrep '^FORM_[a-z0-9]*=[-+a-zA-Z0-9._]*;$' $def`
###      echo '<pre>'
###      egrep '^FORM_[a-z0-9]*=[-+a-zA-Z0-9._]*;$' $def
###      echo '</pre>'
    fi
  fi
fi
# check email address
. ./checkemail.cgi

if [ "$EMAIL" != somene@somewhere ]; then
  pdef=./prefs/$EMAIL.plotoptions
  if [ -s $pdef ]; then
    eval `egrep '^FORM_[a-z0-9]*=[a-zA-Z]*[-+0-9.]*;$' $pdef`
    . ./getfieldopts.cgi
    map0=$map
  fi
fi
. ./myvinkhead.cgi "Seasonal Forecasts" "K-PREP empirical seasonal forecasting system" ""

cat <<EOF
<p>Past observations are used to deduce significant correlations between the weather 
in the last three months (up to the beginning of the month) and the weather over the next season (from the end of the month). The main predictors are El Ni&ntilde;o / La Ni&ntilde;a and the trends due to global warming. Overfitting is avoided as much as possible. The forecasts are accessible in interactive web applications. 
The system has been documented in <a href="http://www.geosci-model-dev.net/8/3947/2015/" target="_new">Eden et al, 2015</a>.

<p><a href="http://climexp.knmi.nl/kprep_mdc">Seasonal forecasts of fire weather / Monthly Drought Code</a>.

<p><a href="http://climexp.knmi.nl/kprep_fc">Seasonal forecasts of temperature, precipitation and sea level pressure</a>.

<p><a href="forecast_verification.cgi?id=$EMAIL">Old seasonal forecast verification page</a>
EOF

. ./myvinkfoot.cgi
