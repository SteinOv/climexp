#!/bin/bash
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi

. ./myvinkhead.cgi "Select a monthly field" "Seasonal forecasts" "index,nofollow"
cat <<EOF
<form action="select.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<table class="realtable" width="100%" border=0 cellspacing=0 cellpadding=0>
<tr><th><input type="submit" class="formbuttonreverse" value="Select field"></th>
<th colspan="12">Choose a field and press this button</th></tr>
EOF

echo '<tr><th colspan=13>FULL ENSEMBLES</th>'
cat ./selectfield_seaens.html
echo '<tr><th colspan=13>ENSEMBLES MEANS</th>'
cat ./selectfield_sea.html
echo '</table>'

. ./myvinkfoot.cgi
