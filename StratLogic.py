from difficulty import difficulty
from averaging import avg
import os
import subprocess
from subprocess import Popen
from time import time, sleep

here = os.getcwd()
start_rvn = os.path.join(here, 'start_rvn.bat')
#pyinstaller is the most stressful thing I have ever used, can't find any files unless directory specified
def process_exists(process_name): #function I stole to find out if a process is running or not
  call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
  #use buildin check_output right away
  output = subprocess.check_output(call).decode()
  # check in last line for process name
  last_line = output.strip().split('\r\n')[-1]
  # because Fail message could be translated
  return last_line.lower().startswith(process_name.lower())


def StratMine():
 while True:
    sleep(900 - time() % 900) #change time in seconds
    if difficulty() > avg(): # if difficulty is greater than the average
      if process_exists("nbminer.exe") is True: #check if miner is currently running
       os.system("TASKKILL /F /IM nbminer.exe") #kill process if mining is running
       print("current difficulty currently higher than average difficulty")
      else:
        print("current difficulty currently higher than average difficulty") #telling client that difficulty is too high

    if difficulty() < avg(): #if difficulty is less than average, mine
      if process_exists("nbminer.exe") is True: #if nbminer is already running
       print("NBminer already running")

      elif  process_exists("nbminer.exe") is False: #if nbminer is not running
        subprocess.Popen(start_rvn, creationflags=subprocess.CREATE_NEW_CONSOLE) 
        #create new console = open seperate console window, not to run in terminal
        

