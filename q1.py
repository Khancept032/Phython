# Total count of lines

def file_len(fname):
    with open(fname) as l:
        for i, l in enumerate(l):
            pass
    return i + 1        

total = (file_len("local_copy.log"))
print("Total Request:", total) 

