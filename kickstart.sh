#!/bin/bash
# This script initializes the dashboards
# Use it to fully configure a dashboard from a cold boot

echo "Droptop Dashboards V1.0 by AMP Studios"
echo
echo
echo

# Git clone
echo "Cloning git repository into home directory"
git clone https://github.com/pealock/scripts.git ~/droptop
echo
echo
echo

# Set up Python environment
echo "Checking for Python environment"
echo
echo
PYTHON=~/.py
if test -d "$PYTHON"; then
  echo "Python environment already configured"
else
  echo "Setting up Python environment"
  python -m venv ~/.py
  ~/.py/bin/pip install selenium python-dotenv
fi
echo
echo
echo

# Check for .env file, create if none exists
echo "Checking for credentials"
echo
echo
CREDS=~/droptop/.env
if test -f "$CREDS"; then
  echo "Credentials found"
else
  echo "Credentials not found"
  echo "Please enter your Droptop credentials"
  echo
  read -p "Email:" email
  read -p "Password:" password
  echo -e "EMAIL='$email'\nPASSWORD='$password'" > ~/droptop/.env
  echo
  echo
  echo
fi


# Set bg
echo "Setting background"
DISPLAY=:0 pcmanfm --set-wallpaper ~/droptop/images/"$HOSTNAME".jpg
echo
echo
echo

# Test launch
echo "Testing dashboard"
DISPLAY=:0 ~/.py/bin/python3 ~/droptop/scripts/bayDashboard.py
killall chromium-browser
echo
echo
echo

echo "Setting up boot environment"
echo "DISPLAY=:0 ~/.py/bin/python3 ~/droptop/scripts/bayDashboard.py" >> ~/.bashrc



