#!/usr/bin/env python3

import os, signal, subprocess, string, time

proc = []
p = subprocess.Popen(["fuzztainer", "-r", "-w", "./PGResults/chris_default/run2/", "chrisioa/dsamdb"])
proc.append(p)
time.sleep(10)

while True:
    time.sleep(10)
    for i, p in enumerate(proc):
        if p.poll() is not None:
            new_p = subprocess.Popen(["fuzztainer", "-r", "-w", "./PGResults/chris_default/run2/", "chrisioa/dsamdb"])
            proc[i] = new_p
