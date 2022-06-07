from averaging import avg
from timeit import timeit
import requests as rq
from bs4 import BeautifulSoup
import subprocess
from subprocess import Popen
import math
import os
from time import time, sleep
import lxml
#from main import callback

here = os.path.dirname(os.path.abspath(__file__))
af1 = os.path.join(here, 'af1.txt')
af2 = os.path.join(here, 'af2.txt')
#because python doesn't know where these files are even though they're in the same directory???

  
#def process_exists(process_name): #checking if a process exists, not useable here
  #call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
  # use buildin check_output right away
  #output = subprocess.check_output(call).decode()
  # check in last line for process name
  #last_line = output.strip().split('\r\n')[-1]
  # because Fail message could be translated
  #return last_line.lower().startswith(process_name.lower())
  
def difficulty():
  #----Grabbing Data From Website-----#
  html_text = rq.get("https://www.coinwarz.com/mining/ravencoin/difficulty-chart").text
  soup = BeautifulSoup(html_text, 'lxml')
  difficulty = soup.find('div', class_ = 'diff-current').text #doesn't exist?!?
  difficulty = difficulty.replace(",", "")

  #-----Writing Raw Data to infile-----#
  f = open(af1, "w") #open infile
  #str(difficulty) #turn data to string
  f.write(difficulty) #write raw data into file
  f.close() #close off file

  #-----Rewriting Data with no whitespace-----#
  with open(af1,"r+") as f, open(af2,"r+") as a: #opening in and out files
     for i in f.readlines(): #for every line in infile
           if not i.strip(): #if not stripped, continue stripping
               continue
           if i: 
               str(i)
               a.write(i) #write out data with no blank space

  #-----Converting to List-----#
  mylines = []                             # Declare an empty list named mylines.
  with open (af2, 'r+') as myfile: # Open lorem.txt for reading text data.
        for myline in myfile:                # For each line, stored as myline,
            mylines.append(myline.strip())#adds content to list, removes \n
  
  #-----Removing uneeded elements-----#
  mylines = mylines[3:]
  mylines = mylines.pop(1)
  difficulty = float(mylines)
  return difficulty
