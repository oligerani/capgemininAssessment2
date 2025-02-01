class Car:
    def move(self):
        print("this a normal car")
class defAieplane:
    def move(self):
        print("this is a defAIRPLANE Car")  
        super().move()   
class FlyingCar(Car,defAieplane):
    def move(self):
        print("it has the both features")
        super().move()
ob=FlyingCar()
ob.move()                   