#!/bin/bash
[ -n "$myvinkfooter" ] && exit
myvinkfooter=done
if [ "$FORM_lang" = nl ]; then
    kaart=kaart
    datavandeze="Data van deze"
    tijdreeks=tijdreeks
    kaartenwereld="Kaarten wereld"
    kaarteneuropa="Kaarten Europa"
    tijdreeksen=Tijdreeksen
    meer=meer
    minder=minder
    noot="Dit is een experimentele pagina, de tijdige beschikbaarheid kan niet gegarandeerd worden.  De gegevens worden meestal tussen de 10e en de 15e van de maand bijgewerkt."
else
    kaart=map
    tijdreeks="time series"
    datavandeze="Data of this"
    kaartenwereld="World maps"
    kaarteneuropa="Europa maps"
    tijdreeksen="Time series"
    meer=more
    minder=fewer
    noot="This is an experimental page, the timely availability cannot be guaranteed. The data are usually updated between the 10th and 15th of the month."
fi
cat <<EOF
<p><div class="noot">$noot</div>
</div>
<div class="col-md-4">
EOF
if [ $FORM_lang = nl ]; then
    jaardir=jaaroverzicht_wereldweer
    seizoendir=seizoensoverzicht_wereldweer
    halfjaardir=halfjaaroverzicht_wereldweer
    maanddir=maandoverzicht_wereldweer
else
    jaardir=annual_overview_world_weather
    seizoendir=seasonal_overview_world_weather
    halfjaardir=biannual_overview_world_weather
    maanddir=monthly_overview_world_weather
fi

echo "<div class=menukopje>$tijdschaal</div>"
if [ $NPERYEAR = 12 ]; then
    echo "<div class=\"menulink\">$maand</div>"
else
    echo "<div class=\"menulink\"><a href=\"../$maanddir/index.cgi?var=$var&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=$FORM_expert&type=$FORM_type&id=$EMAIL\">$maand</a></div>"
fi
if [ $NPERYEAR = 4 ]; then
    echo "<div class=\"menulink\">$seizoen</div>"
else
    echo "<div class=\"menulink\"><a href=\"../$seizoendir/index.cgi?var=$var&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=$FORM_expert&type=$FORM_type&id=$EMAIL\">$seizoen</a></div>"
fi
if [ $NPERYEAR = 2 ]; then
    echo "<div class=\"menulink\">$halfjaar</div>"
else
    echo "<div class=\"menulink\"><a href=\"../$halfjaardir/index.cgi?var=$var&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=$FORM_expert&type=$FORM_type&id=$EMAIL\">$halfjaar</a></div>"
fi
if [ $NPERYEAR = 1 ]; then
    echo "<div class=\"menulink\">$jaar</div>"
else
    echo "<div class=\"menulink\"><a href=\"../$jaardir/index.cgi?var=$var&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=$FORM_expert&type=$FORM_type&id=$EMAIL\">$jaar</a></div>"
fi

oldvar=$var
for type in kaartwereld kaarteuropa tijdreeks
do
case "$type" in
    kaarteuropa) 
	kopje=$kaarteneuropa
	if [ "$FORM_type" = $type ]; then
	    vars="tg_eobs tx_eobs tn_eobs rr_eobs"
	else
	    vars=tg_eobs
	fi
	;;
    tijdreeks)
	kopje=$tijdreeksen
	if [ "$FORM_type" != $type ]; then
	    vars=giss_al_gl_m
	elif [ "$FORM_expert" = ja ]; then
	    vars="giss_al_gl_m giss_land tlt_gl N_ice_area S_ice_area sl_global nh_snow cnt nino5 nino2 cpc_nao snao_ncepncar nqbo maunaloa_f maunaloa_ch4 tsi sunspots"
	else
	    vars="giss_al_gl_m giss_land N_ice_area S_ice_area sl_global nh_snow cnt nino5 maunaloa_f tsi"
	fi
	;;
    *)
	kopje=$kaartenwereld
	if [ "$FORM_type" != $type ]; then
	    vars=t2m_ecmwf_w
	elif [ "$FORM_expert" = ja ]; then
	    vars="z500_ecmwf z500_ecmwf_sh slp_ecmwf t2m_ecmwf t2m_ecmwf_w tlt_uah sst_ncep_w snow_rucl icen_nsidc ices_nsidc prcp_gpcc prcp_cmorph o3nh_knmi o3sh_knmi"
	else
	    vars="slp_ecmwf t2m_ecmwf_w sst_ncep_w snow_rucl icen_nsidc ices_nsidc prcp_gpcc prcp_cmorph o3nh_knmi o3sh_knmi"
	fi
	;;
