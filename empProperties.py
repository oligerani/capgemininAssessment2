class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def display(self):
        print(f"empoye Name:{self.name} employee id{self.id} employee department:{self.department}")
name=input("enter name") 
id=int(input("enter id"))
dep=input ("enter departent")
ob=Employee(name,id,dep)


ob.display()
        