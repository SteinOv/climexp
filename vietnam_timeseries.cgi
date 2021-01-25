#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Vietnam high precipitation study" "time series" nofollow

cat <<EOF
All time series are maximum RX15day over the land points of Vietnam.

<p><i>Time series</i><br>
Primavera GCMs: 
<a href="getindices.cgi?WMO=Vietnam/zoneyearlymaxpr15D_HighResSST_all_%%&STATION=max_RX15day_all&TYPE=i&id=$EMAIL&NPERYEAR=1">all</a>,
<a href="getindices.cgi?WMO=Vietnam/zoneyearlymaxpr15D_HighResSST_CMCC_%%&STATION=max_RX15day_CMCC&TYPE=i&id=$EMAIL&NPERYEAR=1">CMCC</a>,
<a href="getindices.cgi?WMO=Vietnam/zoneyearlymaxpr15D_HighResSST_CNRM_%%&STATION=max_RX15day_CNRM&TYPE=i&id=$EMAIL&NPERYEAR=1">CNRM</a>,
<a href="getindices.cgi?WMO=Vietnam/zoneyearlymaxpr15D_HighResSST_EC-Earth_%%&STATION=max_RX15day_EC-Earth&TYPE=i&id=$EMAIL&NPERYEAR=1">EC-Earth</a>,
<a href="getindices.cgi?WMO=Vietnam/zoneyearlymaxpr15D_HighResSST_ECMWF_%%&STATION=max_RX15day_ECMWF&TYPE=i&id=$EMAIL&NPERYEAR=1">ECMWF</a>,
<a href="getindices.cgi?WMO=Vietnam/zoneyearlymaxpr15D_HighResSST_HadGEM_%%&STATION=max_RX15day_HadGEM&TYPE=i&id=$EMAIL&NPERYEAR=1">HadGEM</a>,
<a href="getindices.cgi?WMO=Vietnam/zoneyearlymaxpr15D_HighResSST_MPI_%%&STATION=max_RX15day_MPI&TYPE=i&id=$EMAIL&NPERYEAR=1">MPI</a>.

<p><i>Fields</i><br>
Primavera GCMs: 
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_all_%%.nc">all</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_CMCC_%%.nc">CMCC</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_CNRM_%%.nc&STATION=max_RX15day_CNRM&TYPE=i&id=$EMAIL&NPERYEAR=1">CNRM</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_EC-Earth_%%.nc">EC-Earth</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_ECMWF_%%.nc">ECMWF</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_HadGEM_%%.nc">HadGEM</a>,
<a href="select.cgi?field=Vietnam/maxyearlypr15D_HighResSST_MPI_%%.nc">MPI</a>.
EOF

. ./myvinkfoot.cgi
