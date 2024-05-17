#!/bin/bash

echo "Droptop Dashboards V1.0 by AMP Studios"
echo
echo
echo

# Set up Python environment
echo "Setting up Python environment"
python -m venv ~/.py
~/.py/bin/pip install selenium python-dotenv
echo
echo
echo

# Set .env file
echo "Please enter Droptop credentials"
read -p "Email:" email
read -p "Password:" password
echo -e "EMAIL='$email'\nPASSWORD='$password'" > ~/droptop/.env
echo
echo
echo

# Set bg
echo "Setting background"
DISPLAY=:0 pcmanfm --set-wallpaper ~/droptop/images/"$HOSTNAME".jpg
echo
echo
echo

# Test launch
echo "Testing dashboard"
DISPLAY=:0 ~/.py/bin/python3 ~/droptop/scripts/bayDashboard.py