class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
       
    def display(self):
        return(f'student name:{self.name} \n roll no:{self.roll_no}') 
name=input("enter your name")
roll_no=int(input("enter your rll no"))
book=Student(name,roll_no)
print(book.display())        