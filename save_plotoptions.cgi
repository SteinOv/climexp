#!/bin/bash
if [ "$FORM_EMAIL" != someone@somewhere ]; then
# remember plotoptions for next plot
###echo "saving preferences in ./prefs/$FORM_EMAIL.plotoptions"
if [ -n "$save_lon2" ]; then
    here_lon2=$FORM_lon2
    FORM_lon2=$save_lon2
fi
if [ -n "$save_lat2" ]; then
    here_lat2=$FORM_lat2
    FORM_lat2=$save_lat2
fi
cat > ./prefs/$FORM_EMAIL.plotoptions <<EOF
FORM_mproj=$FORM_mproj;
FORM_lat1=$FORM_lat1;
FORM_lat2=$FORM_lat2;
FORM_lon1=$FORM_lon1;
FORM_lon2=$FORM_lon2;
FORM_lev1=$FORM_lev1;
FORM_lev2=$FORM_lev2;
FORM_altlat1=$FORM_altlat1;
FORM_altlat2=$FORM_altlat2;
FORM_altlon1=$FORM_altlon1;
FORM_altlon2=$FORM_altlon2;
FORM_plottype=$FORM_plottype;
FORM_cmin=$FORM_cmin;
FORM_cmax=$FORM_cmax;
FORM_maskout=$FORM_maskout;
FORM_pmin=$FORM_pmin;
FORM_colourscale=$FORM_colourscale;
FORM_shadingtype=$FORM_shadingtype;
FORM_yflip=$FORM_yflip;
FORM_notitleonplot=$FORM_notitleonplot;
FORM_nogrid=$FORM_nogrid;
FORM_nopoli=$FORM_nopoli;
FORM_nolab=$FORM_nolab;
FORM_nocbar=$FORM_nocbar;
FORM_xlint=$FORM_xlint;
FORM_ylint=$FORM_ylint;
FORM_intertype=$FORM_intertype;
FORM_masktype=$FORM_masktype;
FORM_standardunits=$FORM_standardunits;
FORM_log=$FORM_log;
EOF
if [ -n "$here_lon2" ]; then
    FORM_lon2=$here_lon2
fi
if [ -n "$here_lat2" ]; then
    FORM_lat2=$here_lat2
fi
fi
