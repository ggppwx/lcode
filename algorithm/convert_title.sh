#!/bin/bash
for entry in *.md
do 
    if [[ $entry =~ "README.md" ]]
    then
        continue
    fi
    problem=`echo "$entry" | cut -d"." -f2`

    echo $entry    
    echo $problem
    sed -i -e "s/^# Problem/# $problem/g" "$entry"
done