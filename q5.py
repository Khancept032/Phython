# Code for most requested file

      
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


# below uses max to count the most frequent file
files = (gifcount, tiffcount, execount, txtcount, xbmcount, pscount, htmlcount)

if gifcount == max(files):
    print('gif is most requested file:', max(files))

elif tiffcount == max(files):
    print('tiff is most requested file:', max(files))

elif execount == max(files):
    print('exe is most requested file:', max(files))

elif txtcount == max(files):
    print('txt is most requested file:', max(files))

elif xbmcount == max(files):
    print('xbm is most requested file:', max(files))

elif pscount == max(files):
    print('ps is most requested file:', max(files))

elif htmlcount == max(files):
    print('html is most requested file:', max(files))

print()

