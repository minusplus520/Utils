#!/usr/bin/env python
import os
import re
import sys
import glob
from subprocess import call
from datetime import datetime,timedelta

class MyStrOrder:
    def __init__(self, inner):
        self.inner = inner
    def __lt__(self, other):
        self_s = self.inner.split(".")
        other_s = other.inner.split(".")
        if self_s.len() < other_s.len():
            return True
        if self_s[0] == other_s[0] and self_s[1] != other_s[1]:
            if self_s[1][-1] == "_" and other_s[1][-1].isdigit():
                return True
            elif self_s[1][-1].isdigit() and other_s[1][-1] == "_":
                return False
            elif self_s[1][-1].isdigit() and other_s[1][-1].isdigit():
                return self_s[1][-1] < other_s[1][-1]
            return len(self_s[1]) > len(other_s[1])
        return self.inner < other.inner

sandboxdir = "/slowfs/vgzebuvi1/chihuang/zebuBuild/"
sandboxdir_s = "~/chiECO/zebuBuild"
cshloc = "/release/zebu_env.csh"
bashloc = "/release/zebu_env.bash"
loc = cshloc

mode = 0

if len(sys.argv) > 1:
    if sys.argv[1] == 'b':
        loc = bashloc
        mode = 1
    elif sys.argv[1] == 'r':
        mode = 2
    elif sys.argv[1] == 'z':
        mode = 3
    elif sys.argv[1] == 'zmake':
        mode = 4
    elif sys.argv[1] == "s":
        mode = 5
else:
    loc = cshloc
    mode = 0
if mode == 0 or mode == 1:
    print("===== ZEBU_ROOT =====")
    if os.getenv('ZEBU_ROOT') is not None:
        print(os.environ['ZEBU_ROOT'])
    else:
        print("Haven't set")
    print("")
    print("===== VCS_HOME =====")
    if os.getenv('VCS_HOME') is not None:
        print(os.environ['VCS_HOME'])
    else:
        print("Haven't set")
    print("")


print("===== LIST =====")
#  for sb in sorted(os.listdir(sandboxdir), key = MyStrOrder):
for sb in sorted(os.listdir(sandboxdir)):
    if os.path.isdir(sandboxdir + sb) == False:
        continue
    if mode == 0 or mode == 1:
        if os.path.exists(sandboxdir+sb+loc) == False:
            print("source " + ("{0:<80s}>NotBuild".format(sandboxdir+sb+loc)).replace(" ","-"))
        else:
            print("source {0:<80s}".format(sandboxdir+sb+loc))
    else:
        if mode == 2:
            print("cd "+sandboxdir_s+sb)
        elif mode == 3:
            print("cd "+sandboxdir_s+sb+"/zebu/")
        elif mode == 4:
            print("cd "+sandboxdir_s+sb+"/zebu/;zmake")
        elif mode == 5:
            print("cd "+sandboxdir_s+sb+"/zebu/sw_cc/")
        else:
            print("FAILURE!!!")
