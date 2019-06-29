#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "France 2019 heat wave study" "time series" nofollow

cat <<EOF
All daily data, take the 3-day average and June max yourself.

<p><b>Observations</b>
<br>France: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iensembles_025_tg_France_metropolitan_su&STATION=EOBS_TG_France">E-OBS</a>,
<a href=getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iberkeley_tavg_daily_full_France_metropolitan_su&STATION=Berkeley_TG_France">Berkeley</a>,
<a href=getindices.cgi?id=$EMAIL&WMO=data/ierai_t2m_daily_e_France_metropolitan_su&STATION=ERA-i_T2m_France">ERA-interim+ECMEF analyses+forecasts</a>,
<br>Toulouse: <a href="becatemp.cgi?id=$EMAIL&WMO=33&STATION=TOULOUSE-BLAGNAC">ECA&amp;D</a>,
<a href=getindices.cgi?id=$EMAIL&WMO=data/ierai_t2m_daily_e_1.38E_43.62N_n_su&STATION=ERA-i_T2m_Toulouse">ERA-interim+ECMEF analyses+forecasts</a>

<p><b>Models</b>
<br>France: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_France_metropolitan_su_%%&STATION=EC-Earth23_tas_France&NPERYEAR=366">16 EC-Earth 2.3 1861-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_France_metropolitan_5lan_su_%%&STATION=RACMO22_tas_France&NPERYEAR=366">16 RACMO 2.2 1950-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_France_metropolitan_su_%%&STATION=EUROCORDEX11bc_tas_France&NPERYEAR=366">10 EUROCORDEX 11m bc 1971-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_France_metropolitan_5lan_su_%%%&STATION=HadGEM3A_tas_France&NPERYEAR=360">HadGEM3-A-N216 1960-2014</a>,
<br>Toulouse: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_1.38E_43.62N_n_su_%%&STATION=EC-Earth23_tas_Toulouse">16 EC-Earth 2.3 1861-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_1.38E_43.62N_n_su_%%&STATION=RACMO22_tas_Toulouse">16 RACMO 2.2 1950-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_1.38E_43.62N_n_su_%%&STATION=EUROCORDEX11bc_tas_Toulouse&NPERYEAR=366">10 EUROCORDEX 11m bc 1971-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_1.38E_43.62N_n_su_%%%&STATION=HadGEM3A_tas_Toulouse&NPERYEAR=360">HadGEM3-A-N216 1960-2014</a>,
<br>Western Europe JJA mean: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_-12-20E_35-72N_n_su_%%&STATION=EC-Earth23_tas_WEurope">16 EC-Earth 2.3 1861-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_-15-20E_37-66N_n_5lan_su_%%&STATION=RACMO22_tas_WEurope">16 RACMO 2.2 1950-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_-12-20E_35-72N_n_su_%%_mean4_anom_30_max1_anom_15yr_low-pass_box_30&STATION=EUROCORDEX11bc_JJA_tas_WEurope"&NPERYEAR=1>10 EUROCORDEX 11m bc 1971-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_-12-20E_35-72N_n_5lan_su_%%%&STATION=HadGEM3A_tas_WEurope">HadGEM3-A-N216 1960-2014</a>,

EOF

. ./myvinkfoot.cgi