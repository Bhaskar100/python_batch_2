

class State():

    def capital(self):
        pass

    def language(self):
        pass


class Karantaka(State):

    def capital(self):
        print('Banglore')

    def language(self):
        print('kannada')


class AP(State):

    def capital(self):
        print('Amaravati')

    def language(self):
        print('Telugu')


a = AP()
a.capital()

k = Karantaka()
k.capital()

