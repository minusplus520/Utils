#!/u/chenc/.aliasscript/python
import sys, os
import subprocess
import datetime
import argparse

GridCmd1 = "qrsh -P zebuDev_largeMem -l mem_free=256G -cwd -V -noshell -now n"
GridCmd2 = "qrsh -P zebuDev_largeMem -l mem_free=128G -cwd -V -noshell -now n"
GridCmd3 = "qrsh -P zebuDev -l mem_free=32G -cwd -V -noshell -now n"

# Flow switch
runzTopB        = 1
runzCoreB       = 1
runzPar         = 1
runzTime        = 1
runPDM          = 1
runDAP          = 1
runPDMTiming    = 1

def print_both(file, s):
    print(s)
    file.write(s+"\n")

def submitJob(Cmd, logFile):
    status = subprocess.run(Cmd.split())
    if status.returncode == 1:
        print_both(logFile, "Failed at " + Cmd)
        sys.exit(1)

# Inital Setting/Checking
cwdPath = os.getcwd()
if ('backend' in cwdPath.split('/')[-1] == False) and ('work' in cwdPath.split('/')[-1] == False):
    print("Wrong directory to start!")
    print(cwdPath.split('/')[-1])
    sys.exit(1)

rtldbPath = cwdPath + "/" + "RTLDB"
if os.path.islink(rtldbPath) == False:
    print("RTLDB not exist!")
    sys.exit(1)

if "ZEBU_ROOT" not in os.environ:
    print("ZEBU_ROOT not set!")
    sys.exit(1)

# Dump log
logPath = cwdPath + "/BE_status_" + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".log"
if os.path.isfile(logPath):
    sys.exit(1)

try:
    logFile = open(logPath, 'w')
except IOError:
    print(logPath + " open failure!")
    sys.exit(1)

print_both(logFile, "runzTopBuild       : " + str(runzTopB))
print_both(logFile, "runzCoreBuild      : " + str(runzCoreB))
print_both(logFile, "runzPar            : " + str(runzPar))
print_both(logFile, "runzTime           : " + str(runzTime))
print_both(logFile, "runPDM             : " + str(runPDM))
print_both(logFile, "runDAP             : " + str(runDAP))
print_both(logFile, "runPDMTiming       : " + str(runPDMTiming))

# Start

# zTopB
if runzTopB == True:
    Cmd = GridCmd1 + " zTopBuild zTopBuild.tcl"
    print_both(logFile, Cmd)
    submitJob(Cmd, logFile)

# zCoreB
if runzCoreB == True:
    for f in os.listdir(cwdPath):
        if os.path.isdir(f) == False:
            continue
        if f.startswith("work.") == False:
            continue
        print("Core:" + f)
        os.chdir(f)
        Cmd = GridCmd1 + " zCoreBuild zCoreBuild_ztb.tcl"
        print_both(logFile, Cmd)
        submitJob(Cmd, logFile)
# End
