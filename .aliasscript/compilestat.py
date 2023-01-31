#!/usr/bin/env python
from __future__ import print_function
import sys
import os

FPGAList = []
FPGApassList = []
FPGARunningStatus = {"NotStart":[], "FAIL":[], "ZNTG":[], "OPT":[], "PLACE":[], "ROUTE":[], "DONE":[]}
FPGAfailList = []
stratList = {}
failList = []
debug = False

pdmOnText = "ZEBU_MDTMX_FORCE_PDM is used"
pdmApplyText = "Inter-SLR multiplexing needed on this FPGA"
CompileLog = "PRINT ENV"
PNRfail = "ERROR in"
PNRfail2 = "FPGA compilation finished with status 2"
zNtgDone = "STEP VIVADO"
OptDone = "STEP PLACE_DESIGN"
PlaceDone = "STEP ROUTE_DESIGN"
RouteDone = "STEP TIMING"
PnRDone = "FPGA compilation finished with status 0"

if len(sys.argv) > 1:
    BEpath = sys.argv[1]
else:
    BEpath = os.getcwd()
if len(sys.argv) > 2:
    debug = True

BEpath = os.path.abspath(BEpath)
print("PWD: " + BEpath)

pdmMode = "undef"
if os.path.isfile(BEpath + "/zPar.log"):
    zparlog = open(BEpath + "/zPar.log")
    for line in zparlog:
        if "pdmCompileFlow" in line:
            pdmMode = line.split()[-1]
            break
    print("PDM Mode: {0:s}".format(pdmMode))

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
    print("Checking({0:3d}/{1:3d}) {2:s} ...".format(idx+1, len(FPGAList), fpgaName), end = '\r')
    srcPath     = BEpath + "/" + fpgaName + ".src"
    pdmdapPath  = BEpath + "/" + fpgaName + ".pdmdap"
    oriPath     = BEpath + "/" + fpgaName + ".Original"
    fpgaPath    = BEpath + "/" + fpgaName

    if os.path.islink(fpgaPath):
        realPath = os.path.realpath(fpgaPath)
        strat = realPath.split(".")[-1]
        log = open(fpgaPath + "/zNetgen.log", "r").read()
        if pdmOnText in log:
            strat += "(PDM)  "
        else:
            strat += "(NoPDM)"
        strat = "{0:15s}".format(strat)
        if pdmApplyText in log:
            strat += " - PDM Used  "
        else:
            strat += " - PDM Noused"
        if strat in stratList:
            stratList[strat] += [fpgaName]
        else:
            stratList[strat] = [fpgaName]
        FPGApassList += [fpgaName]
    else:
        failstat = fpgaName
        if os.path.isfile(oriPath + "/compilation.log"):
            log = open(oriPath + "/compilation.log", "rb").read().decode('utf-8', 'ignore')
        elif os.path.isfile(oriPath + "/zNetgen.log") and os.path.isfile(oriPath + "/vivado.log"):
            log = CompileLog + "\n" + open(oriPath + "/zNetgen.log", "r").read() + "\n" + zNtgDone + "\n" + open(oriPath + "/vivado.log", "r").read()
        elif os.path.isfile(pdmdapPath + "/zNetgen.log"):
            log = open(pdmdapPath + "/zNetgen.log", "r").read()
        else:
            log = ""
        if pdmApplyText in log:
            failstat += " - dapOn\t"
        else:
            failstat += "        \t"
        if not CompileLog in log:
            failstat += "not start"
            FPGARunningStatus["NotStart"] += [fpgaName]
        if PNRfail in log or PNRfail2 in log:
            failstat += "Original failed"
            FPGARunningStatus["FAIL"] += [fpgaName]
        else:
            if zNtgDone in log:
                failstat += "ZNTG"
                FPGARunningStatus["ZNTG"] += [fpgaName]
            if OptDone in log:
                failstat += "/OPT"
                FPGARunningStatus["OPT"] += [fpgaName]
            if PlaceDone in log:
                failstat += "/PLACE"
                FPGARunningStatus["PLACE"] += [fpgaName]
            if RouteDone in log:
                failstat += "/ROUTE"
                FPGARunningStatus["ROUTE"] += [fpgaName]
            if PnRDone in log:
                failstat += "/DONE"
                FPGARunningStatus["DONE"] += [fpgaName]
        failList += [failstat]
        FPGAfailList += [fpgaName]

print("\n")
print("Failing/Compiling FPGAs: " + str(len(FPGAfailList)))
for idx, fpga in enumerate(failList):
    print("[{0:3d}/{1:3d}] - {2:s}".format(idx+1, len(failList), fpga))
print("Summary:")
print("Total FPGAs: " + str(len(FPGAList)))
print("# of Passing FPGAs: " + str(len(FPGApassList)))
print("Strategies: ")
for strat, l in stratList.items():
    print("\t", strat, ":", len(l))
    if debug == True:
        for fpga in l:
            print("\t\t", fpga)

print("# of Failing/Compiling FPGAs: " + str(len(FPGAfailList)))
for key, fpgaList in FPGARunningStatus.items():
    print("\t # of {0:8s} in Origianl FPGA: {1:d}".format(key, len(fpgaList)))

