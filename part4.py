# Part 4 splitting into 12 files
import re

FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')

regex = '(/[A-z]{3})'
read_line = True
 
with open('local_copy.log', "r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line, re.S):
                match_text = match.group()
                match_list.append(match_text)
                print (match_text)
    else:
        data = f.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group()
            match_list.append(match_text)
file.close()