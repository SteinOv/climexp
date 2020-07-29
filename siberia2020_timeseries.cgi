#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Prolonged Siberian heat of 2020" "time series" nofollow

cat <<EOF
There are two "events"/ regions: <br>
<ul>
  <li>Verkhoyansk station: 67.57°N and 133.40E</li>
  <li>'Siberia' region: land points in 60°N - 75°N and (60 - 75N, 60°E - 180°E </li>
</ul>  

<p><i><b>Observational data</b></i><br> 
Contact: Geert Jan van Oldenborgh
<br><br>
<i>Station - Verkhoyansk: daily TX (tasmax)</i><br>
<a href="gdcntmax.cgi?id=$EMAIL&WMO=RSM00024266&STATION=VERHOJANSK">GHCN-D</a>
<p>
<i>Region - Siberia: monthly T (tas)</a></i><br>
<a href="get_index.cgi?email=$EMAIL&field=giss_temp_250&gridpoints=false&intertype=nearest&lat1=60&lat2=75&lon1=60&lon2=180&masktype=5lan&minfac=30">GISTEMP 250km</a>,
<a href="get_index.cgi?email=$EMAIL&field=era5_t2m_e&gridpoints=false&intertype=nearest&lat1=60&lat2=75&lon1=60&lon2=180&masktype=5lan&minfac=30">ERA5</a>.

<p><i><b>CMIP6 data</b></i><br> 
Contact: Mathias Hauser
<br><br>
<i>Station - Verkhoyansk: Tglob and daily TX (tasmax)</i><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_ACCESS-CM2_@@&STATION=ACCESS-CM2_Tglob_stat&TYPE=i&id=$EMAIL">ACCESS-CM2 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_ACCESS-CM2_@@&STATION=ACCESS-CM2_TX_stat&TYPE=i&id=$EMAIL">ACCESS-CM2 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_ACCESS-ESM1-5_@@&STATION=ACCESS-ESM1-5_Tglob_stat&TYPE=i&id=$EMAIL">ACCESS-ESM1-5 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_ACCESS-ESM1-5_@@&STATION=ACCESS-ESM1-5_TX_stat&TYPE=i&id=$EMAIL">ACCESS-ESM1-5 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_AWI-CM-1-1-MR_@@&STATION=AWI-CM-1-1-MR_Tglob_stat&TYPE=i&id=$EMAIL">AWI-CM-1-1-MR Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_AWI-CM-1-1-MR_@@&STATION=AWI-CM-1-1-MR_TX_stat&TYPE=i&id=$EMAIL">AWI-CM-1-1-MR TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_BCC-CSM2-MR_@@&STATION=BCC-CSM2-MR_Tglob_stat&TYPE=i&id=$EMAIL">BCC-CSM2-MR Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_BCC-CSM2-MR_@@&STATION=BCC-CSM2-MR_TX_stat&TYPE=i&id=$EMAIL">BCC-CSM2-MR TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_CanESM5_@@&STATION=CanESM5_Tglob_stat&TYPE=i&id=$EMAIL">CanESM5 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_CanESM5_@@&STATION=CanESM5_TX_stat&TYPE=i&id=$EMAIL">CanESM5 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_CMCC-CM2-SR5_@@&STATION=CMCC-CM2-SR5_Tglob_stat&TYPE=i&id=$EMAIL">CMCC-CM2-SR5 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_CMCC-CM2-SR5_@@&STATION=CMCC-CM2-SR5_TX_stat&TYPE=i&id=$EMAIL">CMCC-CM2-SR5 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_CNRM-CM6-1-HR_@@&STATION=CNRM-CM6-1-HR_Tglob_stat&TYPE=i&id=$EMAIL">CNRM-CM6-1-HR Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_CNRM-CM6-1-HR_@@&STATION=CNRM-CM6-1-HR_TX_stat&TYPE=i&id=$EMAIL">CNRM-CM6-1-HR TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_CNRM-CM6-1_@@&STATION=CNRM-CM6-1_Tglob_stat&TYPE=i&id=$EMAIL">CNRM-CM6-1 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_CNRM-CM6-1_@@&STATION=CNRM-CM6-1_TX_stat&TYPE=i&id=$EMAIL">CNRM-CM6-1 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_CNRM-ESM2-1_@@&STATION=CNRM-ESM2-1_Tglob_stat&TYPE=i&id=$EMAIL">CNRM-ESM2-1 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_CNRM-ESM2-1_@@&STATION=CNRM-ESM2-1_TX_stat&TYPE=i&id=$EMAIL">CNRM-ESM2-1 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_EC-Earth3_@@&STATION=EC-Earth3_Tglob_stat&TYPE=i&id=$EMAIL">EC-Earth3 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_EC-Earth3_@@&STATION=EC-Earth3_TX_stat&TYPE=i&id=$EMAIL">EC-Earth3 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_EC-Earth3-Veg_@@&STATION=EC-Earth3-Veg_Tglob_stat&TYPE=i&id=$EMAIL">EC-Earth3-Veg Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_EC-Earth3-Veg_@@&STATION=EC-Earth3-Veg_TX_stat&TYPE=i&id=$EMAIL">EC-Earth3-Veg TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_FGOALS-g3_@@&STATION=FGOALS-g3_Tglob_stat&TYPE=i&id=$EMAIL">FGOALS-g3 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_FGOALS-g3_@@&STATION=FGOALS-g3_TX_stat&TYPE=i&id=$EMAIL">FGOALS-g3 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_GFDL-CM4_@@&STATION=GFDL-CM4_Tglob_stat&TYPE=i&id=$EMAIL">GFDL-CM4 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_GFDL-CM4_@@&STATION=GFDL-CM4_TX_stat&TYPE=i&id=$EMAIL">GFDL-CM4 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_GFDL-ESM4_@@&STATION=GFDL-ESM4_Tglob_stat&TYPE=i&id=$EMAIL">GFDL-ESM4 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_GFDL-ESM4_@@&STATION=GFDL-ESM4_TX_stat&TYPE=i&id=$EMAIL">GFDL-ESM4 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_HadGEM3-GC31-LL_@@&STATION=HadGEM3-GC31-LL_Tglob_stat&TYPE=i&id=$EMAIL">HadGEM3-GC31-LL Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_HadGEM3-GC31-LL_@@&STATION=HadGEM3-GC31-LL_TX_stat&TYPE=i&id=$EMAIL">HadGEM3-GC31-LL TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_HadGEM3-GC31-MM_@@&STATION=HadGEM3-GC31-MM_Tglob_stat&TYPE=i&id=$EMAIL">HadGEM3-GC31-MM Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_HadGEM3-GC31-MM_@@&STATION=HadGEM3-GC31-MM_TX_stat&TYPE=i&id=$EMAIL">HadGEM3-GC31-MM TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_INM-CM4-8_@@&STATION=INM-CM4-8_Tglob_stat&TYPE=i&id=$EMAIL">INM-CM4-8 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_INM-CM4-8_@@&STATION=INM-CM4-8_TX_stat&TYPE=i&id=$EMAIL">INM-CM4-8 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_INM-CM5-0_@@&STATION=INM-CM5-0_Tglob_stat&TYPE=i&id=$EMAIL">INM-CM5-0 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_INM-CM5-0_@@&STATION=INM-CM5-0_TX_stat&TYPE=i&id=$EMAIL">INM-CM5-0 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_IPSL-CM6A-LR_@@&STATION=IPSL-CM6A-LR_Tglob_stat&TYPE=i&id=$EMAIL">IPSL-CM6A-LR Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_IPSL-CM6A-LR_@@&STATION=IPSL-CM6A-LR_TX_stat&TYPE=i&id=$EMAIL">IPSL-CM6A-LR TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_KACE-1-0-G_@@&STATION=KACE-1-0-G_Tglob_stat&TYPE=i&id=$EMAIL">KACE-1-0-G Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_KACE-1-0-G_@@&STATION=KACE-1-0-G_TX_stat&TYPE=i&id=$EMAIL">KACE-1-0-G TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_MIROC6_@@&STATION=MIROC6_Tglob_stat&TYPE=i&id=$EMAIL">MIROC6 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_MIROC6_@@&STATION=MIROC6_TX_stat&TYPE=i&id=$EMAIL">MIROC6 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_MIROC-ES2L_@@&STATION=MIROC-ES2L_Tglob_stat&TYPE=i&id=$EMAIL">MIROC-ES2L Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_MIROC-ES2L_@@&STATION=MIROC-ES2L_TX_stat&TYPE=i&id=$EMAIL">MIROC-ES2L TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2-HR_Tglob_stat&TYPE=i&id=$EMAIL">MPI-ESM1-2-HR Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2-HR_TX_stat&TYPE=i&id=$EMAIL">MPI-ESM1-2-HR TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_MPI-ESM1-2-LR_@@&STATION=MPI-ESM1-2-LR_Tglob_stat&TYPE=i&id=$EMAIL">MPI-ESM1-2-LR Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_MPI-ESM1-2-LR_@@&STATION=MPI-ESM1-2-LR_TX_stat&TYPE=i&id=$EMAIL">MPI-ESM1-2-LR TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_MRI-ESM2-0_@@&STATION=MRI-ESM2-0_Tglob_stat&TYPE=i&id=$EMAIL">MRI-ESM2-0 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_MRI-ESM2-0_@@&STATION=MRI-ESM2-0_TX_stat&TYPE=i&id=$EMAIL">MRI-ESM2-0 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_NESM3_@@&STATION=NESM3_Tglob_stat&TYPE=i&id=$EMAIL">NESM3 Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_NESM3_@@&STATION=NESM3_TX_stat&TYPE=i&id=$EMAIL">NESM3 TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_NorESM2-MM_@@&STATION=NorESM2-MM_Tglob_stat&TYPE=i&id=$EMAIL">NorESM2-MM Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_NorESM2-MM_@@&STATION=NorESM2-MM_TX_stat&TYPE=i&id=$EMAIL">NorESM2-MM TX station</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_station_UKESM1-0-LL_@@&STATION=UKESM1-0-LL_Tglob_stat&TYPE=i&id=$EMAIL">UKESM1-0-LL Tglob station</a>
<a href="getindices.cgi?WMO=Siberia2020/txx_station_UKESM1-0-LL_@@&STATION=UKESM1-0-LL_TX_stat&TYPE=i&id=$EMAIL">UKESM1-0-LL TX station</a>
<br>
<br>

<i>Region - Siberia: Tglob and monthly T (tas)</i><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_ACCESS-CM2_@@&STATION=ACCESS-CM2_Tglob_region&TYPE=i&id=$EMAIL">ACCESS-CM2 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_ACCESS-CM2_@@&STATION=ACCESS-CM2_tas_region&TYPE=i&id=$EMAIL">ACCESS-CM2 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_ACCESS-ESM1-5_@@&STATION=ACCESS-ESM1-5_Tglob_region&TYPE=i&id=$EMAIL">ACCESS-ESM1-5 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_ACCESS-ESM1-5_@@&STATION=ACCESS-ESM1-5_tas_region&TYPE=i&id=$EMAIL">ACCESS-ESM1-5 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_AWI-CM-1-1-MR_@@&STATION=AWI-CM-1-1-MR_Tglob_region&TYPE=i&id=$EMAIL">AWI-CM-1-1-MR Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_AWI-CM-1-1-MR_@@&STATION=AWI-CM-1-1-MR_tas_region&TYPE=i&id=$EMAIL">AWI-CM-1-1-MR tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_BCC-CSM2-MR_@@&STATION=BCC-CSM2-MR_Tglob_region&TYPE=i&id=$EMAIL">BCC-CSM2-MR Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_BCC-CSM2-MR_@@&STATION=BCC-CSM2-MR_tas_region&TYPE=i&id=$EMAIL">BCC-CSM2-MR tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CAMS-CSM1-0_@@&STATION=CAMS-CSM1-0_Tglob_region&TYPE=i&id=$EMAIL">CAMS-CSM1-0 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CAMS-CSM1-0_@@&STATION=CAMS-CSM1-0_tas_region&TYPE=i&id=$EMAIL">CAMS-CSM1-0 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CanESM5-CanOE_@@&STATION=CanESM5-CanOE_Tglob_region&TYPE=i&id=$EMAIL">CanESM5-CanOE Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CanESM5-CanOE_@@&STATION=CanESM5-CanOE_tas_region&TYPE=i&id=$EMAIL">CanESM5-CanOE tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CanESM5_@@&STATION=CanESM5_Tglob_region&TYPE=i&id=$EMAIL">CanESM5 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CanESM5_@@&STATION=CanESM5_tas_region&TYPE=i&id=$EMAIL">CanESM5 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CESM2_@@&STATION=CESM2_Tglob_region&TYPE=i&id=$EMAIL">CESM2 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CESM2_@@&STATION=CESM2_tas_region&TYPE=i&id=$EMAIL">CESM2 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CESM2-WACCM_@@&STATION=CESM2-WACCM_Tglob_region&TYPE=i&id=$EMAIL">CESM2-WACCM Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CESM2-WACCM_@@&STATION=CESM2-WACCM_tas_region&TYPE=i&id=$EMAIL">CESM2-WACCM tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CIESM_@@&STATION=CIESM_Tglob_region&TYPE=i&id=$EMAIL">CIESM Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CIESM_@@&STATION=CIESM_tas_region&TYPE=i&id=$EMAIL">CIESM tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CMCC-CM2-SR5_@@&STATION=CMCC-CM2-SR5_Tglob_region&TYPE=i&id=$EMAIL">CMCC-CM2-SR5 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CMCC-CM2-SR5_@@&STATION=CMCC-CM2-SR5_tas_region&TYPE=i&id=$EMAIL">CMCC-CM2-SR5 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CNRM-CM6-1-HR_@@&STATION=CNRM-CM6-1-HR_Tglob_region&TYPE=i&id=$EMAIL">CNRM-CM6-1-HR Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CNRM-CM6-1-HR_@@&STATION=CNRM-CM6-1-HR_tas_region&TYPE=i&id=$EMAIL">CNRM-CM6-1-HR tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CNRM-CM6-1_@@&STATION=CNRM-CM6-1_Tglob_region&TYPE=i&id=$EMAIL">CNRM-CM6-1 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CNRM-CM6-1_@@&STATION=CNRM-CM6-1_tas_region&TYPE=i&id=$EMAIL">CNRM-CM6-1 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_CNRM-ESM2-1_@@&STATION=CNRM-ESM2-1_Tglob_region&TYPE=i&id=$EMAIL">CNRM-ESM2-1 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_CNRM-ESM2-1_@@&STATION=CNRM-ESM2-1_tas_region&TYPE=i&id=$EMAIL">CNRM-ESM2-1 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_EC-Earth3_@@&STATION=EC-Earth3_Tglob_region&TYPE=i&id=$EMAIL">EC-Earth3 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_EC-Earth3_@@&STATION=EC-Earth3_tas_region&TYPE=i&id=$EMAIL">EC-Earth3 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_EC-Earth3-Veg_@@&STATION=EC-Earth3-Veg_Tglob_region&TYPE=i&id=$EMAIL">EC-Earth3-Veg Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_EC-Earth3-Veg_@@&STATION=EC-Earth3-Veg_tas_region&TYPE=i&id=$EMAIL">EC-Earth3-Veg tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_FGOALS-f3-L_@@&STATION=FGOALS-f3-L_Tglob_region&TYPE=i&id=$EMAIL">FGOALS-f3-L Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_FGOALS-f3-L_@@&STATION=FGOALS-f3-L_tas_region&TYPE=i&id=$EMAIL">FGOALS-f3-L tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_FGOALS-g3_@@&STATION=FGOALS-g3_Tglob_region&TYPE=i&id=$EMAIL">FGOALS-g3 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_FGOALS-g3_@@&STATION=FGOALS-g3_tas_region&TYPE=i&id=$EMAIL">FGOALS-g3 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_FIO-ESM-2-0_@@&STATION=FIO-ESM-2-0_Tglob_region&TYPE=i&id=$EMAIL">FIO-ESM-2-0 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_FIO-ESM-2-0_@@&STATION=FIO-ESM-2-0_tas_region&TYPE=i&id=$EMAIL">FIO-ESM-2-0 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_GFDL-CM4_@@&STATION=GFDL-CM4_Tglob_region&TYPE=i&id=$EMAIL">GFDL-CM4 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_GFDL-CM4_@@&STATION=GFDL-CM4_tas_region&TYPE=i&id=$EMAIL">GFDL-CM4 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_GFDL-ESM4_@@&STATION=GFDL-ESM4_Tglob_region&TYPE=i&id=$EMAIL">GFDL-ESM4 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_GFDL-ESM4_@@&STATION=GFDL-ESM4_tas_region&TYPE=i&id=$EMAIL">GFDL-ESM4 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_GISS-E2-1-G_@@&STATION=GISS-E2-1-G_Tglob_region&TYPE=i&id=$EMAIL">GISS-E2-1-G Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_GISS-E2-1-G_@@&STATION=GISS-E2-1-G_tas_region&TYPE=i&id=$EMAIL">GISS-E2-1-G tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_HadGEM3-GC31-LL_@@&STATION=HadGEM3-GC31-LL_Tglob_region&TYPE=i&id=$EMAIL">HadGEM3-GC31-LL Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_HadGEM3-GC31-LL_@@&STATION=HadGEM3-GC31-LL_tas_region&TYPE=i&id=$EMAIL">HadGEM3-GC31-LL tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_HadGEM3-GC31-MM_@@&STATION=HadGEM3-GC31-MM_Tglob_region&TYPE=i&id=$EMAIL">HadGEM3-GC31-MM Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_HadGEM3-GC31-MM_@@&STATION=HadGEM3-GC31-MM_tas_region&TYPE=i&id=$EMAIL">HadGEM3-GC31-MM tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_INM-CM4-8_@@&STATION=INM-CM4-8_Tglob_region&TYPE=i&id=$EMAIL">INM-CM4-8 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_INM-CM4-8_@@&STATION=INM-CM4-8_tas_region&TYPE=i&id=$EMAIL">INM-CM4-8 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_INM-CM5-0_@@&STATION=INM-CM5-0_Tglob_region&TYPE=i&id=$EMAIL">INM-CM5-0 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_INM-CM5-0_@@&STATION=INM-CM5-0_tas_region&TYPE=i&id=$EMAIL">INM-CM5-0 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_IPSL-CM6A-LR_@@&STATION=IPSL-CM6A-LR_Tglob_region&TYPE=i&id=$EMAIL">IPSL-CM6A-LR Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_IPSL-CM6A-LR_@@&STATION=IPSL-CM6A-LR_tas_region&TYPE=i&id=$EMAIL">IPSL-CM6A-LR tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_KACE-1-0-G_@@&STATION=KACE-1-0-G_Tglob_region&TYPE=i&id=$EMAIL">KACE-1-0-G Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_KACE-1-0-G_@@&STATION=KACE-1-0-G_tas_region&TYPE=i&id=$EMAIL">KACE-1-0-G tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_MCM-UA-1-0_@@&STATION=MCM-UA-1-0_Tglob_region&TYPE=i&id=$EMAIL">MCM-UA-1-0 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_MCM-UA-1-0_@@&STATION=MCM-UA-1-0_tas_region&TYPE=i&id=$EMAIL">MCM-UA-1-0 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_MIROC6_@@&STATION=MIROC6_Tglob_region&TYPE=i&id=$EMAIL">MIROC6 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_MIROC6_@@&STATION=MIROC6_tas_region&TYPE=i&id=$EMAIL">MIROC6 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_MIROC-ES2L_@@&STATION=MIROC-ES2L_Tglob_region&TYPE=i&id=$EMAIL">MIROC-ES2L Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_MIROC-ES2L_@@&STATION=MIROC-ES2L_tas_region&TYPE=i&id=$EMAIL">MIROC-ES2L tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2-HR_Tglob_region&TYPE=i&id=$EMAIL">MPI-ESM1-2-HR Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2-HR_tas_region&TYPE=i&id=$EMAIL">MPI-ESM1-2-HR tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_MPI-ESM1-2-LR_@@&STATION=MPI-ESM1-2-LR_Tglob_region&TYPE=i&id=$EMAIL">MPI-ESM1-2-LR Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_MPI-ESM1-2-LR_@@&STATION=MPI-ESM1-2-LR_tas_region&TYPE=i&id=$EMAIL">MPI-ESM1-2-LR tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_MRI-ESM2-0_@@&STATION=MRI-ESM2-0_Tglob_region&TYPE=i&id=$EMAIL">MRI-ESM2-0 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_MRI-ESM2-0_@@&STATION=MRI-ESM2-0_tas_region&TYPE=i&id=$EMAIL">MRI-ESM2-0 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_NESM3_@@&STATION=NESM3_Tglob_region&TYPE=i&id=$EMAIL">NESM3 Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_NESM3_@@&STATION=NESM3_tas_region&TYPE=i&id=$EMAIL">NESM3 tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_NorESM2-LM_@@&STATION=NorESM2-LM_Tglob_region&TYPE=i&id=$EMAIL">NorESM2-LM Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_NorESM2-LM_@@&STATION=NorESM2-LM_tas_region&TYPE=i&id=$EMAIL">NorESM2-LM tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_NorESM2-MM_@@&STATION=NorESM2-MM_Tglob_region&TYPE=i&id=$EMAIL">NorESM2-MM Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_NorESM2-MM_@@&STATION=NorESM2-MM_tas_region&TYPE=i&id=$EMAIL">NorESM2-MM tas region</a><br>
<a href="getindices.cgi?WMO=Siberia2020/tglob_regional_UKESM1-0-LL_@@&STATION=UKESM1-0-LL_Tglob_region&TYPE=i&id=$EMAIL">UKESM1-0-LL Tglob region</a>,
<a href="getindices.cgi?WMO=Siberia2020/tas_regional_UKESM1-0-LL_@@&STATION=UKESM1-0-LL_tas_region&TYPE=i&id=$EMAIL">UKESM1-0-LL tas region</a><br>
<br>
<br>

<p><i><b>SMILE data</b></i><br> 
Contact: Flavio Lehner
<i>Station - Verkhoyansk: txx (tasmax)</i><br>
<a href="getindices.cgi?WMO=txx_station_CESM1-CAM5_@@.nc&STATION=CESM1-CAM5_txx_station&TYPE=i&id=$EMAIL">CESM1-CAM5 TXx station</a>
<a href="getindices.cgi?WMO=txx_station_CSIRO-Mk3-6-0_@@.nc&STATION=CSIRO-Mk3-6-0_txx_station&TYPE=i&id=$EMAIL">CSIRO-Mk3-6-0 TXx station</a>
<a href="getindices.cgi?WMO=txx_station_CanESM2_@@.nc&STATION=CanESM2_txx_station&TYPE=i&id=$EMAIL">CanESM2 TXx station</a>
<a href="getindices.cgi?WMO=txx_station_EC-EARTH_@@.nc&STATION=EC-EARTH_txx_station&TYPE=i&id=$EMAIL">EC-EARTH TXx station</a>
<a href="getindices.cgi?WMO=txx_station_GFDL-CM3_@@.nc&STATION=GFDL-CM3_txx_station&TYPE=i&id=$EMAIL">GFDL-CM3 TXx station</a>
<a href="getindices.cgi?WMO=txx_station_GFDL-ESM2M_@@.nc&STATION=GFDL-ESM2M_txx_station&TYPE=i&id=$EMAIL">GFDL-ESM2M TXx station</a>
<br>
<br>

<i>Region - Siberia: tas</i><br>
<a href="getindices.cgi?WMO=tas_regional_CESM1-CAM5_@@.nc&STATION=CESM1-CAM5_tas_region&TYPE=i&id=$EMAIL">CESM1-CAM5 tas region</a>
<a href="getindices.cgi?WMO=tas_regional_CSIRO-Mk3-6-0_@@.nc&STATION=CSIRO-Mk3-6-0_tas_region&TYPE=i&id=$EMAIL">CSIRO-Mk3-6-0 tas region</a>
<a href="getindices.cgi?WMO=tas_regional_CanESM2_@@.nc&STATION=CanESM2_tas_region&TYPE=i&id=$EMAIL">CanESM2 tas region</a>
<a href="getindices.cgi?WMO=tas_regional_EC-EARTH_@@.nc&STATION=EC-EARTH_tas_region&TYPE=i&id=$EMAIL">EC-EARTH tas region</a>
<a href="getindices.cgi?WMO=tas_regional_GFDL-CM3_@@.nc&STATION=GFDL-CM3_tas_region&TYPE=i&id=$EMAIL">GFDL-CM3 tas region</a>
<a href="getindices.cgi?WMO=tas_regional_GFDL-ESM2M_@@.nc&STATION=GFDL-ESM2M_tas_region&TYPE=i&id=$EMAIL">GFDL-ESM2M tas region</a>
<br>
<br>

<i>Region - Tglob</i><br>
<a href="getindices.cgi?WMO=tglob_CESM1-CAM5_@@.nc&STATION=CESM1-CAM5_tglob&TYPE=i&id=$EMAIL">CESM1-CAM5 Tglob</a>
<a href="getindices.cgi?WMO=tglob_CSIRO-Mk3-6-0_@@.nc&STATION=CSIRO-Mk3-6-0_tglob&TYPE=i&id=$EMAIL">CSIRO-Mk3-6-0 Tglob</a>
<a href="getindices.cgi?WMO=tglob_CanESM2_@@.nc&STATION=CanESM2_tglob&TYPE=i&id=$EMAIL">CanESM2 Tglob</a>
<a href="getindices.cgi?WMO=tglob_EC-EARTH_@@.nc&STATION=EC-EARTH_tglob&TYPE=i&id=$EMAIL">EC-EARTH Tglob</a>
<a href="getindices.cgi?WMO=tglob_GFDL-CM3_@@.nc&STATION=GFDL-CM3_tglob&TYPE=i&id=$EMAIL">GFDL-CM3 Tglob</a>
<a href="getindices.cgi?WMO=tglob_GFDL-ESM2M_@@.nc&STATION=GFDL-ESM2M_tglob&TYPE=i&id=$EMAIL">GFDL-ESM2M Tglob</a>
<br>
<br>


EOF

. ./myvinkfoot.cgi
