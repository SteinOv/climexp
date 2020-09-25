#!/bin/bash
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi

. ./myvinkhead.cgi "Select a monthly field" "CORDEX scenario runs" "index,nofollow"

cat <<EOF

Please note that all scenario runs also include the historical part (1951-2005).

<form action="select.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<table class="realtable" width="100%" border=0 cellspacing=0 cellpadding=0>
<tr valign="baseline"><th><input type="submit" class="formbuttonreverse" value="Select field">
<th colspan="13">Choose a field and press this button.
EOF

sed -e "s/EMAIL/$EMAIL/" ./selectfield_cordex.html
echo '</table>'

. ./myvinkfoot.cgi
