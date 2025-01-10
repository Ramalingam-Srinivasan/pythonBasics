from abc import ABC,abstractmethod
print(__name__)

#this is abstract class method example we
# have to import ABC class and abstqarct method and implement that in our child class

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class bike(vehicle):

    color = None
    def showroom(self):
        print("virugambakkam showroom")
    def start(self):
        print("bike start....")

    def stop(self):
        print("stop the bike")


class car(vehicle):
    color = None
    def start(self):
        print ("start the car...")
    def stop(self):
        print("stop the car...")

bike1 = bike()


