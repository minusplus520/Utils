#!/usr/bin/env python
import os,sys
from subprocess import call

pwd = os.getcwd()

foundzcui = False
while len(pwd.split("/")) > 2:
    for dir in os.listdir(pwd):
        if ".p4branch" == dir:
            foundzcui = True
    if foundzcui == True:
        break
    os.chdir('..')
    pwd = os.getcwd()

print("PWD:" + pwd)
if len(pwd.split("/")) != 2:
    call(["vgp4checkin"])
else:
    print("sandbox root not found.")
