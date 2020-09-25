#!/bin/bash
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi

. ./myvinkhead.cgi "Select a monthly field" "CMIP6 scenario runs" "index,nofollow"

cat <<EOF
<div class="kalelink">
First batch of CNIP6 runs downlaoded November 2019, will be updated shortly.
<p>
<form action="select.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<table class="realtable" width="100%" border=0 cellspacing=0 cellpadding=0>
<tr valign="baseline"><th><input type="submit" class="formbuttonreverse" value="Select field">
<th colspan="12">Choose a field and press this button
EOF

cat selectfield_cmip6.html

cat <<EOF
<tr><th colspan=8>Forcings
<tr><th>
<a href="http://solarisheppa.geomar.de/cmip6">Solar</a>
</th><td>
<a href="getindices.cgi?WMO=CMIP6/forcing/cmip6_tsi&STATION=CMIP6_TSI&TYPE=i&id=$EMAIL">TSI</a>
</td><td>
<a href="getindices.cgi?WMO=CMIP6/forcing/cmip6_f107&STATION=CMIP6_10.7mm&TYPE=i&id=$EMAIL">F10.7</a>
</td><td>
<a href="getindices.cgi?WMO=CMIP6/forcing/cmip6_ap&STATION=CMIP6_Ap&TYPE=i&id=$EMAIL">Ap</a>
</td><td>
<a href="getindices.cgi?WMO=CMIP6/forcing/cmip6_kp&STATION=CMIP6_Kp&TYPE=i&id=$EMAIL">Kp</a>
</td></tr>
</table>
</form>
</div>
EOF

. ./myvinkfoot.cgi
