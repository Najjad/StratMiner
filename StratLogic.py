from difficulty import difficulty
from averaging import avg
import os
import subprocess
from time import time, sleep

def process_exists(process_name):
  call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
  #use buildin check_output right away
  output = subprocess.check_output(call).decode()
  # check in last line for process name
  last_line = output.strip().split('\r\n')[-1]
  # because Fail message could be translated
  return last_line.lower().startswith(process_name.lower())


def StratMine():
 while True:
    sleep(5 - time() % 5)
    if difficulty() > avg():
      if process_exists("nbminer.exe") is True:
       os.system("TASKKILL /F /IM nbminer.exe")
      else:
        print("difficulty currently higher than average")
    elif difficulty() < avg(): #if difficulty is less than average, mine
      if process_exists("nbminer.exe") is True: #if nbminer is already running
       os.system("TASKKILL /F /IM nbminer.exe") #exit nbminer
       subprocess.Popen(r'C:\Users\Jado Zeenni\Desktop\EfficientMiner\Design version\start_rvn.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)#rerun nbminer

      elif  process_exists("nbminer.exe") is False: #if nbminer is not running
        subprocess.Popen(r'C:\Users\Jado Zeenni\Desktop\EfficientMiner\Design version\start_rvn.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)#run nbminer