esac
###echo "vars=$vars"
echo "<div class="menukopje">$kopje</div>"
for var in $vars
do
    . ./database.cgi
    if [ $var = "$oldvar" -o \( $var = tlt_uah -a "$FORM_anomalie" = nee \) ]; then
        echo "<div class="menulink">$naam</div>"
    else
        echo "<div class="menulink"><a href=\"index.cgi?var=$var&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=$FORM_expert&type=$FORM_type&id=$EMAIL\">$naam</a></div>"
	fi
done

if [ "$FORM_type" != $type ]; then
	echo "<div class="menulink"><a href=\"index.cgi?var=$oldvar&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=nee&type=$type&id=$EMAIL\">$meer...</a></div>"    
elif [ "$FORM_type" != kaarteuropa ]; then
    if [ "$FORM_expert" = ja ]; then
	echo "<div class="menulink"><a href=\"index.cgi?var=$oldvar&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=nee&type=$FORM_type&id=$EMAIL\">$minder...</a></div>"
    else
	echo "<div class="menulink"><a href=\"index.cgi?var=$oldvar&mon1=$FORM_mon1&year1=$FORM_year1&anomalie=$FORM_anomalie&kort=$FORM_kort&expert=ja&type=$FORM_type&id=$EMAIL\">$meer...</a></div>"
    fi
fi
done

var=$oldvar
. ./database.cgi

# Deze links heb ik al jaren niet onderhouden
# Aangezien niemand het gemerkt heeft neem ik aan dat ik ze weg kan laten.
if [ 0 = 1 -a -n "$verderlezen" ]; then
    echo '<div class="menukopje">Verder lezen</div>'
    echo "<div class=\"menulink\"><a href=\"$verderlezenurl\">$verderlezen</a></div>"
fi
if [ "${FORM_var%eobs}" != "$FORM_var" ]; then
    echo "<div class=menukopje>$datavandeze $kaart</div>"
    echo "<div class=\"menulink\"><a href=\"http://eca.knmi.nl/ensembles target=_new\">via ECA&amp;D site</a></div>"
fi

if [ -n "$climexpfield" ]; then
    if [ "${FORM_var%eobs}" = "$FORM_var" ]; then
	echo "<div class=menukopje>$datavandeze $kaart</div>"
    fi
    echo "<div class=\"menulink\"><a href=\"http://climexp.knmi.nl/select.cgi?id=$EMAIL&field=$climexpfield\">via KNMI Climate Explorer</a></div>"
else
    echo "<div class=menukopje>$datavandeze $tijdreeks</div>"
    echo "<div class=\"menulink\"><a href=\"http://climexp.knmi.nl/getindices.cgi?WMO=${climexpseries}&STATION=${name}&TYPE=i&id=$EMAIL\">via KNMI Climate Explorer</a></div>"
fi

cat <<EOF
</div>
</div>
EOF
c=`echo "$REQUEST_URI" | fgrep -c '?'`
if [ $c != 0 ]; then
    rhs=`echo "$REQUEST_URI" | tr '&' '~'`
else
    rhs="${REQUEST_URI%/index.cgi}/index.cgi?var="
fi
if [ "$FORM_lang" = nl ]; then
    ext=""
#org    exp="s@/index_en.html@${rhs}~lang=en@"
    exp1="s@/index_en.html@${rhs}@"
    exp2="s@maandoverzicht_wereldweer@monthly_overview_world_weather@"
    exp5="s@jaaroverzicht_wereldweer@annual_overview_world_weather@"
    exp4="s@seizoensoverzicht_wereldweer@seasonal_overview_world_weather@"
    exp3="s@halfjaaroverzicht_wereldweer@biannual_overview_world_weather@"
else
    ext=_en
#org    exp="s@\"/\"@\"${rhs}~lang=nl\"@"
    exp1="s@\"/\"@\"${rhs}\"@"
    exp2="s@monthly_overview_world_weather@maandoverzicht_wereldweer@"
    exp5="s@annual_overview_world_weather@jaaroverzicht_wereldweer@"
    exp4="s@seasonal_overview_world_weather@seizoensoverzicht_wereldweer@"
    exp3="s@biannual_overview_world_weather@halfjaaroverzicht_wereldweer@"
fi
file=../vinklude/bottom$ext.html
[ ! -s $file ] && file=$climexp_dir/vinklude/bottom$ext.html
[ ! -s $file ] && echo "CANNOT FIND FILE $file"
cat $file
###[ -s $file ] && sed -e "$exp1" -e "$exp2" -e "$exp3" -e "$exp4" -e "$exp5" -e 's@//@/@g' $file | tr '~' '&'
cat <<EOF
</div>
</body>
</html>
EOF
