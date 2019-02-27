# Part 4 splitting into 12 files
import re

FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')
#Compile lines from log file to be seperated

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