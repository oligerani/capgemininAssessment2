class BankAccount:
    def __init__(self):
        self.l=[]
        
    def deposit(self,money):
        self.money=money
        
        
        self.l.append(money)
        
    def withdraw(self,money):
        if money < sum(self.l):
            print("transaction successful")  
            
        else:
            print("insuffiecnt balance")

            
ba=BankAccount()             
deposit_money=int(input("enter amount"))


ba.deposit(deposit_money)
withdraw_money=int(input("enter money to be withdrawn"))
ba.withdraw(withdraw_money)
            
             
        