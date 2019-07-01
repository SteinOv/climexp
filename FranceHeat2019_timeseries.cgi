#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "France 2019 heat wave study" "time series" nofollow

cat <<EOF
For daily data, take the 3-day average and June max yourself. For annual data this has already been done.

<p><b>Observations</b>
<br>Meteo France 1947-now: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/indT_FR_June&STATION=FR30_TG3x_jun&NPERYEAR=1">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/indT_TLSE_June&STATION=Toulouse_TG3x_jun&NPERYEAR=1">Toulouse</a>,
<br>E-OBS/ECA&amp;D 1950/1947-now: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iensembles_025_tg_France_metropolitan_su&STATION=EOBS_TG_France&NPERYEAR=366">France</a>,
<a href="becatemp.cgi?id=$EMAIL&WMO=33&STATION=TOULOUSE-BLAGNAC&NPERYEAR=366">Toulouse</a>,
<br>Berkeley 1900-now:
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iberkeley_tavg_daily_full_France_metropolitan_su&STATION=Berkeley_TG_France&NPERYEAR=366">France</a>,
<br>ERA-interim+ECMEF analyses+forecasts 1979-now: 
<a href="getindices.cgi?id=$EMAIL&WMO=data/ierai_t2m_daily_e_France_metropolitan_su&STATION=ERA-i_T2m_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=data/ierai_t2m_daily_e_1.38E_43.62N_n_su&STATION=ERA-i_T2m_Toulouse&NPERYEAR=366">Toulouse</a>
<br>CRUTEM4 1900-2018: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/icrutem4_-15-20E_35-72N_n_su_15yr_low-pass_box_30_mean4_trend_max1_anom&STATION=CRUTEM4_WEurope_JJA&NPERYEAR=1">Western Europe JJA</a>

<p><b>Models</b>

<br>10 EUROCORDEX bias-corrected 1971-2100:
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/eurocordex_tasAdjust_day_ens_rcp45_France_metropolitan_su_%%&STATION=EUROCORDEX11bc_tas_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/eurocordex_tasAdjust_day_ens_rcp45_1.38E_43.62N_n_su_%%&STATION=EUROCORDEX11bc_tas_Toulouse&NPERYEAR=366">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/eurocordex_tasAdjust_day_ens_rcp45_-12-20E_35-72N_n_su_%%_mean4_anom_30_max1_anom_15yr_low-pass_box_30&STATION=EUROCORDEX11bc_JJA_tas_WEurope&NPERYEAR=1">Western Europe JJA</a>,
<br>16 RACMO 2.2 1950-2100:
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_France_metropolitan_5lan_su_%%&STATION=RACMO22_tas_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_1.38E_43.62N_n_su_%%&STATION=RACMO22_tas_Toulouse">16 RACMO 2.2 1950-2100</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_mon_RACMO22E_rcp85_-15-20E_37-66N_n_su_mean_15yr_low-pass_box_max1_anom_75&STATION=RACMO22_tas_WEurope">Western Europe JJA</a>,
<br>16 EC-Earth 2.3 1861-2100
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_France_metropolitan_su_%%&STATION=EC-Earth23_tas_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_1.38E_43.62N_n_su_%%&STATION=EC-Earth23_tas_Toulouse">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Amon_ECEARTH23_rcp85_-15-20E_35-72N_n_5lan_su_mean_mean4_anom_max1_anom_15yr_low-pass_box&STATION=EC-Earth23_tas_WEurope">Western Europe JJA</a>,
<br>15 HadGEM3-A-N219 1960-2015
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_France_metropolitan_5lan_su_%%%&STATION=HadGEM3A_tas_France&NPERYEAR=360">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_1.38E_43.62N_n_su_%%%&STATION=HadGEM3A_tas_Toulouse&NPERYEAR=360">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Amon_HadGEM3-A-N216_historical_-15-20E_35-72N_n_5lan_su_mean_mean4_anom_max1_anom_15yr_low-pass_box_20&STATION=HadGEM3A_tas_WEurope">Western Europe JJA</a>,
<br>28 CMIP5 1871-2100
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_France&STATION=tg3x_cmip5_France&NPERYEAR=1">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_Toulouse&STATION=tg3x_cmip5_Toulouse&NPERYEAR=1">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cmip5_%%%_WEurope_JJA&STATION=tas_cmip5_WEurope_JJA&NPERYEAR=1">WEurope JJA</a>,

EOF

. ./myvinkfoot.cgi