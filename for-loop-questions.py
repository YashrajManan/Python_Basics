# question 1
for x in range(11):
    print(x, end=" ")

print("\n")

# question 2
for x in range(10, -1, -1):
    print(x, end=" ")

print("\n")

# question 3
for x in range(65, 91):
    print(chr(x), end=" ")

print("\n")

# question 4
for x in range(2, 101, 2):
    print(x, end=" ")

print("\n")

# question 5
for x in range(1, 100, 2):
    print(x, end=" ")

print("\n")

# question 6
totalsum = 0
for x in range(1, 26):
    totalsum += x
print(totalsum)

# question 7
totalsum = 0
for x in range(2, 11, 2):
    totalsum += x
print(totalsum)

# question 8
totalsum = 0
for x in range(1, 10, 2):
    totalsum += x
print(totalsum)

# question 9
num = int(input("enter the number: "))
for x in range(1, 11):
    print(x * num)

# question 10
sum_total=0
num=input("enter the no. :")
for x in str(num):
    sum_total+=1 
print(sum_total)

# question 11 
num=int(input("enter the no. :"))
original_num = num
last_digit= num%10
for i in range(num):
    if num < 10:
        first_digit= num
        break 
    else: num= num//10
print(first_digit, last_digit)

# question 12 
num=int(input("enter the no. :"))
original_num = num
last_digit= num%10
for i in range(num):
    if num < 10:
        first_digit= num
        break 
    else: num= num//10
print(first_digit + last_digit)