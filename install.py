import json 
import os

f = open('packages.json',) 
data = json.load(f) 
f.close()

for package in data: 
	package['install']=input("Do you want to install "+package['name']+"?  y/n ")

for package in data: 
	if package['install'] == "y":
		print(package)
		for cmd in package['commands']:
			print("*************** Executing Command" + cmd)
			os.system(cmd)
