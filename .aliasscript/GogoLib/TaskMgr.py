# For compute farm job handling
# Chen Chen

import sys,os
import datetime

class Task():
    def __init__(self, project, id, cmd, block_mode = True):
        self.project = project
        self.id = id
        self.cmd = cmd
        self.block_mode = True


class TaskMgr():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.taskList = []
        self.queueList = queue.Queue()

    def add(id, cmd, block_mode = True):
        task = Task(id, cmd, block_mode)
        self.taskList += task
        self.queueList += task

    def status():
        print("=====Task Manager Status=====")

