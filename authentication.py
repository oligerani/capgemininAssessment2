#Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self,username,password):
        pass
    @abstractmethod
    def logout(self,username):
        pass
class GoogleAuth(UserAuthentication):
    def login(self,username,password):
        return f'username:{username} \n password:{password}'  
    def logout(self,username):
        return f'username:{username}'
class FacebookAuth(UserAuthentication): 
    def login(self,username,password):
        return f'username:{username} \n password:{password}'  
    def logout(self,username):
        return f'username:{username}'
ob=FacebookAuth()
print(ob.login("ammu",123456))
print(ob.logout("ammu"))
ob1=GoogleAuth()
print(ob1.login("ammu",123456))
print(ob1.logout("ammu"))    
    