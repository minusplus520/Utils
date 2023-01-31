#!/usr/bin/env python
import os
import sys
import subprocess

def disk_usage(path):
    df = subprocess.Popen(["df", "-h", path], stdout=subprocess.PIPE)
    res = df.communicate()[0]
    output = res.decode().split("\n")[1].split()
    if len(output) < 4:
        output = res.decode().split("\n")[2].split()
    #print(output)
    if (output[0][0]).isdigit():
        print("Free: {0:6s} | Used: {1:6s}".format(output[2], output[1]))
    else:
        print("Free: {0:6s} | Used: {1:6s}".format(output[3], output[2]))

linktoPath = "/remote/us01home54/chenc/linkto/"

scratchlist = []
for dir in os.listdir(linktoPath):
    if "scratch" in dir:
        scratchlist += [linktoPath + dir]
scratchlist.sort()
#print(scratchlist)
print("========== scratch space check ==========")
for path in scratchlist:
    if not os.path.islink(path):
        continue
    if not os.path.exists(path):
        realpath = os.path.realpath(path)
        homedir = realpath[:realpath.rfind('/')]
        if os.path.exists(homedir):
            os.mkdir(realpath)
            print("Dir got removed. Recreate dir...")
        else:
            continue
    print("cd " + path)
    disk_usage(os.path.realpath(path))
