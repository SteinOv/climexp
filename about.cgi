#!/bin/bash
echo "Content-Type: text/html"
echo
echo

. ./getargs.cgi
. ./myvinkhead.cgi "About the Climate Explorer" ""

cat <<EOF
<p>The KNMI Climate Explorer is a web application to analysis climate data statistically. It contains more than 10 TB of climate data and dozens of analysis tools. It is part of the WMO Regional Climate Centre at KNMI.

<p>This is scientific tool. Please verify yourself that the data you use is good enough for your purpose, and <a href="contact.cgi?id=$EMAIL">report errors back</a>. In publications the original data source should be cited, a link to a web page describing the data is always provided.

<p>Much of the observational data is updated monthly, part of the daily data is updated every day.  Other data is updated when needed. If you have an interesting dataset that you want to publish on the Climate Explorer please send me the URL of a <a href="http://cf-pcmdi.llnl.gov/" target="_new">CF-compliant netcdf file</a> and a short description.

<p>The code of the Climate Explorer itself is freely available on <a href="https://gitlab.com/KNMI-OSS/climexp">GitLab</a>.
EOF

. ./myvinkfoot.cgi

