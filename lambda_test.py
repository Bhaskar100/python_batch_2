
def f(x):
    print(x**2)
f(3)

g = lambda x,y:x+y
print(g(3,4))

#filter
#map

s = lambda a,b: a if a>b else b
print(s(5,6))

my_list = [1,5,4,6,8,11,3,12]

new_list =tuple(filter(lambda x:(x%2==0),my_list))
print(new_list)

def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l1 = list(filter(isEven,my_list))
print(l1)

ls = ['ratan','anu','durga']

ss = list(filter(lambda x:'hello' in x,ls ))
print(ss)



def doubleIt(l):
    for i in l:
     print(i*2)
l = [2,4,6,8]
doubleIt(l)


def m1(x):
    return 2*x
ll = list(map(m1,l))
print(ll)

l2 = list(map(lambda x:x*2,l))
print(l2)

ls2 = ['ratan','anu','durga']
ls4 = list(map(lambda x:x + "it",ls2))
print(ls4)




