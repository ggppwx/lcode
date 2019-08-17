#!/bin/bash
for entry in *.md
do 
    newname=`echo "$entry" | sed -e "s/-/ /g"`
    echo $entry
    echo $newname
    mv "$entry" "$newname"
done

