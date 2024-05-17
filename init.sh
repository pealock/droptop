#!/bin/bash

echo "Droptop Dashboards V1.0 by AMP Studios"

# Set up Python environment
echo "Setting up Python environment"
python -m venv ~/.py
~/.py/bin/pip install selenium python-dotenv

# Set .env file
echo "Please enter Droptop credentials"
read -p "Email:" email
read -p "Password:" password
echo -e "EMAIL='$email'\nPASSWORD='$password'" > ~/droptop/.env

# Set bg
echo "Setting background"
DISPLAY=:0 pcmanfm --set-wallpaper ~/droptop/images/"$HOSTNAME".jpg

# Test launch
echo "Testing dashboard"
~/.py/bin/python3 ~/droptop/scripts/bayDashboard.py