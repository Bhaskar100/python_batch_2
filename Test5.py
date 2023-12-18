
d1= [1,3,4,5,4,5,6,7,4,9]

"""

for i in d1:
    print(i)

print(d1[2:6]) # forward indexing
print(d1[-5:-1]) # Backword indexing
print(d1[::2])
print(d1[::-1]) # reverse a list.
print(d1[4])
print(d1[-3])
print(len(d1))
print(type(d1))
print(dir(d1))
print(d1)
d1.append(10) #added the value into the list
print(d1)
#d1.clear() # removing all elements.
#del d1

d2 = d1.copy() # creating duplicate list
print('d2 list')
print(d2)
print(d1.count(4)) # to check number of occurences
"""
d3 = [15,20,30,40]
d1.extend(d3) # add another list to existing list.
print(d1)
print(len(d1))
print(d1.index(15))
print(d1.index(11))
""" it will return index of given value """


