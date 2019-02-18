# Total count of lines

def file_len(fname):
    with open(fname) as l:
        for i, x in enumerate(l):
            pass
    return i + 1        

print("Total Request:") 
print(file_len("local_copy.log")) 
