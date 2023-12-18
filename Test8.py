

l1 = {10,20,30,40,50}
l2 = {'anu','tom','mike','harry','kene'}
dic= zip(l1,l2) #zipping the two lists
dd = dict(dic) # converting into a dict datatype.

print(tuple(dd.keys()))
print(tuple(dd.values()))

print(dd.get(10))
dd.