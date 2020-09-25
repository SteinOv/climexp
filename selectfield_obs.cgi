#!/bin/bash
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi

. ./myvinkhead.cgi "Select a monthly field" "Observations" "index,follow"
cat <<EOF
<form action="select.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<table class="realtable" width="100%" border=0 cellspacing=0 cellpadding=0>
<tr><th><input type="submit" class="formbuttonreverse" value="Select field"><th colspan="2">Choose a field and press this button (<a href="selectfield_obs2.cgi?id=$EMAIL">alternative</a>)</td></tr>
EOF

sed -e "s/EMAIL/$EMAIL/" ./selectfield_obs.html

cat <<EOF
</table>
</form>
The date "now" means that I update the field whenever I need it or someone requests it.
EOF

. ./myvinkfoot.cgi
