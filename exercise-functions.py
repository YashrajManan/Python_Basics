def isprime(x):
    factor= 0
    
    for i in range(1,x+1):
        
        if x%i==0:
            factor+=1
    
    
    if factor==2:
        return True
        
def isarmstrong(x):
    digits = str(x)
    power = len(digits)
    total = 0 
    for digit in digits: 
        total+= int(digit)**power
    return total==x
    
def isperfect(x): 
    if x<= 0: 
        return False 
    sum_divisors = 0 
    for i in range(1,x): 
        if x%i==0: 
            sum_divisors+=i 
    return sum_divisors == x 
    
def numbers(num):
    prime = isprime(num)
    armstrong = isarmstrong(num)
    perfect = isperfect(num) 

    if prime: 
        print("the number is prime no.")
    if armstrong: 
        print("the number is armstrong no.")
    if perfect: 
        print("the number is perfect no.")
    if not (prime or armstrong or perfect): 
        print("the number is neither of the 3 categories")
num=int(input("enter the number: ")) 
numbers(num)

    



