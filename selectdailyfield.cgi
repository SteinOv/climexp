#!/bin/bash
echo 'Content-Type: text/html'
echo
echo

DIR=`pwd`
. ./getargs.cgi

. ./myvinkhead.cgi "Select a daily field" "" "index,follow"

cat <<EOF
<form action="select.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">

<table class="realtable" width="100%" border=0 cellpadding=0 cellspacing=0>
<tr><th><input type="submit" class="formbuttonreverse" value="Select field"><th colspan="9">Choose a field and press this button (<a href="selectdailyfield2.cgi?id=$EMAIL">alternative</a>)</td></tr>
</table>
<table class="realtable" width="100%" border=0 cellpadding=0 cellspacing=0>
EOF
cat selectdailyfield_obs.html
cat <<EOF
</table>
<table class="realtable" width="100%" border=0 cellpadding=0 cellspacing=0>
EOF
cat selectdailyfield_rea.html
echo "</table>"
echo "Please contact <a href=\"mailto:oldenborgh@knmi.nl\">me</a> if you would like to have other areas of ERA5 at high resolution."

. ./myvinkfoot.cgi
