#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Australian fire risk study" "time series" nofollow

cat <<EOF
All time series are averaged over the South-East Australia bush fire region, land points in (155,-29) (150,-29) (144,-40) (155,-40).
We also made scripts that compute all numbers in the paper: <a href=SEAustralia/fit_heat.sh>heat</a>, <a href=SEAustralia/fit_drought_annual.sh>annual drought</a>, <a href=SEAustralia/fit_drought_annual_2100.sh>annual drought up to 2100</a>, <a href=SEAustralia/fit_driest_month.sh>driest month in SONDJF</a>, <a href=SEAustralia/fit_fwi.sh>FWI SONDJF max</a>, <a href=SEAustralia/fit_msr.sh>MSR SONDJF max</a> 

<p><i><b>Area burned</b></i><br> 
Monthly: <a href="getindices.cgi?WMO=SEAustralia/burned_area&STATION=modis_burned_area&TYPE=i&id=$EMAIL">MODIS 1997-2018</a>.
<p><i><b>FWI ERA5 monthly mean 1997-2018, data for Fig 2</b></i><br>
Monthly: <a href="getindices.cgi?WMO=SEAustralia/fwi_era5_monmean_97-18_nsw&STATION=FWI_era5_monmean_nsw&TYPE=i&id=$EMAIL">FWI ERA5 1997-2018</a>.




<p><i><b>Heat (only reliable after 1910)</b></i><br> 
Monthly: <a href="getindices.cgi?WMO=SEAustralia/giss_temp_250_mask0_5lan_su&STATION=GISS250_bushfire&TYPE=i&id=$EMAIL">GISTEMP T2m</a>,
<a href="getindices.cgi?WMO=SEAustralia/berkeley_tavg_mask0_5lan_su_ext&STATION=t2m_Berkeley_bushfire&TYPE=i&id=$EMAIL">Berkeley T2m</a>,
<a href="getindices.cgi?WMO=SEAustralia/berkeley_tmax_mask0_5lan_su_ext&STATION=tmax_Berkeley_bushfire&TYPE=i&id=$EMAIL">Berkeley Tmax</a>.
<br>
Daily fields:
<a href="select.cgi?id=$EMAIL&field=SEAustralia/TMAX_Daily_LatLong1_full_110-155E_-45--10N_su_extended.info">Berkeley Tmax</a>.
<br>
Annual time series:
<a href="getindices.cgi?WMO=SEAustralia/berkeley_tmax_daily_-1_max_50_7v_mask0_5lan_su_ext&STATION=Berkeley_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">Berkeley Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/tmax_acorn_ave&STATION=ACORN_stations_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">ACORN stations Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/awap_tmax_-1_max_50_7v_mask0_5lan_su&STATION=AWAP_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">AWAP Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/era5_tmax_daily_-1_max_mask2_5lan_su_ext&STATION=ERA5_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">ERA5 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/c3tmax_daily_-1_max_50_7v_trend_mask47_land_su&STATION=20CRv3_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">20CRv3 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/CERA20C_DJF_TX7x_region_@@&STATION=CERA-20C_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">CERA-20C Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/JRA55_TX7x_DJF_NSW&STATION=tmax_JRA55_bushfire&TYPE=i&NPERYEAR=1&id=$EMAIL">JRA55 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/tasmax_day_ECEARTH23_rcp85___110-155E_-45--10N_su_info_4_max_7v_mask0_land_su_%%&STATION=EC-Earth_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=4">EC-Earth T159 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/tasmax_day_HadGEM3-A-N216_historical_110-155E_-45--10N_su_info_4_max_7v_____mask0_land_su_%%%&STATION=HadGEM3A_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=4">HadGEM3-A N219 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_DJF_max_tasmax_7day_runmean_@@&STATION=CanESM2_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/CESM1-CAM5_1920-2100_SONDJF_max_tasmax_7day_runmean_@@&STATION=CESM1-CAM5_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM1-CAM5 Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-ESM2M_1950-2100_SONDJF_max_tasmax_7day_runmean_@@&STATION=GFDL-ESM2M_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-ESM2M Tmax</a>,
<a href="getindices.cgi?WMO=SEAustralia/ipsl_yearly_tmax_july-june_nsw_@@&STATION=IPSL_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">IPSL Tmax 7day rm Jul-Jun</a>,
<a href="getindices.cgi?WMO=SEAustralia/ASF20C_TX7x_DJF_1900_2009_NSW_@@&STATION=ASF20C_Tmax&TYPE=i&id=$EMAIL&NPERYEAR=1">ASF20C Tmax 7day DJF</a>.
<a href="getindices.cgi?WMO=SEAustralia/wah_yearly_tmax_seasmax_nsw_actual_@@&STATION=W@H_Tmax_actual&TYPE=i&id=$EMAIL&NPERYEAR=1">WAH Tmax 7day rm Sep-Feb Actual</a>,
<a href="getindices.cgi?WMO=SEAustralia/wah_yearly_tmax_seasmax_nsw_natural_@@&STATION=W@H_Tmax_natural&TYPE=i&id=$EMAIL&NPERYEAR=1">WAH Tmax 7day rm Sep-Feb Natural</a>,

