class Product:
    def __init__(self, quantity,price,stock):
        self.quantity=quantity
        self.price=price
        self.stock=stock
    def check_avaialability(self,quantity):
        if quantity <=self.stock: 
            print("the reqesuted quantity is available")  
        else:
            print("not available")     

quantity=int(input("enter the quantity"))
price=int(input("enter the cost"))
stock=int(input("enter stock"))
ob=Product(quantity,price,stock)

ob.check_avaialability(quantity)            