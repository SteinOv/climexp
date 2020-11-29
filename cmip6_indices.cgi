#!/bin/bash

. ./init.cgi
. ./getargs.cgi
. ./searchengine.cgi
. ./checkemail.cgi

cat <<EOF
Content-Type: text/html

EOF
. ./myvinkhead.cgi "Time series" "CMIP6 climate experiment indices" "index,nofollow"

echo "<div class=kalelink>"
Notre that all models are weighted equally in these ensembles.
cat <<EOF
The following indices are available at this moment:

<div class="alineakop">Global mean temperature (tas)</div>
<ul>
<li>historical+SSP126:
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp126_ave&STATION=CMIP6_ssp126_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp126_%%%&STATION=CMIP6_ssp126_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_ens_ssp126_%%%&STATION=CMIP6_ssp126_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
<li>historical+SSP245:
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp245_ave&STATION=CMIP6_ssp245_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp245_%%%&STATION=CMIP6_ssp245_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_ens_ssp245_%%%&STATION=CMIP6_ssp245_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
<li>historical+SSP370:
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp370_ave&STATION=CMIP6_ssp370_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp370_%%%&STATION=CMIP6_ssp370_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_ens_ssp370_%%%&STATION=CMIP6_ssp370_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
<li>historical+SSP585:
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp585_ave&STATION=CMIP6_ssp585_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_mod_ssp585_%%%&STATION=CMIP6_ssp585_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP6/Tglobal/global_tas_mon_ens_ssp585_%%%&STATION=CMIP6_ssp585_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
</ul>
(<a href="CMIP6/Tglobal/index.cgi?email=$EMAIL">download all files</a>)
</div>

<!--
<div class="alineakop">Blended dlobal mean temperature (tas/tos or T2m/SST)<a href="http://www-users.york.ac.uk/~kdc3/papers/robust2015/methods.html" target="_new"><img src="images/info-i.gif" alt="more information" border="0" align="right"></a></div>
Note that the ensembles are numbered completely differently and BNU-ESM, CMCC-CESM, and bcc-csm1-1-m have been excluded following <a href="https://doi.org/10.1002/2015GL064888">Cowtan et al, GRL, 2015</a>.
<ul>
<li>RCP4.5, unmasked: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_ssp245-xxx_ave&STATION=GMST_blended_CMIP6_ssp245_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_ssp245-xxx_%%%&STATION=GMST_blended_CMIP6_ssp245_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_ssp245-xxx_%%%&STATION=GMST_blended_CMIP6_ssp245_ens&TYPE=i&id=$EMAIL">members</a>. 
<li>RCP4.5, masked to HadCRUT4: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_ssp245-mxx_ave&STATION=GMST_blended_CMIP6_ssp245-masked_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_ssp245-mxx_%%%&STATION=GMST_blended_CMIP6_ssp245-masked_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_ssp245-mxx_%%%&STATION=GMST_blended_CMIP6_ssp245-masked_ens&TYPE=i&id=$EMAIL">members</a>.
<li>RCP8.5, unmasked: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_historical+ssp585-xxx_ave&STATION=GMST_blended_CMIP6_historical+ssp585_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_historical+ssp585-xxx_%%%&STATION=GMST_blended_CMIP6_historical+ssp585_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_historical+ssp585-xxx_%%%&STATION=GMST_blended_CMIP6_historical+ssp585_ens&TYPE=i&id=$EMAIL">members</a>.
<li>RCP8.5, masked to HadCRUT4: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_historical+ssp585-mxx_ave&STATION=GMST_blended_CMIP6_historical+ssp585-masked_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_historical+ssp585-mxx_%%%&STATION=GMST_blended_CMIP6_historical+ssp585-masked_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_historical+ssp585-mxx_%%%&STATION=GMST_blended_CMIP6_historical+ssp585-masked_ens&TYPE=i&id=$EMAIL">members</a>.
</ul>
(<a href="YorkData/blended/index.cgi?email=$EMAIL">download all files</a>).
-->
EOF


. ./myvinkfoot.cgi
