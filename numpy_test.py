import numpy as np

b = np.array([[1,2,3],
 [4,5,6]])
print(b)
print(b.dtype)
print(b.shape)
print(b[0, 0], b[0, 2], b[1, 1])

b[0, 0] = 10
b[1, 1] = 20
print(b)

print(dir(np))
print(np.zeros((2,2)))

c = np.full((2,2), 7)
print(c)

d = np.eye(2)
print(d)

d = np.eye(3)
print(d)

e = np.random.random((2,2))
print(e)

e = np.random.randint(1,10,(3,2))
print(e)

e = np.random.uniform(5,10,(2,3))
print(e)

data1 = np.arange( 10, 30, 5 )
print(data1)
print(type(data1))


a = np.array([[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]])

print(a.shape)

row_r1 = a[1, :]
print(row_r1)
row_r2 = a[1:2, :]
print(row_r2)

print('--- addition opertain with numpy add')

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(x)
print(y)
print('--------------')
print(x + y)
print(np.add(x, y))