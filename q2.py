import datetime
from datetime import date
from datetime import timedelta
import re
#Test value
total = 726736
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