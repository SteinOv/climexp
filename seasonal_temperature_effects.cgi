#!/bin/bash
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi
. ./init.cgi
. ./searchengine.cgi
. ./myvinkhead.cgi "Climate Explorer results" "Effects of El Ni&ntilde;o on world weather: all seasons" "index,follow"

cat | sed -e "s/FORM_EMAIL/$EMAIL/" <<EOF
         <p>El Ni&ntilde;o</a> affects the
         weather in large parts of the world.  The effects depend
         strongly on the location and the season.  We have studied the
         CRU TS 3.22 analyses of 2-meter
         temperature over land. As a measure of the strength of the 
         relationship we used the correlation coefficient with the 
         Ni&ntilde;o3.4 index. The square of this number gives the 
         fraction of the variance that is explained by this aspect
         of El Ni&ntilde;o.

<div class="alineakop"><a name="temperature"></a>Temperature</div>

In the temperature maps, red colours denote locations that on
average are warmer during El Ni&ntilde;o and cooler during La
Ni&ntilde;a.  Blue colours are colder during El Ni&ntilde;o and/or
warmer during La Ni&ntilde;a.  Some North America effects are
non-linear: the effect of La Ni&ntilde;a is not the opposite of the
effect of El Ni&ntilde;o.

<center>
<a href="effects/nino34_cru_tmp_25_JFM.pdf"><img src="effects/nino34_cru_tmp_25_JFM.png" alt="Relationship between El Ni&ntilde;o and temperature in January-March" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_FMA.pdf"><img src="effects/nino34_cru_tmp_25_FMA.png" alt="Relationship between El Ni&ntilde;o and temperature in February-April" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_MAM.pdf"><img src="effects/nino34_cru_tmp_25_MAM.png" alt="Relationship between El Ni&ntilde;o and temperature in March-May" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_AMJ.pdf"><img src="effects/nino34_cru_tmp_25_AMJ.png" alt="Relationship between El Ni&ntilde;o and temperature in April-June" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_MJJ.pdf"><img src="effects/nino34_cru_tmp_25_MJJ.png" alt="Relationship between El Ni&ntilde;o and temperature in May-July" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_JJA.pdf"><img src="effects/nino34_cru_tmp_25_JJA.png" alt="Relationship between El Ni&ntilde;o and temperature in June-August" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_JAS.pdf"><img src="effects/nino34_cru_tmp_25_JAS.png" alt="Relationship between El Ni&ntilde;o and temperature in July-September" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_ASO.pdf"><img src="effects/nino34_cru_tmp_25_ASO.png" alt="Relationship between El Ni&ntilde;o and temperature in August-October" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_SON.pdf"><img src="effects/nino34_cru_tmp_25_SON.png" alt="Relationship between El Ni&ntilde;o and temperature in September-November" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_OND.pdf"><img src="effects/nino34_cru_tmp_25_OND.png" alt="Relationship between El Ni&ntilde;o and temperature in October-December" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_NDJ.pdf"><img src="effects/nino34_cru_tmp_25_NDJ.png" alt="Relationship between El Ni&ntilde;o and temperature in November-January" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
<a href="effects/nino34_cru_tmp_25_DJF.pdf"><img src="effects/nino34_cru_tmp_25_DJF.png" alt="Relationship between El Ni&ntilde;o and temperature in December-February" border=0 width="100%" class="realimage" hspace=0 vspace=0></a>
<br>
</center>
</div>
<div class="col-md-4">
         <div class="menukopje">Standard seasons</div>
         <div class="menulink"><a href="effects.cgi?id=FORM_EMAIL">Precipitation, temperature and tropical storms</a></div>

         <div class="menukopje">Other seasons</div>
         <div class="menulink"><a href="monthly_precipitation_effects.cgi?id=FORM_EMAIL">Monthly precipitation</a></div>
         <div class="menulink"><a href="seasonal_precipitation_effects.cgi?id=FORM_EMAIL">Seasonal precipitation</a></div>
         <div class="menulink"><a href="monthly_temperature_effects.cgi?id=FORM_EMAIL">Monthly temperature</a></div>
         <div class="menulink">Seasonal temperature</div>
</div>
</div>
EOF

cat ./vinklude/bottom_en.html
 cat <<EOF
</body>
</html>
EOF
