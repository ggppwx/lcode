#!/bin/bash
bash ./timestamp.sh ;

# refresh readme
python3 get.py -r

# publish the change to github
git config --global core.autocrlf true
git add README.md
git add Algorithm
git commit -m 'update lcode'
git push 


