#!/u/chenc/.aliasscript/python
import sys, os
import datetime
import time
import threading

def Activation():
    currTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:-")
    print(currTime)




if __name__ == '__main__':
    AllDone = False
    Duration = 1440
    Count = 0
    while AllDone == False:
        AllDone = Activation()
        time.sleep(60)
        Count += 1
        if Count == Duration:
            break
