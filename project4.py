import re
import os
import collections
import datetime
from urllib.request import urlretrieve

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'local_copy.log'

local_file, headers = urlretrieve(url, local)

x = open('local_copy.log' , "r")
lines = x.readlines()

total_requests = 0
requests94 = 0
redirect_count = 0
error_count = 0
unsuc_percent = 0
redir_percent = 0
dates = {}
months = {}
files = {}

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
       
      
