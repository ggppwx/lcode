#!/bin/bash

timestamp=`date +%Y-%m-%d`
echo -e "\n<$timestamp>" >> temp


git diff HEAD --name-only | while read -r line ; do
    
    if [[ $line =~ .*\.py$ ]] || [[ $line =~ .*\.cpp$ ]]; then
        target_file=`echo $line | sed  "s/\/[^\/]*$/\/README.md/"`
        if [[  $target_file =~ .*\.md$ ]]; then
            echo $target_file
            sed -i "$s/<timestamp.*$/<timestamp:$timestamp>/" "$target_file"
        fi
    fi

done

# file_changed=`git diff HEAD --name-only`
# echo $file_changed
# for file in $file_changed
# do
#     echo $file
# done


