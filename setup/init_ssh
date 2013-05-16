#!/bin/bash


echo 'Generating SSH key - you should be ok to hit enter for most of these options...'
ssh-keygen
echo 'Generated SSH key. Printing out PUBLIC key to paste into GitHub/Codebase:'
echo '========== COPY BETWEEN THESE LINES ========='
cat ~/.ssh/id_rsa.pub
echo '========== COPY BETWEEN THESE LINES ========='
echo 'Alternatively, open the below link in a browser and copy from there:'
cat ~/.ssh/id_rsa.pub | curl -F 'sprunge=<-' http://sprunge.us
read -p "Once you have done this, press enter... "
echo ''
echo 'Populating known hosts (GitHub and Codebase)...'
echo '|1|DoFAmwPnwU1YwRSCBgBVARtLI6M=|/+QG7EQ2ZhkMaRI2uuuUAS0BL+o= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==' > ~/.ssh/known_hosts
echo '|1|L3Q/AEEaq0tHrI0oytRGmtj3wJc=|yUv90xn3AgXNuehJjLB/XwW5/oo= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==' >> ~/.ssh/known_hosts
echo '|1|Tz5au394l9L9LqO2SEQ8HliWarM=|RDmFpXx3L4tvfgAZ+TazihqaDkQ= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDfuFY+eDM4/OdGRKZlZ9dZyU8lImckW2oHBX2e2WitbPiCVNP91u2ck4SohxeIdAVMlTLTKGA55ZD/uZ4t37Eo=' >> ~/.ssh/known_hosts
echo '|1|7PsqXJqxI3SAfxhxkH+9uOKpw5Q=|SDLQJFFOGswUNExsAUmnQeFt+nA= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDfuFY+eDM4/OdGRKZlZ9dZyU8lImckW2oHBX2e2WitbPiCVNP91u2ck4SohxeIdAVMlTLTKGA55ZD/uZ4t37Eo=' >> ~/.ssh/known_hosts
echo 'Done.'
