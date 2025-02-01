class Person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def dispaly(self):
        print(f'name:{self.name}\n salary{self.salary}')
class Employee(Person):
    def __init__(self, name, salary,id):
        super().__init__(name, salary)            
        self.id=id
    def dispaly_info(self):
        print(f'name:{self.name}\n salary{self.salary} \n id:{self.id}')
class Manager(Employee):
    def __init__(self, name, salary, id):
        super().__init__(name, salary, id) 
    def dispaly_info_manager(self):
            print(f'name:{self.name}\n salary{self.salary} \n id:{self.id}')    
    def approve(self,days):
        self.days=days
        print(f'name{self.name} is approved with {self.days} leave')
ob=Manager("anu",20000,123)
ob.dispaly_info_manager()
ob.approve(12)
        
                      
        