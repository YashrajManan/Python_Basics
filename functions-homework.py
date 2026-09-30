#question 1
def mylist(x):
    return(sum(x))
answer= mylist([1,2,3,4,5])
print(answer)

#question 2
def yourlist(y):
    s=0
    for i in y:
        s+=i 
    return s 
answer= yourlist([1,2,3,4,5,6])
print(answer)

#question 3    
def number(x):
    if x%2==0:
        return "even no"
    else:
        return "odd no."

x= number(18)
print(x)

#question 4    
def number(x):
    j=1
    while j <=int(x): 
        i=0
        if j%x==0:
            i+=1
        j+=1 
    return i 
x= number(7)
print(x)
if x >2:
    print("not prime no.")
else: 
    print ("prime no.")

#codeforwin questions

#question 1    
def number(x): 
    return x**3
x = number(3)
print(x)

#question 2 
def number(r):
    diameter = (2*r)
    area = (3.14*(r**2))
    circumference = (2*(3.14*(r)))
    return diameter, area, circumference
result = number(3)
print(result)
    
#question 3
def bignsmall(x,y):
    if x>y: 
        return "x is big y is small"
    elif y>x: 
        return "y is big x is small"
    else: 
        return "both are same"
numbers=bignsmall(12,14)
print(numbers)

#question 4
def number(x):
    if x%2==0:
        return "even no"
    else:
        return "odd no."

#question 5
import math
def isprime(x):
    if x<=1:
        return False 
    for i in range(2,(int(x**0.5))+1):
        if x%i==0: 
            return False 
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
    
def number_properties(num):
    prime= isprime(num)
    armstrong= isarmstrong(num)
    perfect= isperfect(num)
    
    if prime: 
        print("the number is prime no.")
    if armstrong: 
        print("the number is armstrong no.")
    if perfect: 
        print("the number is perfect no.")
    if not (prime or armstrong or perfect): 
        print("the number is neither of the 3 categories")
num=int(input("enter the number: "))
number_properties(num)

#question 6
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def interval(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")


interval(1,99)

print("\n")

#question 7
def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

def is_strong(x):
    original = x
    total = 0
    while x > 0:
        digit = x % 10
        total += factorial(digit)
        x = x // 10
    return total == original

def interval(start, end):
    print(f"strong numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_strong(num):
            print(num, end=" ")

interval(1,99 )

print("\n")

#question 8
def is_armstrong(x):
    digits = str(x)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return total == x

def interval(start, end):
    print(f"armstrong numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num, end=" ")

interval(1,99 )

print("\n")

#question 9
def is_perfect(x):
    if x <= 1:
        return False
    sum_divisors = 0
    for i in range(1, x):
        if x % i == 0:
            sum_divisors += i
    return sum_divisors == x

def interval(start, end):
    print(f"perfect numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_perfect(num):
            print(num, end=" ")

interval(1,99 )

print("\n")

#question 10
def numbers(base, power):
    return (base**power)
answer = numbers(2,5)
print(answer)

#question 11
def naturalnumbers(x):
    for i in range(1,int(x+1)):
        print(i)
naturalnumbers(25)

#question 12
def rg(x):
    for i in range(int(x+1)):
        if i%2==0: 
            print(i,"even no.")
        else:
            print(i,"odd no.")
rg(20) 

#question 13
def num(x):
    j=0
    for i in range(x+1):
        j+=i 
    return j 
answer=num(20)
print(answer)

#question 14 
def num(x):
    j=0 
    y=0
    for i in range(x+1):
        if i%2==0:
            j+=i 
        else: 
            y+=i 
    return (j,y)
answer = num(20)
print(answer)

#question 15
def reverse_number(x):
    reverse = 0
    while x > 0:
        digit = x % 10             
        reverse = reverse * 10 + digit  
        x = x // 10                 
    return reverse

num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"Reverse of {num} is {reversed_num}")

#question 16 
def reverse_number(x):
    reverse = 0
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
    return reverse

def is_palindrome(x):
    return x == reverse_number(x)

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is NOT a Palindrome number.")

#question 17
def sum_digits(x):
    total=0
    while x>0:
        digit=x%10
        total+=digit 
        x=x//10 
    return total 
    
num=int(input("enter the no.: "))
result = sum_digits(num)
print(result)

#question 18
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
fact = factorial(num)
print(fact)

#question 19 
def fibonacci_nth(n):
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Enter the position (n) to get nth Fibonacci term: "))
fib = fibonacci_nth(n)
print(fib)

#question 20
def hcf(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = hcf(num1, num2)
print(f"GCD (HCF) of {num1} and {num2} is: {result}")

#question 21
def hcf(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def islcm(a, b):
    gcd = hcf(a, b)
    lcm = (a * b) // gcd
    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = islcm(num1, num2)
print(f"LCM of {num1} and {num2} is: {lcm_result}")

#question 22
def display_array(arr):
    print("Array elements are:")
    for element in arr:
        print(element, end=" ")

size = int(input("Enter the number of elements in the array: "))
array = []

for i in range(size):
    value = int(input(f"Enter element {i + 1}: "))
    array.append(value)

display_array([array])

#question 23
def sum_array(arr):
    total = 0
    for element in arr:
        total += element
    return total
    
size = int(input("Enter the number of elements in the array: "))
array = []

for i in range(size):
    value = int(input(f"Enter element {i + 1}: "))
    array.append(value)

result = sum_array(array)
print(f"Sum of array elements is: {result}")

#question 24
def find_max_min(arr):
    maximum = arr[0]
    minimum = arr[0]
    
    for num in arr[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum

size = int(input("Enter the number of elements in the array: "))
array = []

for i in range(size):
    value = int(input(f"Enter element {i + 1}: "))
    array.append(value)

max_value, min_value = find_max_min(array)

print(f"Maximum element is: {max_value}")
print(f"Minimum element is: {min_value}")


# pynative questions

#question 1
def info(name, age):
    print(f"The name is {name} and the age is {age}")
info("Yashraj", 22)

#question 2

#question 3 

#question 4 

#question 5 

#question 6 

#question 7 

#question 8

#question 9

#question 10

#question 11

#question 12

#question 13

#question 14

#question 15 

#question 16 

#question 17 

#question 18  







    
    
    