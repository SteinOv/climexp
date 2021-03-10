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
<a href="getindices.cgi?WMO=Baltic/Estonia_MPI-GE_@@&STATION=MPI-GE_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-GE</a>,
<a href="getindices.cgi?WMO=Baltic/Estonia_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-ESM1.2</a>,
<a href="getindices.cgi?WMO=Baltic/Estonia_NorESM2-LM_@@&STATION=NorESM2_Estonia&TYPE=t&id=$EMAIL&NPERYEAR=12">NorESM2</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_ACCESS1-3_rcp45_Estonia_su_%%%&STATION=ACCESS1-3_Estonia&TYPE=t&id=&NPERYEAR=12">ACCESS1-3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_CMCC-CMS_rcp45_Estonia_su_%%%&STATION=CMCC-CMS_Estonia&TYPE=t&id=&NPERYEAR=12">CMCC-CMS</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_CSIRO-Mk3-6-0_rcp45_Estonia_su_%%%&STATION=CSIRO-Mk3-6-0_Estonia&TYPE=t&id=&NPERYEAR=12">CSIRO-Mk3-6-0</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-H-CC_p1_rcp45_Estonia_su_%%%&STATION=GISS-E2-H-CC_p1_Estonia&TYPE=t&id=&NPERYEAR=12">GISS-E2-H-CC_p1</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-R_p1_rcp45_Estonia_su_%%%&STATION=GISS-E2-R_p1_Estonia&TYPE=t&id=&NPERYEAR=12">GISS-E2-R_p1</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-R_p2_rcp45_Estonia_su_%%%&STATION=GISS-E2-R_p2_Estonia&TYPE=t&id=&NPERYEAR=12">GISS-E2-R_p2</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-R_p3_rcp45_Estonia_su_%%%&STATION=GISS-E2-R_p3_Estonia&TYPE=t&id=&NPERYEAR=12">GISS-E2-R_p3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_IPSL-CM5A-MR_rcp45_Estonia_su_%%%&STATION=IPSL-CM5A-MR_Estonia&TYPE=t&id=&NPERYEAR=12">IPSL-CM5A-MR</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_MIROC5_rcp45_Estonia_su_%%%&STATION=MIROC5_Estonia&TYPE=t&id=&NPERYEAR=12">MIROC5</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_MRI-CGCM3_rcp45_Estonia_su_%%%&STATION=MRI-CGCM3_Estonia&TYPE=t&id=&NPERYEAR=12">MRI-CGCM3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_bcc-csm1-1-m_rcp45_Estonia_su_%%%&STATION=bcc-csm1-1-m_Estonia&TYPE=t&id=&NPERYEAR=12">bcc-csm1-1-m</a>.

<p><i>Latvia</i><br>
<a href="getindices.cgi?WMO=Baltic/avg_nov_temp_LV&STATION=November_T_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Latvia_su_%%%&STATION=HadGEM3A_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_Latvia_su_%%&STATION=EC-Earth23_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth2.3</a>,
<a href="getindices.cgi?WMO=Baltic/Latvia/tas_Latvia_1970-2050_weighted_%%%&STATION=EC-Earth3_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth3</a>,
<a href="getindices.cgi?WMO=Baltic/Latvia_MPI-GE_@@&STATION=MPI-GE_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-GE</a>,
<a href="getindices.cgi?WMO=Baltic/Latvia_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-ESM1.2</a>,
<a href="getindices.cgi?WMO=Baltic/Latvia_NorESM2-LM_@@&STATION=NorESM2_Latvia&TYPE=t&id=$EMAIL&NPERYEAR=12">NorESM2</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_ACCESS1-3_rcp45_Latvia_su_%%%&STATION=ACCESS1-3_Latvia&TYPE=t&id=&NPERYEAR=12">ACCESS1-3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_CSIRO-Mk3-6-0_rcp45_Latvia_su_%%%&STATION=CSIRO-Mk3-6-0_Latvia&TYPE=t&id=&NPERYEAR=12">CSIRO-Mk3-6-0</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-R_p3_rcp45_Latvia_su_%%%&STATION=GISS-E2-R_p3_Latvia&TYPE=t&id=&NPERYEAR=12">GISS-E2-R_p3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_IPSL-CM5A-MR_rcp45_Latvia_su_%%%&STATION=IPSL-CM5A-MR_Latvia&TYPE=t&id=&NPERYEAR=12">IPSL-CM5A-MR</a>.

