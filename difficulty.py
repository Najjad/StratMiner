
import requests as rq
from bs4 import BeautifulSoup

import os

here = os.getcwd()

af1 = os.path.join(here, 'difficulty1.txt')
af2 = os.path.join(here, 'difficulty2.txt')
#because python doesn't know where these files are even though they're in the same directory???

  
def difficulty():
  #----Grabbing Data From Website-----#
  html_text = rq.get("https://www.coinwarz.com/mining/ravencoin/difficulty-chart").text
  soup = BeautifulSoup(html_text, 'lxml')
  difficulty = soup.find('div', class_ = 'diff-current').text #doesn't exist?!?
  difficulty = difficulty.replace(",", "")

  #-----Writing Raw Data to infile-----#
  f = open(af1, "w") #open infile
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
  difficulty = float(mylines) #turning difficulty into a float number
  return difficulty
