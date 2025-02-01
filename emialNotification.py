# Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        pass
class EmailNotification(Notification):
    def __init__(self,message):
        self.message=message
    def send(self):
        print(f'recived email notificatoin of {self.message}')
class  SMSNotification(Notification):
    def __init__(self,message):
         self.message=message
    def send(self):
       print(f"recoved sms notification{self.message}")
ob=SMSNotification()
ob.send("successfully sent")
ob1=EmailNotification("delivered")
ob1.send()       
       
        