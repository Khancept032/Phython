# Download log file
#print('Starting file download...')

#from urllib.request import urlretrieve

#URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
#LOCAL_FILE = 'local_copy.log'

#urlretrieve (URL_PATH, LOCAL_FILE )

#print('File has downloaded.')

# File for question 3 solutions.

# What percentage of the requests were not successful (any 4xx status code)?

FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')
lines = []
count400 = 0

for line in f:
    line = line.strip()
    lines.append(line)

for a in range(len(lines)):
    try:
        results = lines[a].split()[8]
    except:
        continue
    if results.startswith("4"):
        count400 += 1
        continue  
   # else:
       # continue  

print ('Not successful requests 4xx:', (count400/len(lines)) * 100, 'percent') 