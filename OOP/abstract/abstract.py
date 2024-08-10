from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You are driving a car.")


car = Car()
car.go()

# Abstract method should be overwritten by the child class