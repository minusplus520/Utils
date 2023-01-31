#!/usr/bin/env python
import os,sys
from subprocess import call

pwd = os.getcwd()

if os.path.isdir(pwd+"/zebu"):
    os.chdir("zebu")
    pwd = os.getcwd()
while pwd.split("/")[-1] != "zebu" and len(pwd.split("/")) > 2:
    os.chdir("..")
    pwd = os.getcwd()
pwd += "/"
if len(sys.argv) == 2:
    if sys.argv[1] == "par":
        pwd += "sw_cc/bin/zPar_main"
    elif sys.argv[1] == "ntg":
        pwd += "sw_cc/bin/zNetgen_main"
    elif sys.argv[1] == "time":
        pwd += "sw_cc/bin/zTime_main"
os.chdir(pwd)

if pwd.split("/")[-2] == "zebu" or "main" in pwd.split("/")[-1]:
    call(["gvim", "synmake.err"])
else:
    print("Cannot found")
