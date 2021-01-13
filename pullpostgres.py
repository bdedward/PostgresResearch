#!/usr/bin/env python3
#Author: Benjamin Edwards
#Purpose: Fuzztainer Project Support
#Date: 8/4/2020

import os

#Pulls in image names from postgres list
f = open('postgres', 'r')
images = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
f.close()

#Make logs directory
cmd = 'touch Logs.txt'
os.system(cmd)

for x in range(len(images)):
	#Handles first and last image name on list	
	target = images[x].replace('[', "")
	target = target.replace(']', "")

	cmd = 'docker run -d ' + target 
	ReturnStatus = os.system(cmd)
	
	#Finds container ID
	cmd = 'docker ps > tmp.txt'
	os.system(cmd)
	f = open('tmp.txt', 'r')
	line = f.readline()
	line = f.readline()
	Container_ID = line.split(' ', 1)[0]
	cmd = 'rm tmp.txt'
	os.system(cmd)

	#Removes / from image name for sake of making directory
	directory = target.replace('/', "-")
	directory = directory.replace('"', "")
	directory = directory + '-config'
	cmd = 'mkdir ' + directory 
	os.system(cmd)


	#Command to pull environment variables from image
	cmd = 'echo "printenv > /env.txt" | docker exec -i ' + Container_ID + ' bash'
	os.system(cmd)

	#Copy ENV list to host
	cmd = 'docker cp ' + Container_ID + '://env.txt ./' + directory
	os.system(cmd)

	#Pull PGDATA path from ENV list
	cmd = 'grep PGDATA ' + directory + '/env.txt > ' + directory + '/path.txt'
	os.system(cmd)	

    #path of PGDATA derived
	p = directory + '/path.txt'
	f = open(p, 'r')
	path = f.readline()
	path = path.strip("PGDATA=")
	path = path.rstrip();
	PGpath = ':/' + path + '/postgresql.conf'
	
	#Copies postgresql.conf from running container given the path we found above
	cmd = 'docker cp ' + Container_ID + PGpath + ' ./' + directory + '/'	
	sysReturn = os.system(cmd)
	
	#Logs if no config file found
	if(sysReturn != 0):
		cmd = 'echo ' + target + ' >> Logs.txt'
		os.system(cmd)

	#Cleans up container/image for next iteration
	cmd = 'docker stop $(docker ps -aq)'
	os.system(cmd)

	cmd = 'docker rm $(docker ps -aq)'
	os.system(cmd)

	cmd = 'docker rmi $(docker images -q)'
	os.system(cmd)
    
    #Add prune volume modulus to prevent accruing too much space
	




