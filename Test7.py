
tp = tuple([1,5,4,3,2,9,5])
tp1 = (3,4,5,6,8)
print(tp1)
print(type(tp))
print(tp)
print(tp[2:4])
#tp[2]=8

res1 = [i for i in tp]
print(res1)

for i in tp:
    print(i)

print(tp.count(5))
print(tp.index(2))
print(len(tp))
print(min(tp))
print(max(tp))
print(sum(tp))
print(sorted(tp))