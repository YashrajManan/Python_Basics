# 🔹 Basic Function Questions

# Write a function to return the square of a number.
# def square(x):
#     return (x**2)
# x= int(input("enter the number: "))
# y= square(x)
# print(y)

# Write a function that takes two numbers and returns their sum.
# def add(a,b):
#     return (a+b) 
# a= int(input("enter the first no.: "))
# b= int(input("enter the second no.:"))
# x= add(a,b)
# print(x)

# Write a function to check if a number is even or odd.
# def even_odd(x): 
#     if x%2==0:
#         return "number is even"
# x=int(input("enter the number: "))
# y= even_odd(x)
# print(y)

# Write a function that takes a string and prints each character on a new line.
# def str_ing(x):
#     for i in range(len(x)):
#         print(x[i])
# x=input("enter the string: ")
# str_ing(x)

# Write a function to find the factorial of a number.
# def factorial(x):
#     i=1 
#     total=1
#     while i<=x:
#         total*=i
#         i+=1
#     return total 
# x=int(input("enter the number: "))
# y=factorial(x)
# print(y)

# 🔹 Parameter & Return Type Practice

# Write a function that takes a name and age as input and prints a greeting message.
# def name_age(name, age):
#     return (f"Hello! I am {name}and I am {age} years old, nice to meet you!")
# name=input("enter the name: ")
# age= int(input("enter the age: "))
# greeting= name_age(name,age)
# print(greeting)

# Write a function that takes a list of numbers and returns the maximum number.
# def find_maximum(x):
#     max_num = x[0]
#     for i in x :
#         if x > max_num:
#             max_num = x
#     return max_num
# size = int(input("Enter how many numbers you want in the list: "))
# x = [] 
# for i in range(size):
#     item = int(input(f"Enter number {i + 1}: "))
#     x.append(item)
# maximum = find_maximum(x)
# print(f"The maximum number in the list is {maximum}")

# Write a function that takes a number n and returns a list of all numbers from 1 to n divisible by 3.
# def div3(x):
#     if x%3==0:
#         return True
#     else:
#         return False
# start=int(input("enter the starting range: "))
# end=int(input("enter the ending range: "))
# my_list=[]
# for x in range(start, (end+1)):
#   if div3(x) == True:
#       my_list.append(x)
# print(my_list)

# Write a function that accepts a string and returns it reversed. 
# def ulta(x):
#         return (x[::-1])
# x = input("enter the string: ")
# y = ulta(x)
# print(y)

# Write a function that takes a list and returns the number of unique elements.
# def unique(x):
#     mylist = []
#     for i in x:
#         if i not in mylist:
#             mylist.append(i)
#     return len(mylist)

# size = int(input("Enter how many numbers you want in the list: "))
# x = [] 
# for i in range(size):
#     item = int(input(f"Enter number {i + 1}: "))
#     x.append(item) 
# y = unique(x) 
# print(y)

# 🔹 Logic & Conditionals
# Write a function to check if a number is prime.

# Write a function to return whether a string is a palindrome.

# Write a function that returns the GCD of two numbers.

# Write a function to check if two strings are anagrams.

# Write a function that returns the sum of digits of a given number.

# 🔹 Nested Functions & Higher Logic
# Write a function that takes a string and returns the count of vowels and consonants.

# Write a function to return the Fibonacci series up to n terms.

# Write a function that accepts a list of numbers and returns a new list with only even numbers.

# Write a function to return the frequency of each character in a string 

# # Write a function that takes a sentence and returns the word with the maximum length.