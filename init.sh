#!/bin/bash

# Set .env file
echo -e "EMAIL=development@ampstudios.io\nPASSWORD=Ka5hmiro123" > ~/droptop/.env

# Set bg
DISPLAY=:0 pcmanfm --set-wallpaper ~/droptop/images/"$HOSTNAME".jpg

# Set auto launch