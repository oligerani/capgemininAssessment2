#Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
from abc import ABC,abstractmethod
class IVehicle(ABC):
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
class Car(IVehicle):
    
    def start_engine(self):
        return f'engine is started.'
    def stop_engine(self):
        return f'engine is stopped.' 
class Bike(IVehicle):
    def start_engine(self):
        return f'engine is started.'
    def stop_engine(self):
        return f'engine is stopped.'
class Truck(IVehicle):
    def start_engine(self):
        return f'engine is started.'
    def stop_engine(self):
        return f'engine is stopped.'   
       
ob=Truck()
print(ob.start_engine())
print(ob.stop_engine()) 
print("bike details")
ob1=Bike()
print(ob1.start_engine())
print(ob1.stop_engine()) 
print("car ")
ob2=Car()
print(ob2.start_engine())
print(ob2.stop_engine()) 
     
        
        
          