<p><i><b>Drought</b></i><br> 
Monthly: <a href="getindices.cgi?WMO=SEAustralia/gpccall_10_mask0_su&STATION=GPCC_bushfire&TYPE=i&id=$EMAIL">GPCC pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/cru4_pre_10_mask0_land_su&STATION=CRU_TS_bushfire&TYPE=i&id=$EMAIL">CRU TS pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/awap_prcp_mo_mask0_land_su&STATION=AWAP_bushfire&TYPE=i&id=$EMAIL">AWAP pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/pr_Amon_ECEARTH23_rcp85_mask0_land_su_%%&STATION=EC-Earth_bushfire&TYPE=i&id=$EMAIL">EC-Earth pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/pr_Amon_HadGEM3-A-N216_historical_mask0_land_su_%%%&STATION=HadGEM3-A_bushfire&TYPE=i&id=$EMAIL">HadGEM3-A pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/ipsl_monthly_pr_nsw_@@&STATION=IPSL_bushfire&TYPE=i&id=$EMAIL">IPSL pr</a>.
<a href="getindices.cgi?WMO=SEAustralia/wah_monthly_pr_nsw_actual_@@&STATION=WAH_bushfire_actual&TYPE=i&id=$EMAIL">WAH pr actual</a>,
<a href="getindices.cgi?WMO=SEAustralia/wah_monthly_pr_nsw_natural_@@&STATION=WAH_bushfire_natural&TYPE=i&id=$EMAIL">WAH pr natural</a>.
<br>Annual mean: <a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_Jan-Dec_annual_mean_pr_@@&STATION=CanESM2_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/CESM1-CAM5_1920-2100_Jan-Dec_annual_mean_pr_@@&STATION=CESM1-CAM5_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM1-CAM5 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/CSIRO-Mk3-6-0_1850-2100_Jan-Dec_annual_mean_pr_@@&STATION=CSIRO-Mk3-6-0_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CSIRO-Mk3-6-0 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-CM3_1920-2100_Jan-Dec_annual_mean_pr_@@&STATION=GFDL-CM3_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-CM3 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-ESM2M_1950-2100_Jan-Dec_annual_mean_pr_@@&STATION=GFDL-ESM2M_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-ESM2M pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/MPI-ESM_1850-2099_Jan-Dec_annual_mean_pr_@@&STATION=MPI-ESM_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-ESM pr</a>.
<br>Driest month in SONDJF: 
<a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_SONDJF_min_month_pr_@@&STATION=CanESM2_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/CESM1-CAM5_1920-2100_SONDJF_min_month_pr_@@&STATION=CESM1-CAM5_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM1-CAM5 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/CSIRO-Mk3-6-0_1850-2100_SONDJF_min_month_pr_@@&STATION=CSIRO-Mk3-6-0_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">CSIRO-Mk3-6-0 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-CM3_1920-2100_SONDJF_min_month_pr_@@&STATION=GFDL-CM3_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-CM3 pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/GFDL-ESM2M_1950-2100_SONDJF_min_month_pr_@@&STATION=GFDL-ESM2M_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-ESM2M pr</a>,
<a href="getindices.cgi?WMO=SEAustralia/MPI-ESM_1850-2099_SONDJF_min_month_pr_@@&STATION=MPI-ESM_pr&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-ESM pr</a>.

