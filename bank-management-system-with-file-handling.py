import os
import random
import datetime
import hashlib
import json
from getpass import getpass

ACCOUNTS_FILE= "accounts.dat"
TRANSACTIONS_FILE= "transactions.dat"


class Account:
    
    def __init__(self, acc_no,name,pin,balance=0.0,acc_type="Savings"):
        
        self.acc_no= acc_no
        self.name= name
        self.pin= pin
        self.balance= balance
        self.acc_type= acc_type
        self.created_at= datetime.datetime.now().strftime("%d/%m/%Y %H:%M %P")
        


    def to_dict(self):
            
        return {
            "acc_no" : self.acc_no,
            "name"   : self.name,
            "pin"    : self.pin,
            "balance": self.balance,
            "acc_type":self.acc_type,
            "created_at":self.created_at
        }
    
    @classmethod
    def from_dict(cls,data):
        
        return cls(
            data["acc_no"],
            data["name"],
            data["pin"],
            data["balance"],
            data["acc_type"]
        )
    
class Transaction:
    
    def __init__(self,acc_no,amount,transaction_type,description=""):
        
        self.acc_no= acc_no
        self.amount= amount
        self.transaction_type= transaction_type
        self.description= description
        self.timestamp= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "amount": self.amount,
            "transaction_type":self.transaction_type,
            "description": self.description,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls,data):
        return cls(
            data["acc_no"],
            data["amount"],
            data["transaction_type"],
            data["description"]
        )
    
    
#File Operations
def load_accounts():
    
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
        
    
    with open(ACCOUNTS_FILE,"r") as file:
        
        encrypted_data= file.read()
        
        if encrypted_data:
            
            decrypted_data= json.loads( encrypted_data[::-1] )
            
            return { acc["acc_no"]: Account.from_dict(acc)  for acc in decrypted_data}

        return {}


def save_accounts(accounts):
    
    accounts_list= [ acc.to_dict() for acc in accounts.values()]
    
    encrypted_data= json.dumps(accounts_list)[::-1]
    
    with open(ACCOUNTS_FILE,"w") as file:
        
        file.write(encrypted_data)
        
        
def load_transactions():
    
    if not os.path.exists(TRANSACTIONS_FILE):
        return []
    
    with open(TRANSACTIONS_FILE,"r") as file:
        
        encrypted_data= file.read()
        
        if encrypted_data:
            decrypted_data= json.loads(encrypted_data[::-1])
        
            return [ Transaction.from_dict(txn) for txn in decrypted_data ]
    
def save_transaction(transactions):
    
    transactions_list= [ txn.to_dict()  for txn in transactions]
    
    encrypted_data= json.dumps(transactions_list)[::-1]
    
    with open(TRANSACTIONS_FILE,"w"):
        file.write(encrypted_data)
        

#HELPER FUNCTION
def genrate_account_number():
    
    return ''.join([ str(random.randint(0,9))  for _ in range(10) ])
    
def hash_pin(pin):
    return hashlib.sha256( pin.encode() ).hexdigest()

def verify_pin(hashed_pin,user_pin):
    
    return hashed_pin == hash_pin(user_pin)
    
    
print( hash_pin("123") )  