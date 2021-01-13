#Current Goal of Script: To modify SSL config settings of a postgresql
#target, chrisiodb, 8 different configurations and fuzztainer sessions
import subprocess
import os
from subprocess import check_output

#Pull the target image from github
os.system("docker pull chrisioa/dsamdb:latest")
#Get the image ID
os.system("docker image ls | grep 'chrisioa' | awk '{print $3}' > chrisdb")
f = open("chrisdb", "r")
image_ID = f.readline().rstrip()
print("\nBASE IMAGE: " + image_ID + "\n")

#Run the base image: chrisioa/dsamdb:latest
os.system('docker run -d ' + image_ID + ' > container')
f = open("container", "r")
container = f.readline().rstrip()
print("\nBASE CONTAINER: " + container + "\n")

#Run a range to modify the base image then create 8 unique containers for 
#fuzztainer to parallel run
for i in range(8):
    #Add server.crt and server.key files to image
    print("\nImage# ", i, " DOCKER COPY Server key and certificate.. ")
    cmd = 'docker cp ./server.crt ' + container + ':/var/lib/postgresql/data/'    
    os.system(cmd) 
    cmd = 'docker cp ./server.key ' + container + ':/var/lib/postgresql/data/'
    os.system(cmd)
    #Copy modified config file into container
    cmd = 'docker cp ./configs/' + str(i) + '/postgresql.conf ' + container + ':/var/lib/postgresql/data/'    
    print("\nImage# ", i, " DOCKER COPY Config File.. ")
    os.system(cmd)   
    #Create the Image ID based upon the modified image(mutated configuration settings)
    newimage = check_output(["docker",  "commit", container, "chris" + str(i)])
    newimage = newimage.decode('utf-8').lstrip(":sha256").rstrip()
    print("\nImage# ", i, " NEWIMAGE:  " + newimage)
    
    print("\nRemoving modified image..\n")
    os.system('docker container stop ' + container)
    os.system('docker container rm ' + container)
    print("\nRestarting base image..\n")
    os.system("docker image ls | grep 'chrisioa' | awk '{print $3}' > chrisdb")
    f = open("chrisdb", "r")
    image_ID = f.readline().rstrip()
    os.system('docker run -d ' + image_ID + ' > container')
    f = open("container", "r")
    container = f.readline().rstrip()


os.system("rm container")
#Start fuzztainer.py with current ChrisDB as target and stores results in 
#ith directory under home directory
#proc = []
#print("Fuzztainer..")
#for i in range(8):
#	print("../fuzztainer.py", "-w PGResults/" + str(i), "chris" + str(i))
#	proc.append(subprocess.Popen(["../fuzztainer.py", "-w", "./PGResults/" + str(i), "chris" + str(i)]))

	while(1):
            for p in proc:
                if not p.poll():
                    # p is dead


		print(proc[i].stdout)


