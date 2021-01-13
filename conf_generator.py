#!/usr/bin/env python3

import os 
import time

f = open('conflist', 'r')

#Pulls in image names from postgres list
images = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]

#print(images[0])

for x in range(len(images)): #Opens each image
    print("Image number: ")
    print(x)
    f = open(images[x], 'r')
    lines = [word.strip() for line in f.readlines() for word in line.split('\n') if word.strip()]
    for y in range(len(lines)): #Pulls all headers from images's config file
        header = lines[y].split("=",1)[0]
        setting = lines[y].partition("#")[2] 
        
        print(header)
        print(setting)
        f = open("CONF_headers.txt", "r")
        fileheaders = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
        
        cmd = 'grep ' + setting + ' CONF_headers.txt'
        print(cmd)
        Return = os.system(cmd)
        
        if(Return != 0):
            f = open("CONF_headers.txt", "a")
            f.write(header + '\n')
               