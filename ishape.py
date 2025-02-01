from abc import  ABC,abstractmethod
class Ishape:
    def __init__(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Ishape):
    
          
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
           
        return self.length*self.breadth
class Circle(Ishape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):    
        return 3.1415*self.radius*self.radius
ob1=Rectangle(5,6)
print(ob1.calculate_area())  
ob=Circle(5)
print(ob.calculate_area()) 
      
        
        
