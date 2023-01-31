#!/usr/bin/env python
import os

cmd = "ls -al /remote/vtgimages/SAFE/linux*ZEBU*/release/zebu_env.csh"

list = os.popen(cmd).read()

cshlist = []
for line in list.split("\n"):
    if len(line.split()) < 5:
        continue
    cshlist += [line.split()[8]]

for csh in cshlist:
    print("source " + csh)
