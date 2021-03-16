#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Vietnam high precipitation study" "time series" nofollow

cat <<EOF
Time series, maximum over the land points of (Central) Vietnam.

<p><b>RX15day</b>

<p><a href="notyetready">observations</a>

<p>Primavera GCMs: 
<a href="getindices.cgi?WMO=Vietnam/PRIMAVERA/Rx15day_PRIMAVERA_all_1950-2014_%%&STATION=max_RX15day_PRIMAVERA&TYPE=i&id=$EMAIL&NPERYEAR=1">all</a>,
<a href="getindices.cgi?WMO=Vietnam/PRIMAVERA/Rx15day_PRIMAVERA_CMCC-CM2-VHR4_1950-2014_%%&STATION=max_RX15day_CMCC-CM2-VHR4&TYPE=i&id=$EMAIL&NPERYEAR=1">CMCC-CM2-VHR4</a>,
<a href="getindices.cgi?WMO=Vietnam/PRIMAVERA/Rx15day_PRIMAVERA_CNRM-CM6-1-HR_1950-2014_%%&STATION=max_RX15day_CNRM-CM6-1-HR&TYPE=i&id=$EMAIL&NPERYEAR=1">CNRM-CM6-1-HR</a>,
<a href="getindices.cgi?WMO=Vietnam/PRIMAVERA/Rx15day_PRIMAVERA_EC-Earth3P-HR_1950-2014_%%&STATION=max_RX15day_EC-Earth3P-HR&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth3P-HR</a>,
<a href="getindices.cgi?WMO=Vietnam/PRIMAVERA/Rx15day_PRIMAVERA_ECMWF-IFS-HR_1950-2014_%%&STATION=max_RX15day_ECMWF-IFS-HR&TYPE=i&id=$EMAIL&NPERYEAR=1">ECMWF-IFS-HR</a>,
<a href="getindices.cgi?WMO=Vietnam/PRIMAVERA/Rx15day_PRIMAVERA_HadGEM3-GC31-HM_1950-2014_%%&STATION=max_RX15day_HadGEM3-GC31-HM&TYPE=i&id=$EMAIL&NPERYEAR=1">HadGEM3-GC31-HM</a>,
<a href="getindices.cgi?WMO=Vietnam/PRIMAVERA/Rx15day_PRIMAVERA_MPI-ESM1-2-XR_1950-2014_%%&STATION=max_RX15day_MPI-ESM1-2-XR&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-ESM1-2-XR</a>.

<p>CORDEX East Asia:
<a href="getindices.cgi?WMO=Vietnam/Rx15day/Rx15day_EAS-22_all_%%&STATION=max_RX15day_EAS-22&TYPE=i&id=$EMAIL&NPERYEAR=1">all</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx15day/Rx15day_EAS-22_MOHC-HadGEM2-ES_r1i1p1_GERICS-REMO2015_1970-2099_ANN_nscen_timeseries&STATION=max_RX15day_HadGEM2_REMO2015&TYPE=i&id=$EMAIL&NPERYEAR=1">MOHC-HadGEM2-ES_GERICS-REMO2015</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx15day/Rx15day_EAS-22_MOHC-HadGEM2-ES_r1i1p1_ICTP-RegCM4-4_1970-2099_ANN_nscen_timeseries&STATION=max_RX15day_HadGEM2_RegCM4-4&TYPE=i&id=$EMAIL&NPERYEAR=1">MOHC-HadGEM2-ES_ICTP-RegCM4-4</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx15day/Rx15day_EAS-22_MPI-M-MPI-ESM-LR_r1i1p1_GERICS-REMO2015_1970-2099_ANN_nscen_timeseries&STATION=max_RX15day_MPI-ESM-LR_REMO2015&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-M-MPI-ESM-LR_GERICS-REMO2015</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx15day/Rx15day_EAS-22_MPI-M-MPI-ESM-MR_r1i1p1_ICTP-RegCM4-4_1980-2099_ANN_nscen_timeseries&STATION=max_RX15day_MPI-ESM-MR_RegCM4-4&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-M-MPI-ESM-MR_ICTP-RegCM4-4</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx15day/Rx15day_EAS-22_NCC-NorESM1-M_r1i1p1_GERICS-REMO2015_1970-2099_ANN_nscen_timeseries&STATION=max_RX15day_NCC-NorESM1-M_REMO2015&TYPE=i&id=$EMAIL&NPERYEAR=1">NCC-NorESM1-M_GERICS-REMO2015</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx15day/Rx15day_EAS-22_NCC-NorESM1-M_r1i1p1_ICTP-RegCM4-4_1970-2099_ANN_nscen_timeseries&STATION=max_RX15day_NCC-NorESM1-M__RegCM4-4&TYPE=i&id=$EMAIL&NPERYEAR=1">NCC-NorESM1-M_ICTP-RegCM4-4</a>.

