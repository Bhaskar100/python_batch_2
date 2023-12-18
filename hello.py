
x = 2
def hi(): # outer function
    x = 5
    def hello(): # inner function or nested function
       nonlocal x
       x=10
       print(x)
    hello() # inner function calling
    print(x)

hi() # outer function calling
print(x)
