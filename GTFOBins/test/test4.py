# Code to execute the commands found in filteredVulnerabilities.txt file

import os
from threading import Thread
from time import sleep

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
		print("Privlege escallation failed for: ", x)



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
#print("==================While loop ended==================")
if escallationStatus==0: print("Privlege escallation failed!!!")
os.system("exit")
