#!/usr/bin/env python3

import os, signal, subprocess, string, time

processes = []
for i in range(8):
    p = subprocess.Popen(["fuzztainer", "-r", "-w", "./PGResults/" + str(i) + "/run1/", "chris_" + str(i)], stdout=subprocess.DEVNULL)
    processes.append(p)
    time.sleep(10)

while True:
    time.sleep(10)
    for i, p in enumerate(processes):
        if p.poll() is not None:
            new_p = subprocess.Popen(["fuzztainer", "-r", "-w", "./PGResults/" + str(i) + "/run1/", "chris_" + str(i)], stdout=subprocess.DEVNULL)
            processes[i] = new_p
