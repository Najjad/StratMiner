#Very inneficient, optimizations will come later

import requests as rq
from bs4 import BeautifulSoup
import os

here = os.getcwd()

infile = os.path.join(here, 'infile.txt')
outfile = os.path.join(here, 'outfile.txt')
#because python doesn't know where these files are even though they're in the same directory???

def avg():
  #----Grabbing Data From Website-----#
  html_text = rq.get("https://www.coinwarz.com/mining/ravencoin/difficulty-chart").text #turning HTML of a page into variable called 'html_text'
  soup = BeautifulSoup(html_text, 'lxml')
  table = soup.find('table', class_ = 'table table-bordered table-striped').text #look for specific HTML class containing needed data
  table = table.replace(",", "") #removing commas

  #-----Writing Raw Data to infile-----#
  f = open(infile, "w") #open infile
  str(table) #turn data to string
  f.write(table) #write raw data into file
  f.close() #close off file

  #-----Rewriting Data with no whitespace-----#
  with open(infile,"r+") as f, open(outfile, "r+") as a: #opening in and out files
   for i in f.readlines(): #for every line in infile
         if not i.strip(): #if not stripped, continue stripping
             continue
         if i: 
             str(i)
             a.write(i) #write out data with no blank space

  #-----Converting to List-----#
  mylines = []                             # Declare an empty list named mylines.
  with open (outfile, 'r+') as myfile: # Open lorem.txt for reading text data.
      for myline in myfile:                # For each line, stored as myline,
          mylines.append(myline.strip())#adds content to list, removes \n
  mylines = mylines[2:] #removing first 2 lines of words

  #-----Removing Dates-----#
  count = 0
  for i in mylines: #for every element within the list
    mylines.pop(count) #removing element by index
    count += 1 #removing every other index, where dates are located

  #-----Changing how big the data set is, 1 day to 120 days-----#
  del mylines[-117:] #removing last x days so most recent days are used

  #-----Averaging Data-----#
  mylines = [float(x) for x in mylines] #turning all elements into float
  s = sum(mylines) #sum of all elements
  l = len(mylines) #how many elements total
  return s/l #sum divided by number of terms = average
  
