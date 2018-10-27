
# create a file handle
f = open('mydata.csv', 'r')

# read first lien 
line = f.readline()

# loop file and print each line
while line:
  print(line)
  line = f.readline()

# print 'It's over'
print('It''s over')