# Part 4 splitting into 12 files
import re

FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')

rx_dict = {
    'January': re.compile(r.'January = (Jan)')
    'February': re.compile(r.'February = (Feb)')
    'March': re.compile(r.'March = (Mar)')
    'April': re.compile(r.'April = (Apr)')
    'May': re.compile(r.'May = (May)')
    'June': re.compile(r.'June = (Jun)')
    'July': re.compile(r.'July = (Jul)')
    'August': re.compile(r.'August = (Aug)')
    'September': re.compile(r.'September = (Sep)')
    'OCtober': re.compile(r.'October = (Oct)')
    'November': re.compile(r.'November = (Nov)')
    'December': re.compile(r.'December = (Dec)')
}

def _parse_line('local_copy.log')
    for key, rx in rx_dict.items()
    match = rx.search('local_copy.log')
    if match
        return key, match
return None, None

with open('local_copy.log', 'r') as file object:
    line = file_object.readline()
    while line:
        key, match = _parse_line('local_copy.log')
        if key == 'January'

        if key == 'February'

        if key == 'March'

        if key == 'April'

        if key == 'May'

        if key == 'June'

        if key == 'July'
        
        if key == 'August'

        if key == 'September'

        if key == 'October'

        if key == 'November'

        if key == 'December'      