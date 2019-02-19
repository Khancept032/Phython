# Files for question 5.


def most():
    import operator
    x = open("locl_copy.txt", "r")
    line = []
    countReq = {}
    filelist = []

    count = 0
    for line in x:
        count+=1
        line.append(line)
    for i in range(len(line)):
        listSplit = line[int(i)].split()
        try: reqFile = listSplit[6]
        except: pass
        filelist.append(reqFile)
    for key in filelist:
        if key not in countReq:
            countReq[key] = 1    
        else:
             if key in countReq:
                countReq[key] += 1
