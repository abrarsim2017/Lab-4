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
months ={}

for line in lines:
