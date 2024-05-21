#!/bin/bash
# This script initializes the dashboards
# Use it to fully configure a dashboard from a cold boot

echo "Droptop Dashboards V1.0 by AMP Studios"
echo
echo
echo

sleep 3

# Check for git repo, clone if not found
echo "Checking for Github repository"
echo
echo
echo
sleep 1

GITHUB=~/droptop
if test -d "$GITHUB"; then
  echo "Github repository already configured!"
  echo
  echo
  echo
else
  echo "Cloning git repository into home directory"
  echo
  echo
  echo
  git clone https://github.com/pealock/droptop.git ~/droptop
  echo
  echo
  echo
fi

sleep 3

# Set up Python environment
echo "Checking for Python environment"
echo
echo
echo
sleep 1

PYTHON=~/.py
if test -d "$PYTHON"; then
  echo "Python environment already configured!"
else
  echo "Setting up Python environment"
  python -m venv ~/.py
  ~/.py/bin/pip install selenium python-dotenv
  echo
  echo
  echo
  echo "Python environment configured"
fi
echo
echo
echo

sleep 3

# Check for .env file, create if none exists
echo "Checking for credentials"
echo
echo
echo

sleep 1

CREDS=~/droptop/.env
if test -f "$CREDS"; then
  echo "Credentials found"
  echo
  echo
  echo
else
  echo "Credentials not found"
  echo
  echo
  echo
  sleep 3
  echo "Please enter your Droptop credentials"
  echo
  read -p "Email:" email
  read -p "Password:" password
  echo -e "EMAIL='$email'\nPASSWORD='$password'" > ~/droptop/.env
  echo
  echo
  echo
fi

sleep 3

# Set bg
echo "Setting background"
DISPLAY=:0 pcmanfm --set-wallpaper ~/droptop/images/"$HOSTNAME".jpg
echo
echo
echo

sleep 3

echo "Testing display output"

sleep 1

DISPLAY=:0 ffplay -fs -t 5 -autoexit ~/droptop/videos/catjam.mp4

echo
echo
echo

sleep 3

# Test launch
echo "Testing dashboard"
DISPLAY=:0 ~/.py/bin/python3 ~/droptop/scripts/bayDashboard.py
killall chromium-browser
echo
echo
echo

sleep 3

echo "Setting up boot environment"
echo "DISPLAY=:0 ~/.py/bin/python3 ~/droptop/scripts/bayDashboard.py" >> ~/.bashrc
echo
echo
echo

sleep 3

echo "Removing kickstart script"
rm ~/kickstart.sh
echo
echo
echo


