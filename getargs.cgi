#!/bin/bash
if [ -z "$alreadycalledgetargs" ]; then
    export alreadycalledgetargs=true
    eval `./bin/proccgi "$@"`
    # construct a web call that gives the same results
    if [ -n "$SSL_PROTOCOL" ]; then
        export SCRIPTURL="https://$SERVER_NAME$SCRIPT_NAME?"
    else
        export SCRIPTURL="http://$SERVER_NAME$SCRIPT_NAME?"
    fi
    export EMAIL="$FORM_id"
    [ -z "$EMAIL" ] && EMAIL="$FORM_EMAIL"
    [ -z "$EMAIL" ] && EMAIL="$FORM_email"
    if [ -z "$EMAIL" ]; then
        # maybe someone used the old links
        c1=`echo "$QUERY_STRING" | fgrep -c '@'`
        c2=`echo "$QUERY_STRING" | fgrep -c '+'`
        if [ $c1 = 1 -a $c2 = 0 ]; then
            EMAIL="$QUERY_STRING"
        fi
    fi
    EMAIL=`echo "$EMAIL" | fgrep -v '/' `
    EMAIL=`echo "$EMAIL" | tr -cd '[:alnum:]@.-_' | fgrep -v "/" | egrep -v '(@|\.|-)sexy(@|\.|-)|(@|\.|-)sex(@|\.|-)|(@|\.|-)porn(@|\.|-)|(@|\.|-)porno(@|\.|-)|youtube.com|fynalcut.com|shop.*ru$|della-marta'`
    EMAIL=${EMAIL#id=}
    [ "$EMAIL" = FORM_EMAIL ] && EMAIL=""
    export id=$EMAIL
    FORM_type=`echo "$FORM_type" | tr -d -C '[a-zA-Z0-9_\-]'`
    FORM_TYPE=`echo "$FORM_TYPE" | tr -d -C '[a-zA-Z0-9_\-]'`
    ###echo "EMAIL=$EMAIL<br>"
    # build a variable SCRIPTURL that can be used to reproduce this step later
    # do not include ID, so that it does not leak into plots.
    # do not include big tables, such as station lists.
    formvarlist=`set | egrep '^FORM_' | fgrep -v FORM_data | fgrep -v FORM_list | egrep -v '=$' | tr ' ' '_' | sed -e "s/$id/\\$id/"`
    init=0
    for formvar in $formvarlist; do
        if [ $init = 0 ]; then
            init=1
        else
            SCRIPTURL="$SCRIPTURL&"
        fi
        SCRIPTURL="$SCRIPTURL${formvar#FORM_}"
    done
    SCRIPTURL=`echo "$SCRIPTURL" | sed -e 's/+++/%%%/' -e 's/++/%%/'`
    [ -n "FORM_WMO" ] && FORM_WMO=`echo "$FORM_WMO" | sed -e 's/%%%/+++/' -e 's/%%/++/'`
    [ -n "FORM_wmo" ] && FORM_wmo=`echo "$FORM_wmo" | sed -e 's/%%%/+++/' -e 's/%%/++/'`
    [ -n "$FORM_field" ] && export FORM_field
fi # alreadycalledgetargs