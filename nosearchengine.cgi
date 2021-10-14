#!/bin/bash
. ./searchengine.cgi
if [ -n "$ROBOT" ]
then
  echo "No access for robots and other non-human life forms"
  echo "Please contact the administrator (climate-explorer@knmi.nl) if you are human"
  exit
fi

