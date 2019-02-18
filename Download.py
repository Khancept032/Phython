# This will download the log files to your local machine

from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access-log'
LOCAL_FILE = 'local_copy.log'


local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))


print('Starting file download...')