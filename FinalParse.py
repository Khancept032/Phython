# The master file of the programs will be placed in here once we have finished the programs for each question.

print('Starting file download...')

from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

urlretrieve (URL_PATH, LOCAL_FILE )

print('File has downloaded.')
print()
print('Parsing Files...')

#Question 1, find total requests
def file_len(fname):
    with open(fname) as l:
        for i, l in enumerate(l):
            pass
    return i + 1        

total = (file_len("local_copy.log"))
print("Total Request:", total) 
#Question 2, average requests per day, week and month
import datetime
from datetime import date
from datetime import timedelta
import re
FILE_NAME = 'local_copy.log'  
fh = open('local_copy.log')

with open('local_copy.log', 'rb') as fh:
    first = next(fh).decode()
    fh.seek(-1024, 2)
    last = fh.readlines()[-1].decode()
first2 = re.search(r'\d{2}/\w{3}/\d{4}',first)
last2 = re.search(r'\d{2}/\w{3}/\d{4}',last)
first3 = (first2.group().replace('Oct','10'))
last3 = (last2.group().replace('Oct','10'))
first4 = datetime.datetime.strptime(first3, "%d/%m/%Y").strftime("%Y-%m-%d")
last4 = datetime.datetime.strptime(last3, "%d/%m/%Y").strftime("%Y-%m-%d")
datetimeFormat = '%Y-%m-%d'
diff = datetime.datetime.strptime(last4, datetimeFormat)\
    - datetime.datetime.strptime(first4, datetimeFormat)
finaltime=diff.days
finaltime2=int(finaltime) + 1
print('Average Requests per Day:',int(round(total/finaltime2)))
print('Average Requests per Week:',int(round(total/finaltime*0.14285714)))
print('Average Requests per Month:',int(round(total/finaltime*0.032854884)))
#Question 3
FILE_NAME = 'local_copy.log'  
f = open('local_copy.log',)
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

pc = (count400/len(lines)) * 100
print ('Not Successful Requests 4xx:', round(pc, 2), 'percent')
#Question 4
FILE_NAME = 'local_copy.log'  
f= open('local_copy.log')
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

ps = (count300/len(lines)) * 100
print ('Redirected Requests 3xx:', round(ps, 2), 'percent')
#Question 5
FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')

# each file is set to zero so it can be used to count after stripping
gifcount = 0
tiffcount = 0
execount = 0
txtcount = 0
xbmcount = 0
pscount = 0
htmlcount = 0


lines = []
for line in f:
       line = line.strip()
       lines.append(line)

# stripping for files
for a in range (len(lines)):
       try:
              results = lines[a].split()[6]
       except:
              continue
       if results.endswith('gif'):
              gifcount += 1
              continue
       if results.endswith('tiff'):
              tiffcount += 1
              continue
       if results.endswith('exe'):
              execount += 1
              continue
       if results.endswith('txt'):
              txtcount += 1
              continue 
       if results.endswith('xbm'):
              xbmcount += 1
              continue
       if results.endswith('ps'):
              pscount += 1
              continue
       if results.endswith('html'):
              htmlcount += 1
              continue
       else:
              continue     


# below uses max to count the most frequent file
files = (gifcount, tiffcount, execount, txtcount, xbmcount, pscount, htmlcount)

if gifcount == max(files):
    print('gif is most requested file:', max(files))

elif tiffcount == max(files):
    print('tiff is most requested file:', max(files))

elif execount == max(files):
    print('exe is most requested file:', max(files))

elif txtcount == max(files):
    print('txt is most requested file:', max(files))

elif xbmcount == max(files):
    print('xbm is most requested file:', max(files))

elif pscount == max(files):
    print('ps is most requested file:', max(files))

elif htmlcount == max(files):
    print('html is most requested file:', max(files))
#Question 6
FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')

# each file is set to zero so it can be used to count after stripping
gifcount = 0
tiffcount = 0
execount = 0
txtcount = 0
xbmcount = 0
pscount = 0
htmlcount = 0


lines = []
for line in f:
       line = line.strip()
       lines.append(line)

# stripping for files
for a in range (len(lines)):
       try:
              results = lines[a].split()[6]
       except:
              continue
       if results.endswith('gif'):
              gifcount += 1
              continue
       if results.endswith('tiff'):
              tiffcount += 1
              continue
       if results.endswith('exe'):
              execount += 1
              continue
       if results.endswith('txt'):
              txtcount += 1
              continue 
       if results.endswith('xbm'):
              xbmcount += 1
              continue
       if results.endswith('ps'):
              pscount += 1
              continue
       if results.endswith('html'):
              htmlcount += 1
              continue
       else:
              continue     

# below uses min to count the most frequent file
files = (gifcount, tiffcount, execount, txtcount, xbmcount, pscount, htmlcount)

# below uses min to count least frequent file
if gifcount == min(files):
    print('gif is least requested file:', min(files))

elif tiffcount == min(files):
    print('tiff is least requested file:', min(files))

elif execount == min(files):
    print('exe is least requested file:', min(files))

elif txtcount == min(files):
    print('txt is least requested file:', min(files))

elif xbmcount == min(files):
    print('xbm is least requested file:', min(files))

elif pscount == min(files):
    print('ps is least requested file:', min(files))

elif htmlcount == min(files):
    print('html is least requested file:', min(files))

print()
print('Seperating into files by month...')
f = open('local_copy.log', 'r')
#Create seperate files by month
jan_log = open('jan_log.log', 'w+')
feb_log = open('feb_log.log', 'w+')
mar_log = open('mar_log.log', 'w+')
apr_log = open('apr_log.log', 'w+')
may_log = open('may_log.log', 'w+')
jun_log = open('jun_log.log', 'w+')
jul_log = open('jul_log.log', 'w+')
aug_log = open('aug_log.log', 'w+')
sep_log = open('sep_log.log', 'w+')
oct_log = open('oct_log.log', 'w+')
nov_log = open('nov_log.log', 'w+')
dec_log = open('dec_log.log', 'w+')

for line in f:
    if re.search((r'Jan'), line):
        jan_log.write(line)
    elif re.search((r'Feb'), line):
        feb_log.write(line)
    elif re.search((r'Mar'), line):
        mar_log.write(line)
    elif re.search((r'Apr'), line):
        apr_log.write(line)
    elif re.search((r'May'), line):
        may_log.write(line)
    elif re.search((r'Jun'), line):
        jun_log.write(line)
    elif re.search((r'Jul'), line):
        jul_log.write(line)
    elif re.search((r'Aug'), line):
        aug_log.write(line)
    elif re.search((r'Sep'), line):
        sep_log.write(line)
    elif re.search((r'Oct'), line):
        oct_log.write(line)
    elif re.search((r'Nov'), line):
        nov_log.write(line)
    elif re.search((r'Dec'), line):
        dec_log.write(line)
print('Files have downloaded.')
