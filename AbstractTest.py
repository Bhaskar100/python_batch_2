# Import required modules
from abc import ABC, abstractmethod


# Create Abstract base class
class TV(ABC):
    def __init__(self,model):
        self.model = model



    # Create abstract method
    @abstractmethod
    def printDetails(self):
        pass


    # Create concrete method
    def color(self):
        print("color tv...")



# Create a child class
class Samsung(TV):


    def printDetails(self):
        print("Model:", self.model);

    def printDetails(self):
        print(self.model)


# Create a child class
class LG(TV):


    def printDetails(self):
        print("Model:", self.model)

    def printDetails(self):
        print(self.model)




tv = TV()
tv.color()

tv1 = Samsung("LED");
tv1.printDetails()
tv1.color()

tv2 = LG('OLED')
tv2.printDetails()
tv2.color()