<p><i>Fields</i><br>
Primavera GCMs: 
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_all_%%.nc&id=$EMAIL">all</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_CMCC_%%.nc&id=$EMAIL">CMCC</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_CNRM_%%.nc&id=$EMAIL">CNRM</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_EC-Earth_%%.nc&id=$EMAIL">EC-Earth</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_ECMWF_%%.nc&id=$EMAIL">ECMWF</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_HadGEM_%%.nc&id=$EMAIL">HadGEM</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_MPI_%%.nc&id=$EMAIL">MPI</a>.

<p><b>Rx7day</b>

<p><a href="notyetready">observations</a>

<p>Primavera GCMs: 
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_PRIMAVERA_all_1950-2014_%%&STATION=max_Rx7day_PRIMAVERA&TYPE=i&id=$EMAIL&NPERYEAR=1">all</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_PRIMAVERA_CMCC-CM2-VHR4_1950-2014_%%&STATION=max_Rx7day_CMCC-CM2-VHR4&TYPE=i&id=$EMAIL&NPERYEAR=1">CMCC-CM2-VHR4</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_PRIMAVERA_CNRM-CM6-1-HR_1950-2014_%%&STATION=max_Rx7day_CNRM-CM6-1-HR&TYPE=i&id=$EMAIL&NPERYEAR=1">CNRM-CM6-1-HR</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_PRIMAVERA_EC-Earth3P-HR_1950-2014_%%&STATION=max_Rx7day_EC-Earth3P-HR&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth3P-HR</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_PRIMAVERA_ECMWF-IFS-HR_1950-2014_%%&STATION=max_Rx7day_ECMWF-IFS-HR&TYPE=i&id=$EMAIL&NPERYEAR=1">ECMWF-IFS-HR</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_PRIMAVERA_HadGEM3-GC31-HM_1950-2014_%%&STATION=max_Rx7day_HadGEM3-GC31-HM&TYPE=i&id=$EMAIL&NPERYEAR=1">HadGEM3-GC31-HM</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_PRIMAVERA_MPI-ESM1-2-XR_1950-2014_%%&STATION=max_Rx7day_MPI-ESM1-2-XR&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-ESM1-2-XR</a>.

<p>CORDEX East Asia:
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_EAS-22_all_%%&STATION=max_Rx7day_EAS-22&TYPE=i&id=$EMAIL&NPERYEAR=1">all</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_EAS-22_MOHC-HadGEM2-ES_r1i1p1_GERICS-REMO2015_1970-2099_ANN_nscen_timeseries&STATION=max_Rx7day_HadGEM2_REMO2015&TYPE=i&id=$EMAIL&NPERYEAR=1">MOHC-HadGEM2-ES_GERICS-REMO2015</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_EAS-22_MOHC-HadGEM2-ES_r1i1p1_ICTP-RegCM4-4_1970-2099_ANN_nscen_timeseries&STATION=max_Rx7day_HadGEM2_RegCM4-4&TYPE=i&id=$EMAIL&NPERYEAR=1">MOHC-HadGEM2-ES_ICTP-RegCM4-4</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_EAS-22_MPI-M-MPI-ESM-LR_r1i1p1_GERICS-REMO2015_1970-2099_ANN_nscen_timeseries&STATION=max_Rx7day_MPI-ESM-LR_REMO2015&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-M-MPI-ESM-LR_GERICS-REMO2015</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_EAS-22_MPI-M-MPI-ESM-MR_r1i1p1_ICTP-RegCM4-4_1980-2099_ANN_nscen_timeseries&STATION=max_Rx7day_MPI-ESM-MR_RegCM4-4&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI-M-MPI-ESM-MR_ICTP-RegCM4-4</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_EAS-22_NCC-NorESM1-M_r1i1p1_GERICS-REMO2015_1970-2099_ANN_nscen_timeseries&STATION=max_Rx7day_NCC-NorESM1-M_REMO2015&TYPE=i&id=$EMAIL&NPERYEAR=1">NCC-NorESM1-M_GERICS-REMO2015</a>,
<a href="getindices.cgi?WMO=Vietnam/Rx7day/Rx7day_EAS-22_NCC-NorESM1-M_r1i1p1_ICTP-RegCM4-4_1970-2099_ANN_nscen_timeseries&STATION=max_Rx7day_NCC-NorESM1-M__RegCM4-4&TYPE=i&id=$EMAIL&NPERYEAR=1">NCC-NorESM1-M_ICTP-RegCM4-4</a>.

EOF

. ./myvinkfoot.cgi
