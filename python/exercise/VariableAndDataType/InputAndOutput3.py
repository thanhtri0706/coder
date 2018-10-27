
# create a file handle
fh = open('mydata.csv', 'r')

# create empty list
rain = []

line = fh.readline()
# read lines
for line in fh.readlines():
  r = line.strip().split(',')[-1]
  rain.append(r)

# print 
print(rain)

fout = open('myrain.txt', 'w')

for r in rain:
  fout.write('%s\n' %r)

fout.close()