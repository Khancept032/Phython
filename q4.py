# Download log file
#print('Starting file download...')

#from urllib.request import urlretrieve

#URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
#LOCAL_FILE = 'local_copy.log'

#urlretrieve (URL_PATH, LOCAL_FILE )

#print('File has downloaded.')

# File for question 4 solutions.

# What percentage of the requests were redirected elsewhere (any 3xx codes)?

FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')
lines = []
count300 = 0

# strip lines and count 3xx codes 
for line in f:
    line = line.strip()
    lines.append(line)

for a in range(len(lines)):
    try:
        results = lines[a].split()[8]
    except:
        continue
    if results.startswith("3"):
        count300 += 1
        continue  

print ('Redirected Requests 3xx:', (count300/len(lines)) * 100, 'percent') 