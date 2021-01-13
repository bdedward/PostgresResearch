#!/usr/bin/env python3

#This script is meant to be a companion script to pullpostgres.py & env_generator.py.  After all the images
#have been downloaded, ran, and config/env variable information has been pulled this script 
#is to run and populate the env_deltas.csv with postgres information.  Furthermore, env_generator.py
#will have generated an envlist which is used by this script to run the deltas.

#This script was intended to run with the terminal command: 

#  "parallel --pipepart -a envlist --eta --block -1 -j 7 python3 env_delta.py"

import fileinput
import sys
import os
import pandas as pd
import csv

#Converts the Headers to CSV file 
read_file = pd.read_csv(r'./ENV_headers.txt')
read_file.to_csv(r'./env_deltas.csv', index=None, sep='\n')

f = open('envlist', 'r')
#Pulls in image names from envlist list
images = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
f.close()

for line in fileinput.input():
    line = line.lstrip("./")
    line = line.rstrip("/env.txt\n")
    f = open(line + "/env.txt" , 'r')
    lines = [word.strip() for line in f.readlines() for word in line.split('\n') if word.strip()]
    for y in range(len(lines)):
        header = lines[y].split("=",1)[0] #ENV variable name
        data = lines[y].partition("=")[2] #ENV data

        #Finds line number of ENV variable on master list
        cmd = 'grep -xn ' + header + ' env_deltas.csv > ' + line + '.txt'
        os.system(cmd)        
        f = open(line + ".txt", 'r')
        line_no = f.readline().split(":",1)[0]
        cmd = 'rm ' + line + '.txt'
        os.system(cmd)
        
        #Prepares data for insertion into env_deltas
        if(data != "" and header != "_" and line_no != " "):
            data = data.replace(" ", "_").replace("(", "").replace(")","")     
            cmd = 'grep ' + data + ' env_deltas.csv > ' + line + ".txt"          
            sysReturn = os.system(cmd)            
            f = open(line + ".txt", "r")
            result = f.readline()            
            if sysReturn != 0:
                cmd = 'rm ' + line + '.txt'
                os.system(cmd)
            if result != 0:
                data = data.replace('/', "\/").replace('.', "\.")
                #Awesome sed command to add postgres data to the csv file
                cmd = "sed '/\<" + header + '\>/s/$/ ,' + data + "/' env_deltas.csv > " + line + ".txt && mv " + line + ".txt env_deltas.csv"            
                os.system(cmd)
                #Clean up
                cmd = "rm " + line + ".txt"
                os.system(cmd)
