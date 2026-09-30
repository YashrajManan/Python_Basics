class Bank: 
    def __init__(self, current_balance):
        self.current_balance = current_balance 
        
    def deposit(self,amount): 
        self.current_balance+= amount 
    def withdraw(self,amount):
        net_amount = self.current_balance-amount-1000
        if net_amount > 0  and amount<net_amount:
            self.current_balance-=amount 
        else:
            print("insufficient balance")
            
    def printbalance(self):
        print(self.current_balance) 
        
b1 = Bank(2000)
b2 = Bank(3000)
b3 = Bank(500) 

b1.deposit(200)
b2.withdraw(2500)
b1.printbalance()


         
        
        