# Test for connectivity
ansible all -m ping

# Git pull
ansible all -m shell -a "cd ~/droptop && git pull"

# Run dashboard command
ansible all -m shell -a "DISPLAY=:0 ~/.py/bin/python3 ~/droptop/scripts/bayDashboard.py"
