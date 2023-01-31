#!/usr/bin/env python

from __future__ import with_statement
from __future__ import print_function

import os

envlist = os.environ

with open("/remote/us01home54/chenc/.aliasscript/lenv.txt", "r") as keyfile:
    temp = keyfile.readlines()
keyword = [x.strip().split() for x in temp if len(x) > 3]

for [key, default] in keyword:
    if key[0] == '#':
        continue
    if key[0] == '-':
        print("")
        continue
    if key in envlist.keys():
        print(str(key) + " = " + str(envlist[key]))
    else:
        print(("{0:<60s}>NotSet".format(key)).replace(" ","-"))
        print("\t\t\t\t\tsetenv " + key + " " + default)
