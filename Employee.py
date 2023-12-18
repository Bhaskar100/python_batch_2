
class Employee():
    def __init__(self,empid,empname):
        self.empid = empid
        self.empname = empname

    def dispemp(self):
        print('empid ::' , self.empid)
        print('empname ::' , self.empname)


c=Employee(10,'Bhaskar')
c.dispemp()