# Part 4 splitting into 12 files
import re
FILE_NAME = 'local_copy.log'  
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