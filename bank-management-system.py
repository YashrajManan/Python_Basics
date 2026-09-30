def menu():
    print("WELCOME TO BOI*")
    print("1. Open Your Bank account")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check current balance")


def select_option(op, data):
    
    if op == 1:
        name= input("Enter your name:")
        am  = int(input("Enter amount: "))
        
        name= name.lower()
        data[name]= Bank(am)
        
    elif op==2:    
        name= input("Enter your name:")
        
        if name not in data:
            print("No bank account found!!")
            return 0
        am  = int(input("Enter amount: "))
        data[name].deposite(am)    
        
    elif op==3:    
        name= input("Enter your name:")
        
        if name not in data:
            print("No bank account found!!")
            return 0
        am  = int(input("Enter amount: "))
        data[name].withdraw(am) 
    elif op==4:    
        name= input("Enter your name:")
        bn=   input("Enter benficiary name:")

        if name not in data or bn not in data:
            print("No bank account found!!")
            return 0
        am  = int(input("Enter amount: "))
        data[name].transfer(am,data[bn]) 
    elif op==5:        
        name= input("Enter your name:")
        
        if name not in data:
            print("No bank account found!!")
            return 0
       
        data[name].current_balance() 
    
    else:
        print("Invalid")
        return 0
    
class Bank:
    
    def __init__(self,am):
        self.balance= am
    
    
    def deposite(self,am):
        self.balance+= am
    
    def withdraw(self,am):
        net_amount= self.balance -1000
        
        if am <=self.balance-1000:
            self.balance -= am
            
        else:
            print("Insufficient Balance")
    
    def transfer(self,am,benficiary):
        
        net_amount= self.balance-1000
        
        
        if am<=net_amount:
            self.balance-= am
            benficiary.balance += am
    
    def current_balance(self):
        print("Balance: ",self.balance)

d= {}

while True:
    
    menu()
    op= int(input("Enter your choice: "))
    
    x= select_option(op,d)   
    
    if x==0:
        print("Try again!!")
        break
    else:
        print("Success!!")