import re

#print(dir(re))


"""
re.match() start of the string
re.search()
re.findall()
re.split()
re.sub()
re.compile()
"""

result = re.match(r'ratan','ratan sir is good')
print(result)
print(result.group(0))
print(result.start())
print(result.end())

result1 = re.match(r'ratan','durga sir is good')
print(result1)

result2 = re.search(r'ratan','Hi ratan sir is good')
print(result2)

result3 = re.search(r'ratan','Hi ratan sir is good,ratan is good teacher')
print(result3)

result4 = re.findall(r'ratan','Hi ratan sir is good,ratan is good teacher')
print(result4)

result5 = re.findall(r'durga','Hi ratan sir is good,ratan is good teacher')
print(result5)

ss='ratanit'
result6 = re.split(r'a',ss)
print(result6)


ss2 = 'durga world durga in india'
result7=re.sub(r'durga',r'ratan',ss2)
print(result7)

pattern = re.compile('ratan')
result8=pattern.findall('Hi ratan sir is good,ratan is good teacher')
print(result8)


result9= re.findall('\s','Hello World hi')
print(result9)

result10= re.findall('\S','Hello World hi')
print(result10)


result11= re.findall('\d','Hel2lo Worl1d hi3')
print(result11)

result12 = re.findall('\D','Hel2lo Worl1d hi3')
print(result12)

result13 = re.findall('[a-e]','Hel2lo Worl1d hi3')
print(result13)

result13 = re.findall('[^a-e]','Hel2lo Worl1d hi3')
print(result13)
