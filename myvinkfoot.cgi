#!/bin/bash
cat <<EOF
         </div>
<div class="col-md-4">
EOF
[ -z "$EMAIL" ] && EMAIL=someone@somewhere
###sed -e "s/EMAIL/$EMAIL/" ./menu_standard.html
sed -e "s/EMAIL/$EMAIL/" ./menu_choose.html
if [ -n "$listname" -o -n "$FORM_listname" ]; then
  . ./menu_investigateset.cgi
elif [ -n "$STATION" ]; then
  . ./menu_investigate.cgi
fi
###echo "FORM_field=$FORM_field"
if [ -n "$field2" -a "$splitfield" != true ]; then
  FORM_field=$field1
  kindname=$kindname1
  climfield=$climfield1
  . ./menu_investigatefield.cgi | tr '_' ' ' \
    | sed -e 's/field /field_/' -e 's/field1 /field1_/' -e 's/form /form_/'
  FORM_field=$field2
  kindname=$kindname2
  climfield=$climfield2
  . ./menu_investigatefield.cgi
elif [ -n "$FORM_field" -a "$splitfield" != true ]; then
  . ./menu_investigatefield.cgi
fi
[ -x "./$1.cgi" ] && . "./$1.cgi"
###cat ./menu_contact.html
cat <<EOF
        </div>
</div>
</div>
EOF
if [ -z "$nobottom" ]; then
    cat ./vinklude/bottom_en.html
    cat <<EOF
</body>
</html>
EOF
fi