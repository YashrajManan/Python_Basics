# question 1 Find the factorial of a given number.

def factorial(x):
    if x == 1: 
        return 1 
    else: 
        return x*factorial(x-1)
x = int(input("enter the number: "))
y = factorial(x)
print(y) 

# as well as

factorial = 1
num = int(input("enter the number: "))
for i in range(1,num+1):
    factorial*=i
print(factorial)

# question 2 Write a program that keeps on accepting a number from the user until the user 
#            enters Zero. Display the sum and average of all the numbers.

sum_total = 0
count = 0
while True: 
    num = int(input("enter the number: "))
    if num == 0:
        break 
    sum_total += num
    count += 1
if count>0: 
    avg = sum_total/count
else: 
    avg = 0
print(sum_total)
print(avg)  

# question 3 Reverse a given integer number

num = int(input("enter the number: "))
n = str(num)
x = n[::-1]
print(x)

# question 4 Write a program that will take user input of cost price and selling price and
#           determines whether its a loss or a profit.

cost_price = int(input("enter the cost price: "))
selling_price = int(input("enter the selling price: "))

if cost_price>selling_price: 
    print("This deal was a loss")
elif cost_price<selling_price:
    print("This deal was a profit")
else: 
    print("This deal was neither loss nor profit")
    
# question 5 Write a program that take a user input of three angles and will find out 
#           whether it can form a triangle or not. 

angle_1 = int(input("enter the value of first angle: "))
angle_2 = int(input("enter the value of second angle: "))
angle_3 = int(input("enter the value of third angle: "))

if angle_1 + angle_2 + angle_3 == 180:
    print("The following angles can form a triangle")
else: 
    print("The following angles cannot form a triangle")
    
# question 6 Write a program to find the sum of squares of first n natural numbers where n
#            will be provided by the user.

num = int(input("enter the number: "))
i = 1
sum_total = 0
while i <= num:
    sum_total += (i**2) 
    i+=1 
print(sum_total)

# question 7 Given 2 fractions, find the sum of those 2 fractions. Take the numerator and 
#            denominator values of the fractions from the user.

num_1 = int(input("enter the numerator 1: "))
denum_1 = int(input("enter the denominator 1: "))
num_2 = int(input("enter the numerator 2: "))
denum_2 = int(input("enter the denominator 2: ")) 

total_sum = ((num_1/denum_1) + (num_2/denum_2))
print(total_sum)

# question 8 Take a user input as integer N. Find out the sum from 1 to N. If any number is divisible by 5, then 
#            skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. 
#            Print the final result. And don't use for loop to solve this problem. 

N = int(input("enter the number: "))
i = 1 
sum_total = 0 

while i<=N: 
    if i%5==0:
        i+=1
        continue
    sum_total+=i 
    
    if sum_total>300:
        break 
    i+=1 

print(sum_total)

# question 9 Pint the following pattern. Write a program to use for loop to print the following reverse number 
#            pattern.
#            5 4 3 2 1
#            4 3 2 1
#            3 2 1
#            2 1
#            1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end="")
    print()

# question 10 Print the following pattern.
#             *
#             * *
#             * * *
#             * * * *
#             * * * * *
#             * * * *
#             * * *
#             * *
#             *

for i in range(0,6):
    for j in range(i):
        print("*", end="")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*", end="")
    print()