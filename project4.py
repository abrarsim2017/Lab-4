#IMPORTS# 
import re
import os
import collections
import datetime
from urllib.request import urlretrieve

#OPEN LOG#
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'local_copy.log'

local_file, headers = urlretrieve(url, local)

x = open('local_copy.log' , "r")
lines = x.readlines()

#VARIABLES#
total_requests = 0
requests94 = 0
redir_count = 0
unsuc_count = 0
unsuc_percent = 0
redir_percent = 0
dates = []
months = {}
files = {}

#MONTH/DATE REQUESTS MADE#
for line in lines:
  line = line.split(" ")
  a = " "
  if len(line) == 9:
    if len(line[3]) >= 19:
      a = line[3].replace('[', '')
      a = a[0:11]
      date_f = datetime.datetime.strptime(a, '%d/%b/%Y').date()
      month_f = date_f.month
      
      if a in dates:
        dates[a] += 1
      else:
        dates[a] = 1
      if month_f in months:
        months[month_f] += 1
      else:
        months[month_f] = 1
        

#UNSUCCESSFUL/REDIRECT/LAST YEAR REQUESTS#
for line in lines:   
   unsuc_count +=1
   for i in range(400, 499):
      if line.find(str(i)) != -1:
         unsuc_count += 1
        
for line in lines:   
   redir_count +=1
   for i in range(300, 399):
      if line.find(str(i)) != -1:
         redir_count += 1
        
for line in lines:
   total_requests +=1
   if line.find("1995") != -1:
      requests94 += 1        
      
unsuc_percent = unsuc_count / total_requests
redir_percent = redir_count / total_requests
      
#LEAST/MOST REQUESTED FILES#      
for line in lines:
  line = line.split(" ")
  a = " "
  if len(line) == 9:
    if len(line[6]) >= 3:
      a = line[6].replace('"', '').replace('>', '')
      
      if a in files:
        files[a] += 1
      else:
        files[a] = 1

file_sort = sorted(files)
print("What was the least-requested file? ", file_sort[0])
print("What was the most-requested file? ", file_sort[len(file_sort)-1])

x.close()

#FINAL INFORMATION DUMP#
print("\nHow many requests were made on each day? ", dates)
print("How many requests were made Per month? ", months)
print("What percentage of the requests were not successful (any 4xx status code)? ", unsuc_percent)
print("What percentage of the requests were redirected elsewhere (any 3xx codes)? ", redir_percent)
