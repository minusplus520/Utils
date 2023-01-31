#!/u/chenc/.aliasscript/python
import sys, os
from shutil import copyfile
from subprocess import call
import datetime

if sys.argv[1] == "jp":
    ftp = "ftp jp01-ftp-int.synopsys.com"
else:
    ftp = "ftp us01-ftp-int.synopsys.com"

filename= input("File: ")

abspath = os.path.abspath(filename)

upload = "/remote/us01home54/chenc/upload/" + str(datetime.datetime.now()).replace(' ','')

targetname = input("gpg name: ")
uploadfile = targetname + ".gpg"
destpath = upload + "/" + uploadfile

if os.path.isdir(upload) == False:
    os.mkdir(upload)
else:
    print("Dir already created")

if os.path.exists(destpath):
    print("File already exists!!")
    assert False

copyfile(abspath, destpath)
print("copy file " + filename + " to " + destpath)

os.chdir(upload)

print("======== Procedure ========")
print("cd outgoing")
print("bin")
print("hash")
print("prompt")
print("put " + uploadfile)
print("quit")

call(ftp.split(" "))
