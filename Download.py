# This will download the log files to your local machine

print('Starting file download...')

from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

urlretrieve (URL_PATH, LOCAL_FILE )


print('File has downloaded')