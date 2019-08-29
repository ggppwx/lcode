#!/bin/bash


git config core.autocrlf input
git add algorithm
bash ./timestamp.sh
# refresh readme
python3 get.py -r

# publish the change to github
git add README.md
git add SUMMARY.md
git add algorithm
git commit -m 'update lcode'
git push