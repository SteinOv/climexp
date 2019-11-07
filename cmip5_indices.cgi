#!/bin/bash

. ./init.cgi
. ./getargs.cgi
. ./searchengine.cgi
. ./checkemail.cgi

cat <<EOF
Content-Type: text/html

EOF
. ./myvinkhead.cgi "Time series" "CMIP5 climate experiment indices" "index,nofollow"

echo "<div class=kalelink>"
cat CMIP5_disclaimer.html
cat <<EOF
The following indices are available at this moment:

<div class="alineakop">Global mean temperature (tas)</div>
<ul>
<li>RCP2.6:
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_modmean_rcp26_000&STATION=CMIP5_RCP26_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_mod_rcp26_%%%&STATION=CMIP5_RCP26_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_ens_rcp26_%%%&STATION=CMIP5_RCP26_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
<li>RCP4.5:
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_modmean_rcp45_000&STATION=CMIP5_RCP45_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_mod_rcp45_%%%&STATION=CMIP5_RCP45_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_ens_rcp45_%%%&STATION=CMIP5_RCP45_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
<li>RCP6.0:
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_modmean_rcp60_000&STATION=CMIP5_RCP60_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_mod_rcp60_%%%&STATION=CMIP5_RCP60_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_ens_rcp60_%%%&STATION=CMIP5_RCP60_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
<li>RCP8.5:
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_modmean_rcp85_000&STATION=CMIP5_RCP85_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_mod_rcp85_%%%&STATION=CMIP5_RCP85_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_ens_rcp85_%%%&STATION=CMIP5_RCP85_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
<li>historicalNat:
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_modmean_historicalNat_000&STATION=CMIP5_historicalNat_Tglobal&TYPE=i&id=$EMAIL">multi-model mean</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_mod_historicalNat_%%%&STATION=CMIP5_historicalNat_models_Tglobal&TYPE=i&id=$EMAIL">models</a>,
<a href="getindices.cgi?WMO=CMIP5/Tglobal/global_tas_Amon_ens_historicalNat_%%%&STATION=CMIP5_historicalNat_members_Tglobal&TYPE=i&id=$EMAIL">members</a>
</ul>
(<a href="CMIP5/Tglobal/index.cgi?email=$EMAIL">download all files</a>)
</div>

<div class="alineakop">Blended dlobal mean temperature (tas/tos or T2m/SST)<a href="http://www-users.york.ac.uk/~kdc3/papers/robust2015/methods.html" target="_new"><img src="images/info-i.gif" alt="more information" border="0" align="right"></a></div>
Note that the ensembles are numbered completely differently and BNU-ESM, CMCC-CESM, and bcc-csm1-1-m have been excluded following <a href="https://doi.org/10.1002/2015GL064888">Cowtan et al, GRL, 2015</a>.
<ul>
<li>RCP4.5, unmasked: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp45-xxx_ave&STATION=GMST_blended_CMIP5_RCP45_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp45-xxx_%%%&STATION=GMST_blended_CMIP5_RCP45_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_rcp45-xxx_%%%&STATION=GMST_blended_CMIP5_RCP45_ens&TYPE=i&id=$EMAIL">members</a>. 
<li>RCP4.5, masked to HadCRUT4: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp45-mxx_ave&STATION=GMST_blended_CMIP5_RCP45-masked_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp45-mxx_%%%&STATION=GMST_blended_CMIP5_RCP45-masked_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_rcp45-mxx_%%%&STATION=GMST_blended_CMIP5_RCP45-masked_ens&TYPE=i&id=$EMAIL">members</a>.
<li>RCP8.5, unmasked: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp85-xxx_ave&STATION=GMST_blended_CMIP5_RCP85_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp85-xxx_%%%&STATION=GMST_blended_CMIP5_RCP85_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_rcp85-xxx_%%%&STATION=GMST_blended_CMIP5_RCP85_ens&TYPE=i&id=$EMAIL">members</a>.
<li>RCP8.5, masked to HadCRUT4: <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp85-mxx_ave&STATION=GMST_blended_CMIP5_RCP85-masked_ave&TYPE=i&id=$EMAIL">multi-model mean</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_model_rcp85-mxx_%%%&STATION=GMST_blended_CMIP5_RCP85-masked_model&TYPE=i&id=$EMAIL">models</a>, <a href="getindices.cgi?WMO=YorkData/blended/blended_ens_rcp85-mxx_%%%&STATION=GMST_blended_CMIP5_RCP85-masked_ens&TYPE=i&id=$EMAIL">members</a>.
</ul>
(<a href="YorkData/blended/index.cgi?email=$EMAIL">download all files</a>).
EOF


. ./myvinkfoot.cgi
