import os
import time
import sys

com_clock = ""
path = "/home/miner12/ethminer.err.log"

def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    #command = "/sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

while 1:
  with open(path) as f:
    lines = f.readlines()
    last = lines[-1]
    clock = last.split()[2]
    print clock
    if clock == com_clock:
      sys.stdout.write("Something Wrong")
      restart()
    print sys.stdout.write(clock + " No Problem ")
    com_clock = clock
  time.sleep(300)
