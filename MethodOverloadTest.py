
class MethodOverloadTest():

    def add(self,a,b,c = 0):
       return a+b+c


c = MethodOverloadTest()
v = c.add(2,3)
print(v)