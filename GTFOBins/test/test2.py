import os

os.system("find / -perm -04000 2>/dev/null > SUIDs.txt")

suidPermissionsFile = open("SUIDs.txt",'r')
usefulSUIDFile = open("UsefulSUIDs.txt",'w')

usefulSUIDs=list()
for x in suidPermissionsFile:
	if(x.startswith("/usr/bin/")):
		x=x[9:]
		usefulSUIDs.append(x)
		usefulSUIDFile.write(x)
print(usefulSUIDs,end='')