<p><i><b>Fire Weather Index</b></i><br>
ERA5: 
<a href="getindices.cgi?WMO=SEAustralia/era5_yearly_seasmax_nsw&STATION=ERA5_FWI&TYPE=i&NPERYEAR=1&id=$EMAIL">ERA5 annual seasonal maximum NSW</a>,
<a href="getindices.cgi?WMO=SEAustralia/era5_monthly_msr_nsw&STATION=ERA5_MSR&TYPE=i&NPERMONTH=1&id=$EMAIL">ERA5 MSR monthly NSW</a>,
<a href="getindices.cgi?WMO=SEAustralia/msr_yearly_seasmax_nsw&STATION=ERA5_MSR_SM&TYPE=i&NPERYEAR=1&id=$EMAIL">ERA5 MSR yearly NSW</a>.
<br>MODELS FWI:
<a href="getindices.cgi?WMO=SEAustralia/cesm_yearly_fwi_seasmax_nsw_@@&STATION=CESM1_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM annual seasonal maximum FWI</a>,
<a href="getindices.cgi?WMO=SEAustralia/ecearth_yearly_fwi_seasmax_nsw_@@&STATION=EC-Earth_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth annual seasonal maximum FWI</a>,
<a href="getindices.cgi?WMO=SEAustralia/canesm_yearly_fwi_seasmax_nsw_@@&STATION=CanESM2_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 annual seasonal maximum FWI</a>,
<a href="getindices.cgi?WMO=SEAustralia/ipsl_yearly_fwi_seasmax_nsw_@@&STATION=IPSL_FWI&TYPE=i&id=$EMAIL&NPERYEAR=1">IPSL annual seasonal maximum FWI</a>,
<a href="getindices.cgi?WMO=SEAustralia/wah_yearly_fwi_seasmax_nsw_actual_@@&STATION=WAH_FWI_ACTUAL&TYPE=i&id=$EMAIL&NPERYEAR=1">WAH annual seasonal maximum FWI Actual</a>,
<a href="getindices.cgi?WMO=SEAustralia/wah_yearly_fwi_seasmax_nsw_natural_@@&STATION=WAH_FWI_NATURAL&TYPE=i&id=$EMAIL&NPERYEAR=1">WAH annual seasonal maximum FWI Natural</a>,
<br>MODELS MSR:
<a href="getindices.cgi?WMO=SEAustralia/cesm_yearly_msr_seasmax_nsw_@@&STATION=CESM1_MSR&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM annual seasonal maximum MSR</a>,
<a href="getindices.cgi?WMO=SEAustralia/ecearth_yearly_msr_seasmax_nsw_@@&STATION=EC-Earth_MSR&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth annual seasonal maximum MSR</a>,
<a href="getindices.cgi?WMO=SEAustralia/canesm_yearly_msr_seasmax_nsw_@@&STATION=CanESM2_MSR&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 annual seasonal maximum MSR</a>,
<a href="getindices.cgi?WMO=SEAustralia/ipsl_yearly_msr_seasmax_nsw_@@&STATION=IPSL_MSR&TYPE=i&id=$EMAIL&NPERYEAR=1">IPSL annual seasonal maximum MSR</a>,
<a href="getindices.cgi?WMO=SEAustralia/wah_yearly_msr_seasmax_nsw_natural_@@&STATION=W@H_MSR_NATURAL&TYPE=i&id=$EMAIL&NPERYEAR=1">W@H annual seasonal maximum MSR natural</a>,
<a href="getindices.cgi?WMO=SEAustralia/wah_yearly_msr_seasmax_nsw_actual_@@&STATION=W@H_MSR_ACTUAL&TYPE=i&id=$EMAIL&NPERYEAR=1">W@H annual seasonal maximum MSR actual</a>,


<p><i><b>Octher potential drivers</b></i><br> 
IOD: <a href="getindices.cgi?WMO=NCDCData/dmi_ersst&STATION=DMI_ERSST&TYPE=i&id=$EMAIL">ERSSTv5 obs</a>, <a href="getindices.cgi?WMO=SEAustralia/dmi_ecearth_%%&STATION=DMI_EC-Earth&TYPE=i&id=$EMAIL">EC-Earth</a>, <a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_IOD_monthly_ts_@@&STATION=DMI_CanESM2&TYPE=i&id=$EMAIL">CanESM2</a>, 
<a href="getindices.cgi?WMO=SEAustralia/CESM1-CAM5_1920-2100_IOD_monthly_ts_@@&STATION=DMI_CESM1-CAM5&TYPE=i&id=$EMAIL">CESM1-CAM5</a>, 
<a href="getindices.cgi?WMO=SEAustralia/CSIRO-Mk3-6-0_1850-2100_IOD_monthly_ts_@@&STATION=DMI_CSIRO&TYPE=i&id=$EMAIL">CSIRO Mk3.6.0</a>, 
<a href="getindices.cgi?WMO=SEAustralia/GFDL-CM3_1920-2100_IOD_monthly_ts_@@&STATION=DMI_GFDL-CM3&TYPE=i&id=$EMAIL">GFDL CM3</a>, 
<a href="getindices.cgi?WMO=SEAustralia/GFDL-ESM2M_1950-2100_IOD_monthly_ts_@@&STATION=DMI_GFDL-ESM2M&TYPE=i&id=$EMAIL">GFDL ESM2M</a>, 
<a href="getindices.cgi?WMO=SEAustralia/MPI-ESM_1850-2099_IOD_monthly_ts_@@&STATION=DMI_MPI-ESM&TYPE=i&id=$EMAIL">MPI ESM</a>.

