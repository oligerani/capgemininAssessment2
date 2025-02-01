#Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
         self.side=side
    def area(self):
           
        self.side*self.side
        
        
        return self.side*self.side
class Triangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    
    def area(self):
        return 0.5 * self.l * self.b 
            
        
    
ob= Square(4)
print(ob.area())
ob1=Triangle(5,6)
print(ob1.area())    
         
    
        