
from A import A

class B(A):
    y=20

    def m2(self):
        print('in parent class B m2 method')


v = B()
print(v.x)
