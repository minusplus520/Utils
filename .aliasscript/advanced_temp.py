class jobType(Enum):
    zTopBuild   = 1
    zCoreBuild  = 2
    zPar        = 3
    zTime       = 4
    PDMDAP      = 5
    PDMTiming   = 6
    FPGA        = 7
    zTimefpga   = 8

class Job:
    def __init__(self, Cmd, JobType):
        self.Cmd = Cmd
        self.JobType = JobType

class schedular:
    def __init__(self, logFile):
        self.logFile = logFile
        self.q = Queue.Queue()
    def add(j):
        self.q.put(j)


