# Self-->

# In Python Object-Oriented Programming,self represents the current object of the class.It is used to access variables and methods inside the class.
# When we create an object,Python automatically passes the object reference as the first argument to methods.By convention, we call it self (but you can name it anything).

class calculator():
    
    def add(self,a,b):
        print(a+b)
        
    def sub(self,a,b):
        print(a-b)
    
    def mul(self,a,b):
        print(a*b)
    
    def div(self,a,b):
        print(a/b)
    
    def mds(self,a,b):
        print(a%b)
    
    def flrdiv(self,a,b):
        print(a//b)
    
    def exp(self,a,b):
        print(a**b)
    
    def describe(self):
        print(self.model_no)
        print(self.made_in)
        print(self.color)
        print(self.discount)

cal1=calculator()
cal2=calculator()

cal1.model_no="A101"
cal1.made_in="Japan"
cal1.color="Silver"
cal1.discount="15%"

cal2.model_no="B202"
cal2.made_in="Germany"
cal2.color="Black"
cal2.discount="5%"

cal1.add(10,20)
cal1.sub(15,12)
cal1.mul(12,9)
cal1.div(5,4)
cal1.mds(15,25)
cal1.flrdiv(60,20)
cal1.exp(14,3)
cal1.describe()


cal2.add(5,4)
cal2.sub(15,3)
cal2.mul(16,6)
cal2.div(40,20)
cal2.mds(21,3)
cal2.flrdiv(6,4)
cal2.exp(10,6)
cal2.describe()


