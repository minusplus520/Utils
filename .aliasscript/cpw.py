#!/u/chenc/.aliasscript/python
import os
import sys
from datetime import datetime,timedelta

print("Copy Work Procedure")
print("1.\tmkdir; cd")
print("2.\tln -s [design work dir]/* .")
print("3.\tmkdir my_work; cd")
print("4.\tcp [design be_default dir]/* .")
print("5.\tln -s ../design/RTLDB .")
print("6.\tcd ..")
print("7.\tln -s [design upper dir]/config_FR5 .")

# input
if len(sys.argv) < 2:
    designdir = input("Design Dir:")
else:
    designdir = sys.argv[1]

#1
if input("1.\tmkdir; cd") != 0:
    design = input("design Name:")
    os.makedirs(design)
    os.chdir(design)
#2
if input("2.\tln -s [design work dir]/* .") != 0:
    os.system("ln -s " + designdir + "/* .")

#3
if input("3.\tmkdir my-work; cd") != 0:
    work = input("work Name:")
    os.makedirs(work)
    os.chdir(work)

#4
if input("4.\tcp [design be_default dir]/* .") != 0:
    os.system("cp " + designdir + "/backend_default/* .")

#5
if input("5.\tln -s ../design/RTLDB .") != 0:
    os.system("ln -s ../design/RTLDB .")

