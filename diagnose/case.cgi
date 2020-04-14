#!/bin/sh

gxout=shaded
lat1=
lat2=
lon1=
lon2=
cmaxsea=
cmaxhalf=
colour_f=
case $var in
  slp|slp_f) field=era5_msl_e # nslp
        name=slp_ecmwf # slp_ncepncar
        mproj=nps
        lon1=-180
        lon2=180
        colour=10
        colour_f=10
        cmax=1500
        cmaxsea=1000
        cmaxhalf=500
        cmaxyr=250
        c1=98000
        c2=103000
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  slp_w|slp_w_f) field=era5_msl_e # nslp
        name=slp_w_ecmwf
        mproj=latlon
        lon1=-180
        lon2=180
        colour=10
        colour_f=10
        cmax=1500
        cmaxsea=500
        cmaxhalf=250
        cmaxyr=100
        c1=98000
        c2=103000
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  slpsh|slpsh_f) field=era5_msl_e # nslp
        name=slp_ncepncar_sh
        mproj=sps
        colour=10
        colour_f=10
        cmax=1500
        cmaxsea=1000
        cmaxhalf=500
        cmaxyr=250
        c1=98000
        c2=103000
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  z500|z500_f) field=era5_z500_e # nz500
        name=z500_ecmwf # z500_ncepncar
        mproj=nps
        colour=10
        colour_f=10
        cmax=1500 # 150
        cmaxsea=1000 # 100
        cmaxhalf=750 # 75
        cmaxyr=500 # 50
        c1=50000 # 5000
        c2=60000 # 6000
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  z500sh|z500sh_f) field=era5_z500_e # nz500
        name=z500_ecmwf_sh # z500_ncepncar_sh
        mproj=sps
        colour=10
        colour_f=10
        cmax=1500 # 150
        cmaxsea=1000 # 100
        cmaxhalf=750 # 75
        cmaxyr=500 # 50
        c1=5000 # 5000
        c2=6000 # 6000
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  nt2m|nt2m_f) field=nair
        name=t2m_ncepncar
        mproj=nps
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        c1=220
        c2=320
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  t2m|t2m_f) field=era5_t2m_e # ghcn_cams_05
        name=t2m_ecmwf # t2m_ghcncams
        mproj=nps
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        c1=-50
        c2=50
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  t2mw|t2mw_f) field=era5_t2m_e # ghcn_cams_05
        name=t2m_ecmwf_w # t2m_ghcncams_w
        mproj=latlon
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        c1=-50
        c2=50
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  tlt)  field=tlt_60
        name=tlt_uah
        mproj=latlon
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  temp) field=crutem3
        name=t2m_cru
        mproj=nps
        gxout=grfill
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  sst|sst_f) field=sstoi_v2
        name=sst_ncep
        mproj=nps
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        c1=0
        c2=30
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1982
        climyear2=2010
        ;;
  sst_w|sst_w_f) field=sstoi_v2
        name=sst_ncep_w
        mproj=latlon
		lat1=-90
		lat2=90
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        c1=0
        c2=30
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1982
        climyear2=2010
        ;;
  snow|snow_f) field=rutgers_nhsnow
        name=snow_rucl
        mproj=nps
        colour=11
        cmax=1
        cmaxsea=0.5
        cmaxyr=0.25
        c1=0
        c2=1
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  ice|ice_f)  field=iceoi_v2
        name=ice_ncep
        mproj=nps
        colour=11
        cmax=1
        cmaxsea=0.5
        cmaxyr=0.25
        c1=0
        c2=1
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  ice_n|ice_n_f) field=ice_index_n
        name=icen_nsidc
        mproj=nps
        colour=11
        cmax=1
        cmaxsea=0.5
        cmaxyr=0.25
        c1=0
        c2=1
        lat1=55
        lat2=90
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  ice_s|ice_s_f) field=ice_index_s
        name=ices_nsidc
        mproj=sps
        colour=11
        cmax=1
        cmaxsea=0.5
        cmaxyr=0.25
        c1=0
        c2=1
        lat1=-90
        lat2=-55
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  o3nh|o3nh_f) field=o3col
        name=o3nh_knmi
        mproj=nps
        colour=10
        cmax=75
        cmaxyr=50
        c1=200
        c2=400
        lat1=30
        lat2=90
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  o3sh|o3sh_f) field=o3col
        name=o3sh_knmi
        mproj=sps
        colour=10
        cmax=75
        cmaxyr=50
        c1=200
        c2=400
        lat1=-90
        lat2=-30
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  prcp) field=cmorph_monthly
        name=prcp_cmorph
        mproj=latlon
        colour=12
        c1=0
        c2=24
        lat1=-90
        lat2=90
        plotanomaly=
        climyear1=
        climyear2=
        ;;
  prcp_frac)
        field=cmorph_monthly
        name=prcp_cmorph
        mproj=latlon
        colour=11
        cmax=2
        cmaxhalf=1
        cmaxyr=0.5
        lat1=-90
        lat2=90
        plotanomaly=on
        plotanomalykind=relative
        climyear1=
        climyear2=
        ;;
  pr)   field=gpccall_10
        name=prcp_gpcc
        mproj=latlon
        colour=12
        c1=0
        c2=25
        lat1=-90
        lat2=90
        plotanomaly=
        climyear1=1981
        climyear2=2010
        ;;
  pr_frac)
        field=gpccall_10
        name=prcp_gpcc
        mproj=latlon
        colour=11
        cmax=2
        cmaxhalf=1
        cmaxyr=0.5
        lat1=-90
        lat2=90
        plotanomaly=on
        plotanomalykind=relative
        climyear1=1981
        climyear2=2010
        ;;
  tg|tg_f)
        field=ensembles_025_tg_mo
        name=tg_eobs
        mproj=latlon
        gxout=grfill
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        lat1=30
        lat2=75
        lon1=-30
        lon2=50
        c1=-20
        c2=30
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  tn|tn_f)   
        field=ensembles_025_tn_mo
        name=tn_eobs
        mproj=latlon
        gxout=grfill
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        lat1=30
        lat2=75
        lon1=-30
        lon2=50
        c1=-30
        c2=20
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  tx|tx_f)
        field=ensembles_025_tx_mo
        name=tx_eobs
        mproj=latlon
        gxout=grfill
        colour=10
        colour_f=10
        cmax=5
        cmaxyr=2.5
        lat1=30
        lat2=75
        lon1=-30
        lon2=50
        c1=-10
        c2=40
        plotanomaly=on
        plotanomalykind=absolute
        climyear1=1981
        climyear2=2010
        ;;
  rr|rr_f)
        field=ensembles_025_rr_mo
        name=rr_eobs
        mproj=latlon
        gxout=grfill
        colour=11
        cmax=2
        cmaxyr=1
        lat1=30
        lat2=75
        lon1=-30
        lon2=50
        c1=0
        c2=5
        plotanomaly=on
        plotanomalykind=relative
        climyear1=1981
        climyear2=2010
        ;;
  *) echo "unknown var $var";exit -1;;
  esac
  if [ ${var%_f} != ${var} ]; then
      name=${name}_f
      plotanomaly=
      plotanomalykind=
      climyear1=
      climyear2=
      if [ -n "$colour_f" ]; then
          colour=$colour_f
      else
          if [ $colour = 0 -o $colour = 10 ]; then
              colour=13
          else
              colour=12
          fi
      fi
      if [ -z "$c1" ]; then
          echo "absolute plots for $var not ready"
          exit -1
      fi
  else
      if [ $var != pr -a $var != prcp ]; then
      if [ ${i%er} != $i ]; then
      	if [ -z "$cmaxhalf" ]; then
      		c1=-$cmaxyr
      		c2=$cmaxyr
      	else
      		c1=-$cmaxhalf
      		c2=$cmaxhalf
      	fi
      elif [ ${i#yr} != $i -o ${i%er} != $i ]; then
          [ -z "$cmaxyr" ] && echo "please define cmaxyr for $var" && exit -1
          c1=-$cmaxyr
          c2=$cmaxyr
      elif [ \( $i = season -o $i = DJF -o $i = JFM -o $i = FMA -o $i = MAM -o $i = AMJ \
        -o $i = MJJ -o $i = JJA -o $i = JAS -o $i = ASO -o $i = SON -o $i = OND -o $i = NDJ \) -a -n "$cmaxsea" ]; then
          c1=-$cmaxsea
          c2=$cmaxsea
      else
          c1=-$cmax
          c2=$cmax
      fi
      fi
  fi
