#!/bin/bash


timestamp=`date +%Y-%m-%d`
git config --global core.autocrlf true
git diff HEAD --name-only | while read -r line ; do    
    if [[ $line =~ .*\.py$ ]] || [[ $line =~ .*\.cpp$ ]] || [[ $line =~ .*\.md$ ]]; then
        target_file=`echo $line`
        if [[  $target_file =~ .*\.md$ ]]; then
            echo "generating timestamp $target_file"
            sed -i -e "s/@timestamp.*$/@timestamp:$timestamp/g" "$target_file"
        fi
    fi

done

# file_changed=`git diff HEAD --name-only`
# echo $file_changed
# for file in $file_changed
# do
#     echo $file
# done

# useful command 
# find  ./Algorithm/ -name "*.md" -exec sh -c 'echo \\n[comment]: \<timestamp:$(stat -c "%y" "{}" | cut -d" " -f 1)\> >> "{}" ' \;