<br>Nino3.4r:
<a href="getindices.cgi?WMO=NCDCData/ersst_nino3.4a_rel&STATION=NINO3.4_rel&TYPE=i&id=$EMAIL">ERSSTv5 obs</a>, <a href="getindices.cgi?WMO=KNMI14Data/Nino/nino34_%%%&STATION=EC-Earth23_Nino3.4&TYPE=i&NPERYEAR=12&id=$EMAIL">EC-Earth</a>, <a href="getindices.cgi?WMO=SEAustralia/CanESM2_1950-2100_Nino34_monthly_ts_@@&STATION=DMI_CanESM2&TYPE=i&id=$EMAIL">CanESM2</a>, 
<br>IOD-Nino3.4r: <a href="getindices.cgi?WMO=SEAustralia/dmi-enso_ersst&STATION=DMI-ENSO&TYPE=i&id=$EMAIL">ERSSTv5 obs</a>, <a href="getindices.cgi?WMO=SEAustralia/dmi-enso_ecearth_%%%&STATION=DMI-NINO34_EC-Earth&TYPE=i&id=$EMAIL">EC-Earth</a>, 

<br>SAM:
<a href="getindices.cgi?WMO=BASData/bas_sam&STATION=SAM_BAS&TYPE=i&id=$EMAIL">BAS</a>,
<a href="getindices.cgi?WMO=NCEPNCAR40/sam_ncepncar&STATION=SAM_NCEPNCAR&TYPE=i&id=$EMAIL">NCEPNCAR R1</a>,
<a href="getindices.cgi?WMO=ERA5/era5_sam&STATION=SAM_ERA5&TYPE=i&id=$EMAIL">ERA5</a>,
<a href="getindices.cgi?WMO=CMIP5/knmi14_psl_Amon_ECEARTH23_rcp85_0-360E_-40N_n____-knmi14_psl_Amon_ECEARTH23_rcp85_0-360E_-65N_n_%%&STATION=EC-Earth_SAM&TYPE=i&id=$EMAIL">EC-Earth</a>.

<br>Ozone hole:
<a href="getindices.cgi?WMO=TEMISData/ozon_mo&STATION=lost_ozone&TYPE=i&id=$EMAIL">lost ozone</a>

<br>
<p><i><b>GMST timeseries</b></i><br> 
<a href="getindices.cgi?WMO=SEAustralia/gmst_cesm_yr_ce&STATION=CESM1_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">CESM annual GMST</a>,
<a href="getindices.cgi?WMO=SEAustralia/gmst_ecearth_yr&STATION=ECEARTH_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">ECEarth annual GMST</a>,
<a href="getindices.cgi?WMO=SEAustralia/gmst_ipsl&STATION=IPSL_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">IPSL annual GMST</a>,
<a href="getindices.cgi?WMO=SEAustralia/gmst_canesm2_yr&STATION=CANESM2_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">CanESM2 annual GMST</a>,
<a href="getindices.cgi?WMO=SEAustralia/gmst_gfdl-cm3_yr&STATION=GFDL-CM3_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-CM3 annual GMST</a>,
<a href="getindices.cgi?WMO=SEAustralia/gmst_gfdl-esm2m_yr&STATION=GFDL-ESM2M_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">GFDL-ESM2M annual GMST</a>,
<a href="getindices.cgi?WMO=SEAustralia/gmst_mpi-esm_yr&STATION=MPI-ESM_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-ESM annual GMST</a>,
<a href="getindices.cgi?WMO=SEAustralia/gmst_csiro_yr&STATION=CSIRO_TAS&TYPE=i&id=$EMAIL&NPERYEAR=1">CSIRO-Mk3-6-0 annual GMST</a>.

EOF

. ./myvinkfoot.cgi
