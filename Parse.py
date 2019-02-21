# The master file of the programs will be placed in here once we have finished the programs for each question.

print('Starting file download...')

from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

urlretrieve (URL_PATH, LOCAL_FILE )

print('File has downloaded')

