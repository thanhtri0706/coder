

# create file with nam my data.csv
fh = open('mydata.csv', 'w')

# data base
lines = [
  'Data,Time,Temp,Rainfall',
  '2014-01-01,00:00,2.34,4.45',
  '2014-01-01,12:00,6.70,8.34',
  '2014-01-02,00:00,-1.34,10.25'
]

# write data to file
for line in lines:
  fh.write(line + '\n')

# close and save file
fh.close()