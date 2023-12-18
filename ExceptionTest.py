import logging
from InvalidAgeEx import InvalidAgeEx

logging.basicConfig(filename='app.txt',level=logging.INFO)

age =int(input('Enter youre age'))

if age < 0:
    raise InvalidAgeEx("Provide positive nunber")

elif age > 18:
    logging.info('eligible for voting')

else:
    print('not eligble for voting age is not morethan 18',age)
