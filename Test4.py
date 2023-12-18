

# NameError
# IndexError
#TypeError

# when ever we perform string operations incorrectly we may get above error's

ss = 'hello'
print(ss[1:3])

"""
Traceback (most recent call last):
    print(se[1:3])
          ^^
NameError: name 'se' is not defined. Did you mean: 'ss'?


"""
"""
s1='hello'
print(len(s1))
print(s1[5])
"""
"""
Traceback (most recent call last):
    print(s1[5])
          ~~^^^
IndexError: string index out of range
el
5
"""

a=10
ss='hello'
print(a+ss)

"""
Traceback (most recent call last):
  File
    print(a+ss)
          ~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
el

"""
