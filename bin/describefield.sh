#!/bin/sh
file="$1"
if [ -z "$file" ]; then
  echo "usage: $0 file"
  exit -1
fi
lwrite=false
[ "$lwrite" = true ] && echo "file=$file<br>"
describefile=${0%.sh}
if [ ${file%.nc} = $file -a ${file%.cdf} = $file -o ${file#data} != $file ]; then
    [ "$lwrite" = true ] && echo "grads file $file<br>"
    ($describefile $file > /dev/null) 2>&1
    eval `./bin/getunits $file`
else
    [ "$lwrite" = true ] && echo "netcdf file $file"  
    c1=`echo $file | fgrep -c '%%'`
    c2=`echo $file | fgrep -c '++'`
    [ "$lwrite" = true ] && echo "ensemble? c1,c2 = $c1,$c2<br>"
    if [ $c1 -eq 0 -a $c2 -eq 0 ]
    then
        ensfile=$file
    else
  	    c3=`echo $file | fgrep -c '%%%'`
  	    i=0
  	    if [ $c3 = 0 ]; then
    	    ii=00
    	    nmax=99
        else
    	    ii=000
    	    nmax=999
        fi
        newestfile=""
        while [ $i -le $nmax ]
        do
    	    if [ $c3 = 0 ]; then
    	        allfiles=`echo $file | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
		    else
		        allfiles=`echo $file | sed -e "s:\%\%\%:$ii:"`
		    fi
		    if [ "$splitfield" = true ]; then
    		    ensfile=`ls -t $allfiles | head -1`
    		else
    		    ensfile=$allfiles
    		fi
	        if [ -s $ensfile -a \( -z "$newestfile" -o $ensfile -nt "$newestfile" \) ]; then
	    	    newestfile=$ensfile
	    	    newestfiles=$allfiles
	        fi
	        if [ $i -lt 1 -o -s $ensfile ]; then
		        i=$((i+1))
		    else
			    i=$((1+nmax))
		    fi
		    if [ $c3 = 0 ]; then
		        if [ $i -lt 10 ]; then
		    	    ii=0$i
  			    else
  				    ii=$i
  			    fi
  		    else
		        if [ $i -lt 10 ]; then
		    	    ii=00$i
  			    elif [ $i -lt 100 ]; then
  				    ii=0$i
  			    else
  				    ii=$i
  			    fi
  		    fi
	    done
	    ensfile=$newestfile
	    allfiles=$newestfiles
    fi
    metadata=./metadata/`echo $file|tr '/' '.'`.txt
    [ "$lwrite" = true ] && echo "echo ensfile=$ensfile<br>"
    if [ ! -s $ensfile ]; then
        echo "error: cannot locate $ensfile<br>"
        exit -1
    fi
    if [ -s $metadata -a ! $metadata -ot $ensfile ]; then
#       quick from cache
        cat $metadata
        if [ -s $metadata.eval ]; then
            eval `egrep '^[A-Z]*=[-"0-9a-zA-Z/*]*$' $metadata.eval`
        else
            ./bin/getunits $file | fgrep -v error > $metadata.eval        
            touch -r $file $metadata.eval
            [ -s $metadata.eval ] && eval `egrep '^[A-Z]*=[-"0-9a-zA-Z/*]*$' $metadata.eval`
        fi
#       but make sure the field is read once to make it faster on the next page
        [ ! "$splitield" = true ] && ( ./bin/getunits $file < /dev/null > /dev/null 2>&1 ) &
    else
        ($describefile $file > /dev/null ) 2>&1 | tee $metadata
        ###echo "./bin/getunits $file &gt; $metadata.eval<br>"
        ./bin/getunits $file | fgrep -v error > $metadata.eval
        touch -r $file $metadata
        touch -r $file $metadata.eval
    fi
fi
