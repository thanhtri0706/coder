
#create file handle
f = open('mydata.csv', 'r')

# read data
data = f.read()

# split data
data = data.split('\n')

# print data
for item in data:
  print(item)

f.close()