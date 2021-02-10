#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Baltic November 2020 temperature anomaly study" "time series" nofollow

cat <<EOF

<p><i>Estonia</i><br>
<a href="getindices.cgi?WMO=Baltic/November_temp_Estonia&STATION=November_T_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Estonia_su_%%%&STATION=HadGEM3A_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_Estonia_su_%%&STATION=EC-Earth23_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth2.3</a>,
<a href="getindices.cgi?WMO=Baltic/Estonia/tas_Estonia_1970-2050_weighted_%%%&STATION=EC-Earth3_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth3</a>,

<p><i>Latvia</i><br>
<a href="getindices.cgi?WMO=Baltic/avg_nov_temp_LV&STATION=November_T_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Latvia_su_%%%&STATION=HadGEM3A_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_Latvia_su_%%&STATION=EC-Earth23_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth2.3</a>,
<a href="getindices.cgi?WMO=Baltic/Latvia/tas_Latvia_1970-2050_weighted_%%%&STATION=EC-Earth3_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth3</a>,

<p><i>Sweden</i><br>
<a href="getindices.cgi?WMO=Baltic/sweYrlyAnoms_monnr_11&STATION=November_T_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Sweden_su_%%%&STATION=HadGEM3A_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_Sweden_su_%%&STATION=EC-Earth23_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth2.3</a>,
<a href="getindices.cgi?WMO=Baltic/Sweden/tas_Sweden_1970-2050_weighted_%%%&STATION=EC-Earth3_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth3</a>,

<p><i>Denmark</i><br>
<a href="getindices.cgi?WMO=Baltic/DMI_november_1874-2020&STATION=November_T_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Denmark_su_%%%&STATION=HadGEM3A_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_Denmark_su_%%&STATION=EC-Earth23_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth2.3</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_t2m_mon_RACMO22E_rcp85_Denmark_su_%%&STATION=RACMO22_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">RACMO2.2E</a>,
<a href="getindices.cgi?WMO=Baltic/Denmark/tas_Denmark_1970-2050_weighted_%%%&STATION=EC-Earth3_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth3</a>,
<a href="getindices.cgi?WMO=Baltic/MPI-ESM_Denmark_@@&STATION=MPI-ESM_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-ESM</a>,

<p><i>Covariates</i><br>
<a href="getindices.cgi?WMO=NASAData/giss_al_gl_a_4yrlo&STATION=smoothed_GMST&TYPE=i&id=$EMAIL">smoothed observed GMST (4-yr running mean GISTEMP)</a>,
annual mean ensemble mean 
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_0-360E_-90-90N_n_su_mean_mean1_anom&STATION=EC-Earth2.3_GMST&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth2.3 GMST</a>,
<a href="getindices.cgi?WMO=Baltic/tas_historicalssp119_1970-2050_ensmean&STATION=EC-Earth3_GMST&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth3 GMST</a>,
EOF

. ./myvinkfoot.cgi
