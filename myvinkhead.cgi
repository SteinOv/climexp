#!/bin/bash
# generates the vink headers with a user-defied title and subtitle
if [ -z "$myvinkhead" ]; then
myvinkhead="done"
if [ -n "$3" ]; then
  robot="<meta name=\"robots\" content=\""$3"\">"
fi
if [ -n "$absolute_paths" ]; then
    prfx="https://climexp.knmi.nl/"
    prfx="/" # maybe better
else
    prfx=""
fi
cat <<EOF
<!doctype html>
<html lang="en">
<head>
<!-- beheerder: Geert Jan van Oldenborgh -->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
$extrahead
$robot
<link rel="stylesheet" href="${prfx}styles/rccstyle.css" type="text/css">
<link rel="shortcut icon" href="/favicon.ico"> 
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<title>Climate Explorer: $1</title>
<style type="text/css">
a { text-decoration: none }
</style>
</head>
<body>
<div id="top"></div>
<!-- font import WMO style-->
<script language="javascript" src="${prfx}library/javascript/hidden_info_switch.js"></script>
<script language="javascript" src="${prfx}library/javascript/pop_page.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
EOF
. ./searchengine.cgi
# in case it does not come from getopts filter the EMAIL string 
EMAIL=`echo "$EMAIL" | sed -e 's/[^A-Za-z0-9_.@-]/_/g'`
sed -e "s/FORM_EMAIL/$EMAIL/" ./vinklude/rcc_pagehead.html 
cat <<EOF
            <div class="col-md-8">
            <div class="breadc2020"><a href="start.cgi?id=$EMAIL">Home</a> <img src="${prfx}vinklude/images/separator_bdc.png">   $1: $2</div>
            <h2>$1</h2>
            $2<br>
<!-- Voeg hieronder de inhoud van de pagina in -->
EOF
fi
. ./init.cgi