<p><i>Sweden</i><br>
<a href="getindices.cgi?WMO=Baltic/sweYrlyAnoms_monnr_11&STATION=November_T_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Sweden_su_%%%&STATION=HadGEM3A_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_Sweden_su_%%&STATION=EC-Earth23_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth2.3</a>,
<a href="getindices.cgi?WMO=Baltic/Sweden/tas_Sweden_1970-2050_weighted_%%%&STATION=EC-Earth3_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth3</a>,
<a href="getindices.cgi?WMO=Baltic/Sweden_MPI-GE_@@&STATION=MPI-GE_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-GE</a>,
<a href="getindices.cgi?WMO=Baltic/Sweden_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-ESM1.2</a>,
<a href="getindices.cgi?WMO=Baltic/Sweden_NorESM2-LM_@@&STATION=NorESM2_Sweden&TYPE=t&id=$EMAIL&NPERYEAR=12">NorESM2</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_ACCESS1-3_rcp45_Sweden_su_%%%&STATION=ACCESS1-3_Sweden&TYPE=t&id=&NPERYEAR=12">ACCESS1-3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_CESM1-CAM5_rcp45_Sweden_su_%%%&STATION=CESM1-CAM5_Sweden&TYPE=t&id=&NPERYEAR=12">CESM1-CAM5</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-R_p1_rcp45_Sweden_su_%%%&STATION=GISS-E2-R_p1_Sweden&TYPE=t&id=&NPERYEAR=12">GISS-E2-R_p1</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-R_p2_rcp45_Sweden_su_%%%&STATION=GISS-E2-R_p2_Sweden&TYPE=t&id=&NPERYEAR=12">GISS-E2-R_p2</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-R_p3_rcp45_Sweden_su_%%%&STATION=GISS-E2-R_p3_Sweden&TYPE=t&id=&NPERYEAR=12">GISS-E2-R_p3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_IPSL-CM5A-MR_rcp45_Sweden_su_%%%&STATION=IPSL-CM5A-MR_Sweden&TYPE=t&id=&NPERYEAR=12">IPSL-CM5A-MR</a>.

<p><i>Denmark</i><br>
<a href="getindices.cgi?WMO=Baltic/DMI_november_1874-2020&STATION=November_T_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=1">observations</a>,
<a href="getindices.cgi?WMO=Baltic/eucleia_tas_Amon_HadGEM3-A-N216_historical_Denmark_su_%%%&STATION=HadGEM3A_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">HadGEM3-A</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_Denmark_su_%%&STATION=EC-Earth23_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth2.3</a>,
<a href="getindices.cgi?WMO=Baltic/knmi14_t2m_mon_RACMO22E_rcp85_Denmark_su_%%&STATION=RACMO22_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">RACMO2.2E</a>,
<a href="getindices.cgi?WMO=Baltic/Denmark/tas_Denmark_1970-2050_weighted_%%%&STATION=EC-Earth3_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">EC-Earth3</a>,
<a href="getindices.cgi?WMO=Baltic/MPI-ESM_Denmark_@@&STATION=MPI-ESM_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-ESM</a>,
<a href="getindices.cgi?WMO=Baltic/Denmark_MPI-GE_@@&STATION=MPI-GE_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-GE</a>,
<a href="getindices.cgi?WMO=Baltic/Denmark_MPI-ESM1-2-HR_@@&STATION=MPI-ESM1-2_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-ESM1.2</a>,
<a href="getindices.cgi?WMO=Baltic/Denmark_NorESM2-LM_@@&STATION=NorESM2_Denmark&TYPE=t&id=$EMAIL&NPERYEAR=12">NorESM2</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-H-CC_p1_rcp45_Denmark_su_%%%&STATION=GISS-E2-H-CC_p1_Denmark&TYPE=t&id=&NPERYEAR=12">GISS-E2-H-CC_p1</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-H_p1_rcp45_Denmark_su_%%%&STATION=GISS-E2-H_p1_Denmark&TYPE=t&id=&NPERYEAR=12">GISS-E2-H_p1</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-H_p2_rcp45_Denmark_su_%%%&STATION=GISS-E2-H_p2_Denmark&TYPE=t&id=&NPERYEAR=12">GISS-E2-H_p2</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_GISS-E2-H_p3_rcp45_Denmark_su_%%%&STATION=GISS-E2-H_p3_Denmark&TYPE=t&id=&NPERYEAR=12">GISS-E2-H_p3</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_IPSL-CM5A-MR_rcp45_Denmark_su_%%%&STATION=IPSL-CM5A-MR_Denmark&TYPE=t&id=&NPERYEAR=12">IPSL-CM5A-MR</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_MIROC5_rcp45_Denmark_su_%%%&STATION=MIROC5_Denmark&TYPE=t&id=&NPERYEAR=12">MIROC5</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_MPI-ESM-LR_rcp45_Denmark_su_%%%&STATION=MPI-ESM-LR_Denmark&TYPE=t&id=&NPERYEAR=12">MPI-ESM-LR</a>,
<a href="getindices.cgi?WMO=Baltic/icmip5_tas_Amon_MPI-ESM-MR_rcp45_Denmark_su_%%%&STATION=MPI-ESM-MR_Denmark&TYPE=t&id=&NPERYEAR=12">MPI-ESM-MR</a>.

