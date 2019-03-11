#!/bin/bash
git add README.md
git add Algorithm

bash ./timestamp.sh ;

# refresh readme
python3 get.py -r

# publish the change to github

git commit -m 'update lcode'
git push 


