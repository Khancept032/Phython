# Download log file
print('Starting file download...')

from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

urlretrieve (URL_PATH, LOCAL_FILE )

print('File has downloaded.')

# File for question 4 solutions.

# What percentage of the requests were redirected elsewhere (any 3xx codes)?