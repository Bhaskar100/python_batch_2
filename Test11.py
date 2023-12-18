
class Test11():

    def __init__(self):
        print('Constructor..')

    def __str__(self):
        return 'helloworld'


    def __del__(self):
        print('Object destroyed')


t = Test11()
print(t)
