#!/depot/Python-2.7/bin/python

import subprocess
import os
import sys
import getpass
import shutil

debug = False
user = getpass.getuser()

sshdir = '/u/%s/.ssh' % user
done = '%s/.sfs_done'%sshdir
if os.path.exists(done):
    print "\n\tSeems like ssh_for_synmake was already run and synmake.identity created in %s\n" % sshdir
    print "\tIf you wish to re-generate, please remove %s/.sfs_done file and re-try \n" % sshdir
    sys.exit(0)

try:
    if not os.path.exists(sshdir):
        os.makedirs(sshdir)
except Exception, m:
    print m
    print '[ERROR] : Could not create the ssh dir: %s' % sshdir
    sys.exit(1)

passphrase = ""
cmd = 'ssh-keygen -t rsa -f %s/synmake.identity -N "%s" '%(sshdir,passphrase)

if debug:
    print "cmd is %s\n"%cmd
    print "sshdir is %s\n"%sshdir

try:
    p = subprocess.Popen('ssh-keygen -t rsa -f %s/synmake.identity -N "%s" '%(sshdir,passphrase), 
                    stderr = subprocess.STDOUT, 
                    env = os.environ,
                    cwd = sshdir,
                    shell = True)
except OSError, msg:
    print msg
    print "[ERROR]: Unable to locate ssh-keygen. Please check if \"/usr/bin\" is there in your path. \n"
    print "Alternatively, try running from a different machine (RH4 or RH5)\n"
    sys.exit(1)
except KeyboardInterrupt, msg:
    sys.exit(0)
except Exception, msg:
    print msg
    print '[ERROR] : Could not execute ssh-keygen'
    sys.exit(1)

try:
    ssh_status = p.wait()
except KeyboardInterrupt, msg:
    print msg
    sys.exit(0)
    
if ssh_status:
    print '[ERROR] : Could not successfully execute ssh_for_synmake.py'
    sys.exit(1)

pub_key = '%s/synmake.identity.pub'%sshdir
try:
    with open("%s/authorized_keys"%sshdir, "a") as filehandle:  # Open the authorized_keys in append mode
        filehandle.write(open(pub_key, 'r').read())
    os.chmod(pub_key, 0600)
    os.chmod('%s/authorized_keys'%sshdir, 0600)
    if not os.path.exists(done):
        open(done, 'w').close()
except Exception, m:
    print m
    print '[ERROR] : Unable to do the final steps...'
    print '[INFO]  : Please contact vgtools-dev@synopsys.com'
    sys.exit(1)

print "\n[INFO] : SSH setup successfully done. You can now use vgbuild with password free ssh.\n"
