# Files for question 5.

#Below is incomplete and does not work yet.

# def most():
   # import operator
   # x = open("locl_copy.txt", "r")
   # line = []
   # countReq = {}
   # filelist = []

   # count = 0
   # for line in x:
    #    count+=1
     #   line.append(line)
   # for i in range(len(line)):
    #    listSplit = line[int(i)].split()
     #   try: reqFile = listSplit[6]
      #  except: pass
       # filelist.append(reqFile)
   # for key in filelist:
    #    if key not in countReq:
     #       countReq[key] = 1    
      #  else:
       #      if key in countReq:
        #        countReq[key] += 1

#testing a method to count the most requested file
#currently this below doesnt do exactly what we need it to, it uses dictionary. 

print('Retrieving Most Requested File...')
fname = 'local_copy.log'
if len(fname) < 1 : fname = 'local_copy.log'
hand = open(fname)

d = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
       d[w] = d.get(w,0) + 1 
  
largest = -1
theword = None
for k,v in d.items() :
        if v in d :
            largest = v
            theword = k
print('Most Requested:',theword,largest)            
       
