#!/usr/bin/env python
import sys, os
import datetime

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.islink(fp):
                continue
            total_size += os.path.getsize(fp)
    return total_size

def ConvertNum(num):
    ratio = num/1024.0/1024.0/1024.0/400.0*100.0
    c = "B"
    if num > 1024:
        num = num / 1024
        c = "KB"
    if num > 1024:
        num = num / 1024
        c = "MB"
    if num > 1024:
        num = num / 1024
        c = "GB"
    return "{0:8.2f} {1:>3s} ({2:5.2f}%)".format(num,c,ratio)

def WalkSize(dir, godowndir):
    s = 0
    for subdir in sorted(os.listdir(dir)):
        if os.path.isdir(dir+"/"+subdir) == False:
            continue
        if subdir in godowndir:
            s += WalkSize(dir+"/"+subdir,godowndir)
        else:
            temp = get_size(dir+"/"+subdir)
            print("{0:<32s} \t: {1:20s}".format((dir+"/"+subdir)[rootsize:],ConvertNum(temp)) )
            log.write("{0:<32s} \t: {1:20s}\n".format((dir+"/"+subdir)[rootsize:],ConvertNum(temp)) )
            s += temp
    return s


root = "/remote/vgrnd104/chenc"
rootsize = len(root) + 1
logpos = "~/.aliasscript/space.log"
log = open(logpos,"w")

if len(sys.argv) >= 2:
    root = sys.argv[1]

Sum = 0

GoDownDir = ["designs", "sandbox"]

print("\n==========Disk Space Report==========\n")
log.write("\n==========Disk Space Report==========\n\n")
Sum = WalkSize(root, GoDownDir);
print("Sum: " + ConvertNum(Sum))
log.write("Sum: " + ConvertNum(Sum) + "\n")
ts = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("Time : " + ts)
log.write("Time: " + ts + "\n")