<p><i>Covariates</i><br>
<a href="getindices.cgi?WMO=NASAData/giss_al_gl_a_4yrlo&STATION=smoothed_GMST&TYPE=i&id=$EMAIL">smoothed observed GMST (4-yr running mean GISTEMP)</a>,
annual mean ensemble mean 
<a href="getindices.cgi?WMO=Baltic/knmi14_tas_Amon_ECEARTH23_rcp85_0-360E_-90-90N_n_su_mean_mean1_anom&STATION=EC-Earth2.3_GMST&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth2.3 GMST</a>,
<a href="getindices.cgi?WMO=Baltic/tas_historicalssp119_1970-2050_ensmean&STATION=EC-Earth3_GMST&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth3 GMST</a>,
<a href="getindices.cgi?WMO=Baltic/GMST_MPI-GE&STATION=MPI-GE_GMST&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-GE</a>,
<a href="getindices.cgi?WMO=Baltic/GMST_MPI-ESM1-2-HR&STATION=MPI-ESM1-2_GMST&TYPE=t&id=$EMAIL&NPERYEAR=12">MPI-ESM1.2</a>,
<a href="getindices.cgi?WMO=Baltic/GMST_NorESM2-LM&STATION=NorESM2_GMST&TYPE=t&id=$EMAIL&NPERYEAR=12">NorESM2</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_ACCESS1-3_rcp45_ave_mean1&STATION=ACCESS1-3_GMST&TYPE=t&id=&NPERYEAR=1">ACCESS1-3</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_CESM1-CAM5_rcp45_ave_mean1&STATION=CESM1-CAM5_GMST&TYPE=t&id=&NPERYEAR=1">CESM1-CAM5</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_CMCC-CMS_rcp45_ave_mean1&STATION=CMCC-CMS_GMST&TYPE=t&id=&NPERYEAR=1">CMCC-CMS</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_CSIRO-Mk3-6-0_rcp45_ave_mean1&STATION=CSIRO-Mk3-6-0_GMST&TYPE=t&id=&NPERYEAR=1">CSIRO-Mk3-6-0</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_GISS-E2-H-CC_p1_rcp45_ave_mean1&STATION=GISS-E2-H-CC_p1_GMST&TYPE=t&id=&NPERYEAR=1">GISS-E2-H-CC_p1</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_GISS-E2-H_p1_rcp45_ave_mean1&STATION=GISS-E2-H_p1_GMST&TYPE=t&id=&NPERYEAR=1">GISS-E2-H_p1</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_GISS-E2-H_p2_rcp45_ave_mean1&STATION=GISS-E2-H_p2_GMST&TYPE=t&id=&NPERYEAR=1">GISS-E2-H_p2</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_GISS-E2-H_p3_rcp45_ave_mean1&STATION=GISS-E2-H_p3_GMST&TYPE=t&id=&NPERYEAR=1">GISS-E2-H_p3</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_GISS-E2-R_p1_rcp45_ave_mean1&STATION=GISS-E2-R_p1_GMST&TYPE=t&id=&NPERYEAR=1">GISS-E2-R_p1</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_GISS-E2-R_p2_rcp45_ave_mean1&STATION=GISS-E2-R_p2_GMST&TYPE=t&id=&NPERYEAR=1">GISS-E2-R_p2</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_GISS-E2-R_p3_rcp45_ave_mean1&STATION=GISS-E2-R_p3_GMST&TYPE=t&id=&NPERYEAR=1">GISS-E2-R_p3</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_IPSL-CM5A-MR_rcp45_ave_mean1&STATION=IPSL-CM5A-MR_GMST&TYPE=t&id=&NPERYEAR=1">IPSL-CM5A-MR</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_MIROC5_rcp45_ave_mean1&STATION=MIROC5_GMST&TYPE=t&id=&NPERYEAR=1">MIROC5</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_MPI-ESM-LR_rcp45_ave_mean1&STATION=MPI-ESM-LR_GMST&TYPE=t&id=&NPERYEAR=1">MPI-ESM-LR</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_MPI-ESM-MR_rcp45_ave_mean1&STATION=MPI-ESM-MR_GMST&TYPE=t&id=&NPERYEAR=1">MPI-ESM-MR</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_MRI-CGCM3_rcp45_ave_mean1&STATION=MRI-CGCM3_GMST&TYPE=t&id=&NPERYEAR=1">MRI-CGCM3</a>,
<a href="getindices.cgi?WMO=Baltic/iglobal_tas_Amon_bcc-csm1-1-m_rcp45_ave_mean1&STATION=bcc-csm1-1-m_GMST&TYPE=t&id=&NPERYEAR=1">bcc-csm1-1-m</a>.
EOF

. ./myvinkfoot.cgi
