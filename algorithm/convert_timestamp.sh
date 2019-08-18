#!/bin/bash

# replace \| with ,
for entry in *.md
do 
    if [[ $entry =~ "README.md" ]]
    then
        continue
    fi    

    echo $entry        
    sed -i -e 's/\\\[comment\\\]/@timestamp/g' "$entry"
done