# Files for question 5.

#Below is incomplete and does not work yet.
      
FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')

gifcount = 0
tiffcount = 0
execount = 0
txtcount = 0
xbmcount = 0
pscount = 0
htmlcount = 0

lines = []


for line in f:
       line = line.strip()
       lines.append(line)
# stripping for files
for a in range (len(lines)):
       try:
              results = lines[a].split()[6]
       except:
              continue
       if results.endswith('gif'):
              gifcount += 1
              continue
       if results.endswith('tiff'):
              tiffcount += 1
              continue
       if results.endswith('exe'):
              execount += 1
              continue
       if results.endswith('txt'):
              txtcount += 1
              continue 
       if results.endswith('xbm'):
              xbmcount += 1
              continue
       if results.endswith('ps'):
              pscount += 1
              continue
       if results.endswith('html'):
              htmlcount += 1
              continue
       else:
              continue     

         

