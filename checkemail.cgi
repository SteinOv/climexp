#!/bin/bash
# redefine anonymous
[ -z "$id" ] && id=$EMAIL
[ -z "$EMAIL" ] && EMAIL=$id
[ -z "$EMAIL" ] && EMAIL=someone@somewhere  && id=$EMAIL
# common typo?
[ "$EMAIL" = someone@somehere ] && EMAIL=someone@somewhere
c=`fgrep -c "^$EMAIL " ./log/newlist`
if [ $c != 0 ]; then # the user gave a real aemail address. Cpnvert to md5 hash.
    md5=`fgrep "^$EMAIL " ./log/newlist | cut -f 4 -d ' ' | tail -1`
    EMAIL=$md5
    id=$md5
fi
# new system
if [ $EMAIL != someone@somewhere ]; then
    EMAIL=`echo "${EMAIL}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" | cut -b 1-32` 
fi
c=`fgrep -c " $EMAIL " ./log/newlist`
if [ $c != 0 ]; then
    realemail=`fgrep " $EMAIL " log/newlist | tail -1 | cut -f 1 -d ' ' | cut -b 2-`
    if [ `uname` = Darwin ]; then
        md5=`echo "$realemail" | md5`
    else
        md5=`echo "$realemail" | md5sum | cut -f 1 -d ' '`
    fi
    if [ "$md5" != "$EMAIL" ]; then
        . ./myvinkhead.cgi "Error" "Id \"$EMAIL\" does not correspond to email address" "noindex,nofollow"
        EMAIL="someone@somewhere"
        id=someone@somewhere
        FORM_id=someone@somewhere
        . ./myvinkfoot.cgi
        exit
    fi
fi

if [ $c = 0 -a $EMAIL != someone@somewhere ]; then
    EMAIL=someone@somewhere
    id=someone@somewhere
    FORM_id=someone@somewhere
    . ./myvinkhead.cgi "User $string unknown" "" "noindex,follow"
    echo "Please <a href=\"registerform.cgi\">register or log in</a>, default is to use the site anonymously (with restrictions)"
fi    
