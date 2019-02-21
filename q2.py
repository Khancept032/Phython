# Download log file
#print('Starting file download...')

#from urllib.request import urlretrieve

#URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
#LOCAL_FILE = 'local_copy.log'

#urlretrieve (URL_PATH, LOCAL_FILE )

#print('File has downloaded.')

# File for question 2 solutions.
# How many requests were made on each day? per week? per month?

with open(local_copy.log, 'rb') as fh:
    first = next(fh).decode()
    fh.seek(-1024,2)
    last = fh.readlines()[-1].decode()
for line in fh:
    pass
last = line

import re

totaldays = 353
# Calculate results based on total requests
day = total/totaldays
week = day/7
month = week/4.35
# Output results as averages request per period
print ('Average Request per Day is', day)
print ('Average Request per Week is', week)
print ('Average Request per Month is', month)
