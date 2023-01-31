#!/usr/bin/env python
import os,sys
from subprocess import call

pwd = os.getcwd()

foundzcui = False
while len(pwd.split("/")) > 2:
    for dir in os.listdir(pwd):
        if "zCui" == dir:
            foundzcui = True
    if foundzcui == True:
        break
    os.chdir('..')
    pwd = os.getcwd()

zCuilog = pwd + "/zCui/log/zCui.log"

if os.path.isfile(zCuilog) and len(pwd.split("/")) != 2:
    call(["gvim", zCuilog])
else:
    print("zCui.log not found. {:s}".format(zCuilog))
