<h1>DROPTOP Bay Screens</h1>

Collection of scripts for automating Droptop devices to display specific information relevant to the location of the device. This particular collection of scripts assumes a four bay operation plus a waiting room.
<br/>
<br/>
<b>Requirements - you must supply your own .ENV file</b>
<br/>
<br/>
EMAIL = 'YOUREMAIL@EXAMPLE.COM'
<br/>
PASSWORD = 'YOURPASSWORD'


<h3>Install Instructions for Raspberry PI OS LIte</h3>
<br>
<code>
sudo apt update && apt upgrade -y<br>
sudo apt install lightdm blackbox xterm<br>
sudo nano /etc/lightdm/lightdm.conf<br>
[Seat*]<br>
xserver-command=X -nocursor<br>
sudo raspi-config<br>
	system - desktop autoboot<br>
	display - blanking disable<br>
reboot<br>
sudo apt install chromium-browser chromium-chromedriver git python3 pip -y<br>
python -m venv ~/.py<br>
~/.py/bin/pip install selenium python-dotenv<br>
cd ~ && git clone https://github.com/pealock/droptop.git<br>
nano ~/droptop/.env<br>
EMAIL=YOUREMAIL@EMAIL.COM<br>
PASSWORD=YOURPASSWORD<br>
crontab -e<br>
0 6 * * 1-5 ~/droptop/launchers/bay1.sh<br>
0 18 * * 1-5 killall chromium-browser<br>
</code>