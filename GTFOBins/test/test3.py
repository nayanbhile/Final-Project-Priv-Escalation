# Code to filter the vulnerabilities found in the victim machine using SUID executables and write it into a file

import os

vulnerabilities = open("vulnerabilities.txt")
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
print(filteredVulnerabilities)


