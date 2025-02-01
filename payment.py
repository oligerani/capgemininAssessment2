#  Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
class Payment:
    def process_payment(self):
        pass
class Creditcard(Payment):
    def process_payment(self):
        print("paymnet done via credit card")
class PaypalPayment(Payment):
    def process_payment(self):
        print("paymnet done via Paypal ")
class BitcoinPaymnet(Payment):
    def process_payment(self):
       print("payment done via Bitcoin")   
ob=BitcoinPaymnet()
ob.process_payment()          
        