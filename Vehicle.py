class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f'car name:{self.brand}\n model{self.model}')    
        
class Car(vehicle):
    def __init__(self, brand, model,color):
        super().__init__(brand, model)  
        self.color=color
    def start(self):
        print (f'brand:{self.brand} \n model:{self.model} color is {self.color}')
class Bike(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def bike_info(self):
        print(f" brand:{self.brand} \nbike model:{self.model} ") 
class Electricar(Car):
    def __init__(self, brand, model, color,engine):
        super().__init__(brand, model, color)  
        self.engine=engine
    def dispaly_Ele(self):
        print(f'barnd:{self.brand} \nmodel:{self.model} \ncolor:{self.color} engine{self.engine}')
print("electic CAr details")
ob=Electricar("toyota","camry","black",126)
ob.dispaly_Ele()
print()
print("bike details")
ob1=Bike("yamaha","r15")
ob1.bike_info()
print()
print("car details")
#c=Car("hyundai","sonata","blue")
ob.start()

                         
    
             