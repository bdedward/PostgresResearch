#!/usr/bin/env python3
import fileinput
import os 
import pandas as pd
import csv

#Converts the Headers to CSV file 
read_file = pd.read_csv(r'./CONF_headers.txt')
read_file.to_csv(r'./conf_deltas.csv', index=None, sep='\n')

for line in fileinput.input():
    line = line.lstrip("./")
    line = line.replace("/postgresql.conf\n", "")
    f = open(line + '/postgresql.conf', 'r')
    lines = [word.strip() for line in f.readlines() for word in line.split('\n') if word.strip()]
    f.close()
    
    f = open('CONF_headers.txt', 'r')
    #Pulls in image names from envlist list
    variables = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
    f.close()
    for y in range(len(lines)): #Pulls all headers from images's config file
        
        for x in range(len(variables)):
            cmd = 'grep -nw "' + variables[x] + '" ' + line + "/postgresql.conf | cut -f 1 -d \":\" --complement | cut -f1 -d \"=\" --complement | tr -d ' ' > " + line + ".tmp"
            #print(cmd)
            os.system(cmd)
            
            f = open(line + ".tmp", "r")
            out = [word.strip() for line in f.readlines() for word in line.split('\n') if word.strip()]   

            os.system("rm " + line + ".tmp")
             
            if(len(out) > 0):         
                data = out[0].rstrip(" ")
            else:
                data = out;
            data = str(data).replace('"',"_")              
            
  
            cmd = 'echo "' + str(data) + '" | cut -f1 -d \"#\"' + "| cut -f1 -d '\"' > " + line + ".tmp"
            os.system(cmd)            
            os.system("rm " + line + ".tmp")
            
            f = open(line + ".tmp", "r")
            out = f.readlines()
            if(out[0] != ""):
                out = out[0].replace("\n","").replace("\t","").replace('/', "\/").replace('.', "\.").replace(" ", "_").replace("'", "\'")   
                cmd = "sed '/\<" + variables[x] + '\>/s/$/ ,' + out + "/' conf_deltas.csv > " + line + ".tmp && mv " + line + ".tmp conf_deltas.csv"  
                os.system(cmd)

                    