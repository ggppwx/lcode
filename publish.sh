#!/bin/bash


git config core.autocrlf input
bash ./timestamp.sh
# refresh readme
python3 get.py -r

# publish the change to github
git add README.md
git add Algorithm
git commit -m 'update lcode'
git push 


