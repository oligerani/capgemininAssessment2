class Animal:
    def __init__(self):
        print("overriding the animals")
    def speak(self):
        print("it is a overriding method")
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        print("it says bow bow")
class Cat(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        print("it says mew mew")
ob=Cat()
ob.speak() 
ob1=Dog()
ob1.speak()              
                