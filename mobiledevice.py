#Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    def __init__(self,brand):
        self.brand=brand
        
    def display (self) :
        print(f'brand:{self.brand}')  
        
        
class Smarphone(Electronics):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model=model
    def display(self):
        print(f'brand:{self.brand} model:{self.model} ')
            
        
       
class MobileDevice(Smarphone):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery=battery
    def display(self):
        print(f'brand:{self.brand} model:{self.model} battery{self.battery} ')
    def reuse_attributes(self):
        return {
            "Brand": self.brand,
            "model":self.model,
            
            "Battery": f"{self.battery}mAh",
            
            
        }    
ob=MobileDevice("iphone","15pro","100%")
ob.display()
print(ob.reuse_attributes())
        
        
 


