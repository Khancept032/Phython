import datetime
from datetime import date
import re

FILE_NAME = 'local_copy.log'  
fh = open('local_copy.log')

with open('local_copy.log', 'rb') as fh:
    first = next(fh).decode()

    fh.seek(-1024, 2)
    last = fh.readlines()[-1].decode()



print(first)
print(last)
