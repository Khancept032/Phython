# This will download the log files to your local machine

from urllib.request import urlretrieve

print('Starting file download...')

url = 'https:s3.amazonaws.com/tcmg476/http_access-log'
local_file = 'local_copy.log'


