#!/usr/bin/python
import xml.dom.minidom
from xml.dom.minidom import Node
import os
import sys
import string

def getJobList():
    f = os.popen("qstat -xml -r")
    dom = xml.dom.minidom.parse(f)
    jobs = dom.getElementsByTagName("job_info")
    run = jobs[0]
    runjobs = run.getElementsByTagName("job_list")
    return runjobs

def fakeqstat(joblist):
    for r in joblist:
        #for x in r.childNodes:
        #    if x.nodeType == Node.ELEMENT_NODE:
        #        print(x)
        jobnum      = r.getElementsByTagName("JB_job_number")[0].childNodes[0].data
        jobname     = r.getElementsByTagName("JB_name")[0].childNodes[0].data
        jobstate    = r.getElementsByTagName("state")[0].childNodes[0].data
        jobtime     = "not set"
        if jobstate == "r" or jobstate == "dt":
            jobtime = r.getElementsByTagName("JAT_start_time")[0].childNodes[0].data
        else:
            jobtime = r.getElementsByTagName("JB_submission_time")[0].childNodes[0].data
        print(jobnum, '\t', jobname.ljust(16),'\t', jobstate,'\t',jobtime)

list = getJobList()
fakeqstat(list)
print(len(list))
