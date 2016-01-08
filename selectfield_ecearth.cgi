#!/bin/sh
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi

. ./myvinkhead.cgi "Select a monthly field" "EC-Earth scenario runs" "index,nofollow"

cat <<EOF
<div class="kalelink">
</div>
<form action="select.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<table class="realtable" width="100%" border=0 cellspacing=0 cellpadding=0>
<tr valign="baseline"><th colspan="14"><input type="submit" class="formbutton" value="Select field">
Choose a field and press this button</td></tr>
<tr><th>EC-Earth 2.3<br>RCP8.5
<th>tas
<th>tas<br>min
<th>tas<br>max
<th>pr
<th>evsp<br>sbl
<th>pme
<th>ssr
<th>uas
<th>vas
<th>psl
<tr><td>KNMI'14 (16)
<td><input type=radio class=formradio name=field value=knmi14_tas_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_tasmin_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_tasmax_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_pr_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_evspsbl_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_pme_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_ssr_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_uas_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_vas_Amon_ECEARTH23_rcp85>
<td><input type=radio class=formradio name=field value=knmi14_psl_Amon_ECEARTH23_rcp85>

</table>
</form>
<div class=alineakop>Monthly series</div>
<p><a href="getindices.cgi?WMO=KNMI14Data/Tglobal/iknmi14_tas_Amon_ECEARTH23_rcp85_0-360E_-90-90N_n_su_%%&STATION=Tglobal_EC-Earth23&TYPE=t&NPERYEAR=12&id=$EMAIL">Global mean temperature</a>,
<a href="getindices.cgi?WMO=KNMI14Data/Tglobal/iknmi14_tas_Amon_ECEARTH23_rcp85_0-360E_-90-90N_n_5lan_su_%%&STATION=Tland_EC-Earth23&TYPE=t&NPERYEAR=12&id=$EMAIL">land only</a>.
<p><a href="getindices.cgi?WMO=KNMI14Data/Nino/nino34_%%%&STATION=EC-Earth23_Nino3.4&TYPE=i&NPERYEAR=12&id=$EMAIL">Ni&ntilde;o3.4 (detrended)</a>,

<div class=alineakop>Dailly series</div>
<p><a href="getindices.cgi?WMO=KNMI14Data/Tdebilt/tas_day_ECEARTH23_rcp85_%%_18600101-21001231_52N_5E&STATION=Tdebilt_EC-Earth23&TYPE=t&NPERYEAR=366&id=$EMAIL">temperature at 52&deg;N, 5&deg;E</a>,
<p><a href="getindices.cgi?WMO=KNMI14Data/Pcumbria/pr_day_ECEARTH23_rcp85_%%_18600101-21001231_NEngland&STATION=P_NEngland_EC-Earth23&TYPE=p&NPERYEAR=366&id=$EMAIL">precipitation in Northern England</a>,
<p><a href="getindices.cgi?WMO=KNMI14Data/Pboulder/pr_day_ECEARTH23_rcp85_%%_18600101-21001231_Boulder&STATION=P_Boulder_EC-Earth23&TYPE=p&NPERYEAR=366&id=$EMAIL">precipitation in Boulder, Colorado, USA</a>.
EOF

. ./myvinkfoot.cgi
