#!/usr/bin/env python
from __future__ import print_function
import sys
import os

fileList = []
checkMode = 0
"""
0: Specific
1: Specific PDMDAP
2: Success
3: PDMDAP
4: Original
5: Failed Original(pass by parff)
6: Failed
"""

pwd = os.getcwd()
foundBE = False
while len(pwd.split("/")) > 2:
    for dir in os.listdir(pwd):
        if len(dir) >= 2 and dir[0] == 'U' and (dir[1:]).isdigit():
            foundBE = True
    if foundBE == True:
        break
    os.chdir('..')
    pwd = os.getcwd()
if foundBE == False:
    print("Cannot find backend_default dir. Exit.")
    sys.exit()
BEpath = pwd

if len(sys.argv) == 1:
    print("Help: ")
    print("0: Specific \t 1: Specific PDMDAP \t 2: Success \t 3: PDMDAP \t 4: Original \t 5: Failed Original(pass by parff) \t 6: Failed")
    sys.exit()


option = sys.argv[1]
if len(option) > 1:
    if option[0] == 'p':
        checkMode = 1
        option = option[1:]
    else:
        checkMode = 0
    if len(option) == 5:
        specificUid = int(option[0:1])
        specificMid = int(option[2])
        specificFid = int(option[3:])
    elif len(option) == 3 or len(option) == 4:
        specificUid = int(option[0])
        specificMid = int(option[1])
        specificFid = int(option[2:])
    else:
        print("Invalid FPGA" + option)
        sys.exit()
else:
    checkMode = int(option)

if len(sys.argv) == 3:
    checkMode = int(sys.argv[2])

if checkMode < 0 or checkMode > 6:
    print("Invalid check mode")
    sys.exit()

FPGAList = []
for Uid in range(12):
    for Mid in range(5):
        for Fid in range(12):
            fpgaName = "U{0:d}/M{1:d}/F{2:02d}".format(Uid, Mid, Fid)
            #print(fpgaName)
            srcPath     = BEpath + "/" + fpgaName + ".src"
            pdmdapPath  = BEpath + "/" + fpgaName + ".pdmdap"
            oriPath     = BEpath + "/" + fpgaName + ".Original"
            fpgaPath    = BEpath + "/" + fpgaName
            if not os.path.isdir(srcPath):
                continue
            FPGAList += [[Uid, Mid, Fid]]

for idx, [Uid, Mid, Fid] in enumerate(FPGAList):
    fpgaName = "U{0:d}/M{1:d}/F{2:02d}".format(Uid, Mid, Fid)

    srcPath     = BEpath + "/" + fpgaName + ".src"
    pdmdapPath  = BEpath + "/" + fpgaName + ".pdmdap"
    oriPath     = BEpath + "/" + fpgaName + ".Original"
    fpgaPath    = BEpath + "/" + fpgaName

    if (checkMode == 0 or checkMode == 1) and (Uid != specificUid or Mid != specificMid or Fid != specificFid):
        continue

    if checkMode == 0: # Specific
        if os.path.islink(fpgaPath):
            fileList += [fpgaPath + "/compilation.log"]
        elif os.path.isfile(oriPath + "/compilation.log"):
            print("Cannot find success symbolic link. open Original compile for {0:s}... ".format(fpgaName))
            fileList += [oriPath + "/compilation.log"]
        else:
            print("Cannot find both success or Original compile for {0:s}... Exit.".format(fpgaName))
            sys.exit()
    elif checkMode == 1: # Specific PDMDAP
        if os.path.isfile(pdmdapPath + "/zNetgen.log"):
            fileList += [pdmdapPath + "/zNetgen.log"]
        else:
            print("Cannot find pdmdap zNetgen.log for {0:s}".format(fpgaName))
            sys.exit()
    elif checkMode == 2: # Success
        if os.path.islink(fpgaPath):
            fileList += [fpgaPath + "/compilation.log"]
        else:
            print("Cannot find success compile for {0:s}".format(fpgaName))
    elif checkMode == 3: # PDMDAP
        if os.path.isfile(pdmdapPath + "/zNetgen.log"):
            fileList += [pdmdapPath + "/zNetgen.log"]
        else:
            print("Cannot find pdmdap zNetgen.log for {0:s}".format(fpgaName))
    elif checkMode == 4: # Original
        if os.path.isfile(oriPath + "/compilation.log"):
            fileList += [oriPath + "/compilation.log"]
        else:
            print("Cannot find original compilation.log for {0:s}".format(fpgaName))
    elif checkMode == 5: # failed Origianl(pass by parff)
        if os.path.islink(fpgaPath) and os.path.realpath(fpgaPath) != oriPath and os.path.isfile(oriPath + "/compilation.log"):
            fileList += [oriPath + "/compilation.log"]
    elif checkMode == 6: # failed
        if os.path.islink(fpgaPath) == False and os.path.isfile(oriPath + "/compilation.log"):
            fileList += [oriPath + "/compilation.log"]
    else:
        print("Invalid check mode")
        sys.exit()

if len(fileList) == 0:
    print("No matching FPGAs")
    sys.exit()

cmd = "gvim " + " ".join(fileList)
print(cmd)
os.system(cmd)



