
# User defined exception
class InvalidAgeEx(Exception):
    def __init__(self,age):
        super().__init__()
        self.age = age