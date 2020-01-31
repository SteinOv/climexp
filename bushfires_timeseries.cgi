#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Australian fire risk study" "time series" nofollow

cat <<EOF
All time series are averaged over the South-East Australia bush fire region, land points in (155,-29) (150,-29) (144,-40) (155,-40).
We also made scripts that compute all numbers in the paper: <a href=SEAustralia/fit_heat.sh>heat</a>, <a href=SEAustralia/fit_drought_annual.sh>annual drought</a>, <a href=SEAustralia/fit_drought_annual_2100.sh>annual drought up to 2100</a>, 

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
<a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_DJF_max_tasmax_7day_runmean_@@&STATION=CanESM2_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/CESM1-CAM5_1920-2100_SONDJF_max_tasmax_7day_runmean_@@&STATION=CESM1-CAM5_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM1-CAM5 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-ESM2M_1950-2100_SONDJF_max_tasmax_7day_runmean_@@&STATION=GFDL-ESM2M_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-ESM2M Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/ipsl_yearly_tmax_july-june_nsw_@@&STATION=IPSL_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">IPSL Tmax 7day rm Jul-Jun</a>.

<p><i><b>Drought</b></i><br> 
Monthly: <a href="getindices.cgi?WMO=SEAustralia/gpccall_10_mask0_su&STATION=GPCC_bushfire&TYPE=i&id=$EMAIL">GPCC pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/cru4_pre_10_mask0_land_su&STATION=CRU_TS_bushfire&TYPE=i&id=$EMAIL">CRU TS pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/pr_Amon_ECEARTH23_rcp85_mask0_land_su_%%&STATION=EC-Earth_bushfire&TYPE=i&id=$EMAIL">EC-Earth pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/pr_Amon_HadGEM3-A-N216_historical_mask0_land_su_%%%&STATION=HadGEM3-A_bushfire&TYPE=i&id=$EMAIL">HadGEM3-A pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/ipsl_monthly_pr_nsw_@@&STATION=IPSL_bushfire&TYPE=i&id=$EMAIL">IPSL pr</a>,
<br>Annual: <a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_Jan-Dec_annual_mean_pr_@@&STATION=CanESM2_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/CESM1-CAM5_1920-2100_Jan-Dec_annual_mean_pr_@@&STATION=CESM1-CAM5_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM1-CAM5 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/CSIRO-Mk3-6-0_1850-2100_Jan-Dec_annual_mean_pr_@@&STATION=CSIRO-Mk3-6-0_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CSIRO-Mk3-6-0 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-CM3_1920-2100_Jan-Dec_annual_mean_pr_@@&STATION=GFDL-CM3_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-CM3 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-ESM2M_1950-2100_Jan-Dec_annual_mean_pr_@@&STATION=GFDL-ESM2M_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-ESM2M pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/MPI-ESM_1850-2099_Jan-Dec_annual_mean_pr_@@&STATION=MPI-ESM_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-ESM pr</a>.

<p><i><b>Fire Weather Index</b></i><br>
ERA5: 
<a href="getindices.cgi?WMO=SEAustralia/era5_yearly_seasmax_nsw&STATION=ERA5_FWI&TYPE=i&NPERYEAR=1&id=$EMAIL">ERA5 annual seasonal maximum NSW</a>,

<a href="getindices.cgi?WMO=SEAustralia/era5_monthly_msr_nsw&STATION=ERA5_MSR&TYPE=i&NPERMONTH=1&id=$EMAIL">ERA5 MSR monthly NSW</a>,

<a href="getindices.cgi?WMO=SEAustralia/msr_yearly_seasmax_nsw&STATION=ERA5_MSR_SM&TYPE=i&NPERYEAR=1&id=$EMAIL">ERA5 MSR yearly NSW</a>,

<br>

MODELS:
<a href="getindices.cgi?WMO=SEAustralia/cesm_yearly_fwi_seasmax_nsw_@@&STATION=CESM2_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM annual seasonal maximum FWI</a>,
<a href="getindices.cgi?WMO=SEAustralia/ecearth_yearly_fwi_seasmax_nsw_@@&STATION=EC-Earth_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth annual seasonal maximum FWI</a>,
<a href="getindices.cgi?WMO=SEAustralia/canesm_yearly_fwi_seasmax_nsw_@@&STATION=CanESM2_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 annual seasonal maximum FWI</a>,
<a href="getindices.cgi?WMO=SEAustralia/ipsl_yearly_fwi_seasmax_nsw_@@&STATION=IPSL_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">IPSL annual seasonal maximum FWI</a>,

<p><i><b>Ocean indices</b></i><br> 
IOD: <a href="getindices.cgi?WMO=NCDCData/dmi_ersst&STATION=DMI_ERSST&TYPE=i&id=$EMAIL">ERSSTv5 obs</a>, <a href="getindices.cgi?WMO=SEAustralia/dmi_ecearth_%%&STATION=DMI_EC-earth&TYPE=i&id=$EMAIL">EC-Earth</a>, 
<br>IOD-Nino3.4: <a href="getindices.cgi?WMO=SEAustralia/dmi-enso_ersst&STATION=DMI-ENSO&TYPE=i&id=$EMAIL">ERSSTv5 obs</a>, <a href="getindices.cgi?WMO=SEAustralia/dmi-enso_ecearth_%%%&STATION=DMI-NINO34_EC-Earth&TYPE=i&id=$EMAIL">EC-Earth</a>, 
EOF

. ./myvinkfoot.cgi
