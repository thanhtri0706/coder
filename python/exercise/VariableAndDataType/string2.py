
# create a string name 's'
s = 'I love to write python'

# split words an put into a list
split_s = s.split()
print(split_s)

# execute condition
for word in split_s:
  if word.find('i') > -1:
    print("I found 'i' in : '%s'" %word)