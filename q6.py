# Code for least frequent file. 



FILE_NAME = 'local_copy.log'  
f = open('local_copy.log')

# each file is set to zero so it can be used to count after stripping
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

# below uses min to count the most frequent file
files = (gifcount, tiffcount, execount, txtcount, xbmcount, pscount, htmlcount)

# below uses min to count least frequent file
if gifcount == min(files):
    print('gif is least requested file:', min(files))

elif tiffcount == min(files):
    print('tiff is least requested file:', min(files))

elif execount == min(files):
    print('exe is least requested file:', min(files))

elif txtcount == min(files):
    print('txt is least requested file:', min(files))

elif xbmcount == min(files):
    print('xbm is least requested file:', min(files))

elif pscount == min(files):
    print('ps is least requested file:', min(files))

elif htmlcount == min(files):
    print('html is least requested file:', min(files))

