#!/usr/bin/env python3

#This script is meant to pull all unique ENV from all images
import os 

f = open('envlist', 'r')
#Pulls in image names from envlist list
images = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
f.close()

for x in range(len(images)): #Opens each image
    print("Image number: ")
    print(x)
    f = open(images[x], 'r')
    lines = [word.strip() for line in f.readlines() for word in line.split('\n') if word.strip()]
    for y in range(len(lines)): #Pulls all headers from images's ENV list
        header = lines[y].split("=",1)[0]
        
        f = open("ENV_headers.txt", "r")
        fileheaders = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
        #Command checks ENV against ENV Master List
        cmd = 'grep ' + header + ' ENV_headers.txt'
        Return = os.system(cmd)
        
        if(Return != 0):
            f = open("ENV_headers.txt", "a")
            f.write(header + '\n')
               