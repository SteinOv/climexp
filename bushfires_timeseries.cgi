#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Australian fire risk study" "time series" nofollow

cat <<EOF
All time series are averaged over the South-East Australia bush fire region, land points in (155,-29) (150,-29) (144,-40) (155,-40).
We also made a <a href=SEAustralia/fit_heat.sh>script</a> that computes all numbers in the paper.

<p><i><b>Heat (only reliable after 1910)</b></i><br> 
Monthly: <a href="getindices.cgi?WMO=SEAustralia/giss_temp_250_mask0_5lan_su&STATION=GISS250_bushfire&TYPE=i&id=$EMAIL">GISTEMP T2m</a>,
<a href="getindices.cgi?WMO=SEAustralia/berkeley_tavg_mask0_5lan_su_ext&STATION=t2m_Berkeley_bushfire&TYPE=i&id=$EMAIL">Berkeley T2m</a>,
<a href="getindices.cgi?WMO=SEAustralia/berkeley_tavg_mask0_5lan_su_ext&STATION=t2m_Berkeley_bushfire&TYPE=i&id=$EMAIL">Berkeley Tmax</a>
<br>
Daily fields:
<a href="select.cgi?id=$EMAIL&field=SEAustralia/TMAX_Daily_LatLong1_full_110-155E_-45--10N_su_extended.info">Berkeley Tmax</a>,
<a href="select.cgi?id=$EMAIL&field=SEAustralia/tasmax_day_ECEARTH23_rcp85__%%_110-155E_-45--10N_su.info">EC-Earth T159 Tmax</a>,
<a href="select.cgi?id=$EMAIL&field=SEAustralia/tasmax_day_HadGEM3-A-N216_historical_110-155E_-45--10N_su.info">HadGEM3-A N219</a>,
<br>
Annual time series:
<a href="getindices.cgi?WMO=SEAustralia/TMAX_Daily_LatLong1_full_110-155E_-45--10N_su_extended.info_4_max_7v_mask0_su&STATION=Berkeley_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=4">Berkeley Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/tasmax_day_ECEARTH23_rcp85___110-155E_-45--10N_su_info_4_max_7v_mask0_land_su_%%&STATION=EC-Earth_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=4">EC-Earth T159 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/tasmax_day_HadGEM3-A-N216_historical_110-155E_-45--10N_su_info_4_max_7v_____mask0_land_su_%%%&STATION=HadGEM3A_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=4">HadGEM3-A N219 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-ESM2M_1950-2100_SONDJF_max_tasmax_7day_runmean_@@&STATION=GFDL-ESM2M_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-ESM2M Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/CESM1-CAM5_1920-2100_SONDJF_max_tasmax_7day_runmean_@@&STATION=CESM1-CAM5_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM1-CAM5 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_DJF_max_tasmax_7day_runmean_@@&STATION=CanESM2_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 Tmax</a>

<p><i><b>Drought</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/gpccall_10_mask0_su&STATION=GPCC_bushfire&TYPE=i&id=$EMAIL">GPCC</a>,

<p><i><b>Fire Weather Index</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/era5_yearly_seasmax_nsw&STATION=ERA5_FWI&TYPE=i&NPERYEAR=1&id=$EMAIL">ERA5 annual</a>

EOF

. ./myvinkfoot.cgi
