#!/bin/bash
echo Generating SSH key - you should be ok to hit enter for most of these options.
ssh-keygen
echo Generated SSH key. Printing out PUBLIC key to paste into GitHub/Codebase:
echo ========== COPY BETWEEN THESE LINES =========
cat ~/.ssh/id_rsa.pub
echo ========== COPY BETWEEN THESE LINES =========
echo Alternatively, open the below link in a browser and copy from there:
cat ~/.ssh/id_rsa.pub | curl -F 'sprunge=<-' http://sprunge.us
read -p "Once you have done this, press enter... "
