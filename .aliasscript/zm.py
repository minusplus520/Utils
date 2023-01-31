#!/usr/bin/env python
import os, sys
from subprocess import call

additionalDir = "zebu/"
cmd = ["vgbuild", "--full64"]
if len(sys.argv) == 2:
    if sys.argv[1] == "par":
        additionalDir += "sw_cc/bin/zPar_main/"
    elif sys.argv[1] == "ntg":
        additionalDir += "sw_cc/bin/zNetgen_main/"
    elif sys.argv[1] == "time":
        additionalDir += "sw_cc/bin/zTime_main/"
    elif sys.argv[1] == "core":
        additionalDir += "sw_cc/bin/zCoreBuild_main/"
    elif sys.argv[1] == "top":
        additionalDir += "sw_cc/bin/zTopBuild_main/"
    elif sys.argv[1] == "c":
        cmd += ["--target=clean"]
    elif sys.argv[1] == "s":
        additionalDir = "./"
        cmd = ["vgp4sync", "zebu"]
    elif sys.argv[1] == "u":
        cmd += ["--target=run_unit_test,l0_tests"]
    elif sys.argv[1] == "i":
        cmd += ["--target=install_makerelease"]
    else:
        print("Unrecongnized option")
        sys.exit(0)

# Found View path
pwd = os.getcwd()

foundView = False
while len(pwd.split("/")) > 2:
    for dir in os.listdir(pwd):
        if ".p4branch" == dir:
            foundView = True
    if foundView == True:
        break
    os.chdir('..')
    pwd = os.getcwd()

if foundView == False:
    print("Wrong directory to execute zm")
    sys.exit()

if additionalDir != "./":
    os.chdir(additionalDir)
print("DIR: " + os.getcwd())
print("CMD: " + ' '.join(cmd))
call(cmd)
