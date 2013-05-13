#!/bin/bash
echo Generating SSH key - you should be ok to hit enter for most of these options.
ssh-keygen
echo Generated SSH key. Printing out PUBLIC key to paste into GitHub/Codebase:
echo ========== COPY BETWEEN THESE LINES =========
cat ~/.ssh/id_rsa.pub
echo ========== COPY BETWEEN THESE LINES =========
read -p "Once you have done this, press enter... "
