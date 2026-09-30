# Create a class Car with attributes brand and year. Add a method display_info() to print these values.

# class car: 
#     def display_info(self):
#         print(f"brand name: {self.brand}")
#         print(f"year: {self.year}")

# car1= car()
# car2= car()

# car1.brand="TATA"
# car1.name="SAFARI"
# car1.year=2000
# car1.price=1500000

# car2.brand="MAHINDRA"
# car2.name="THAR"
# car2.year=2010
# car2.price=2500000

# car1.display_info()
# print("\n")
# car2.display_info()

# Create a class Student with attributes name and marks. Add a method get_grade() that returns "Pass" if marks >= 40  "Fail".

# class student: 
#     def get_grade(self):
#         if self.marks >= 40:
#             print(f"{self.name}: pass" )
#         else: 
#             print(f"{self.name}: fail")

# std1=student()
# std2=student()
# std3=student()

# std1.name="Yashraj"
# std1.marks= 90.16

# std2.name="Saumya"
# std2.marks= 100 

# std3.name="Aniket"
# std3.marks=39

# std1.get_grade()
# std2.get_grade()
# std3.get_grade()

# Write a class Rectangle with attributes length and width. Add a method area() that returns the area.

# class rectangle:
#     def area(self):
#         print(f"the area of {self.name} is {self.length*self.width}")
# rec1= rectangle()
# rec2= rectangle()

# rec1.name= "rectangle1"
# rec1.length= 10
# rec1.width= 5

# rec2.name="rectangle2"
# rec2.length= 10
# rec2.width= 7

# rec1.area()
# rec2.area()

# Write a class Circle that has a radius attribute and a method get_circumference() (use pie = 3.14).

# class circle:
#     def get_circumference(self):
#         print(f"the circumference for {self.name} is {6.28*self.radius}")

# c1 = circle()
# c2 = circle()

# c1.name= "circle1"
# c1.radius=5 
# c2.name= "circle2"
# c2.radius=10 

# c1.get_circumference()
# c2.get_circumference()

# Create a class Employee with attributes name, salary. Add a method give_raise(amount) that increases the salary.

# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         print(f"employee name: {self.name}")
#         print(f"employee salary: {self.salary}")
#         print("\n")
#     def give_raise(self):
#         amount = int(input("enter the amount: "))
#         print(f"the updated salary for {self.name} is: {self.salary+amount}")
# e1=employee("Yashraj",400000)
# e2=employee("Bhavya",450000)

# e1.give_raise()
# e2.give_raise()

# Write a class Book with attributes title, author, and a method description() that prints a summary.

# class Book: 
#     def __init__(self, title, author, genre):
#         self.title = title 
#         self.author = author 
#         self.genre =  genre 
#         print(f" Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f" Genre: {self.genre}")
#         print("\n")

# B1 = Book("ALCHEMIST","PAULO COELHO","NOVEL,ADVENTURE FICTION")
# B2 = Book("THE PERSONAL MBA","JOSH KAUFFMANN","NON-FICTION, FINANCE, SELF=HELP, BUSSINESS, ECONOMICS")
# B3 = Book("SAPIENS","YUVAL NOAH HARARI","HISTORY, ANTHROPOLOGY, PHILOSOPHY") 

# Create a class Rectangle with methods to calculate area and perimeter.

# class rectangle: 
#     def __init__(self, name, length, breadth):
#         self.name = name
#         self.length = length 
#         self.breadth = breadth 
#         print(self.name)
#         print(self.length)
#         print(self.breadth)
#         print("\n")
#     def area(self):
#         print(f"the area for rectangle {self.name} is : {self.length*self.breadth}")
#     def perimeter(self):
#         print(f"the perimeter for rectangle {self.name} is : {2*self.length+self.breadth}")
#     print("\n")
# R1 = rectangle("Rectagnle 1", 10, 20)
# R2 = rectangle("Rectagnle 2", 5, 15)
# R3 = rectangle("Rectagnle 3", 15, 25)

# print(R1.__dict__)
# R1.area()
# R1.perimeter()
# print(R2.__dict__)
# R2.area()
# R2.perimeter()
# print(R3.__dict__)
# R3.area()
# R3.perimeter()
    
# Create a class BankAccount with deposit and withdraw methods.

# class BankAccount:
#     def __init__(self):
#         self.accounts = []

#     def add_account(self, name, account_number, balance):
#         account = {
#             "name": name,
#             "account_number": account_number,
#             "balance": balance
#         }
#         self.accounts.append(account)
#         print(f'Bank account for "{name}" (Account No.: {account_number}) has been created.')

#     def remove_account(self, account_number):
#         for account in self.accounts:
#             if account["account_number"] == account_number:
#                 self.accounts.remove(account)
#                 print(f'Bank account for "{account["name"]}" (Account No.: {account_number}) has been removed.')
#                 return
#         print("No such bank account found.")

#     def account_info(self):
#         if self.accounts:
#             print("The accounts currently running in this bank are:\n")
#             for index, account in enumerate(self.accounts, start=1):
#                 print(f'{index}. Name: {account["name"]}, Account No.: {account["account_number"]}, Balance: {account["balance"]}')
#         else:
#             print("The bank has no accounts.")

#     def deposit(self, account_number, amount):
#         for account in self.accounts:
#             if account["account_number"] == account_number:
#                 account["balance"] += amount
#                 print(f'Amount {amount} deposited. Updated balance in Account No.: {account_number} is {account["balance"]}')
#                 return
#         print("No such bank account found.")

#     def withdraw(self, account_number, amount):
#         for account in self.accounts:
#             if account["account_number"] == account_number:
#                 if amount <= account["balance"]:
#                     account["balance"] -= amount
#                     print(f'Amount {amount} withdrawn. Updated balance in Account No.: {account_number} is {account["balance"]}')
#                 else:
#                     print("Insufficient balance for withdrawal.")
#                 return
#         print("No such bank account found.")

# bank = BankAccount()

# bank.add_account("Yashraj", "12345", 1500)
# bank.add_account("xy", "67890", 500)
# bank.add_account("xx","9870",7000)

# bank.account_info()

# bank.deposit("12345", 45000)
# bank.withdraw("9870", 4000)

# bank.withdraw("67890", 1000)  # will show insufficient balance
# bank.remove_account("67890")
# bank.account_info()

# Create a class Movie that stores the title, director, and year. Add a method to check if it’s older than 10 years. 

# class movie:
#     def __init__(self, title, director, year):
#         self.title = title 
#         self.director = director 
#         self.year = year  
        
#         print(f" title: {self.title}")
#         print(f" director: {self.director}")
#         print(f" year: {self.year}") 
#         print("\n")
        
#     def isold(self):
#         if self.year >10:
#             print(f" the movie {self.title} is more than 10 years old.")
#         else:
#             print(f" the movie {self.title} is not more than 10 years old") 
#         print("\n")

# m1 = movie("BORDER", "JP DUTTA", 28)
# m2 = movie("PALTAN", "JP DUTTA", 8)
# m3 = movie("BELL BOTTOM", "RANJIT TIWARI", 4)

# print(m1.__dict__)
# m1.isold()
# print(m2.__dict__)
# m2.isold()
# print(m3.__dict__)
# m3.isold()

# Create a class Library that stores a list of books and has methods to add, remove, and display them. 

# class Library: 
#     def __init__ (self):
#         self.books = []

#     def add_book(self, name):
#         self.books.append(name)
#         print(f' The book "{name}" has been added in the library')
#         print("\n")
#     def remove_book(self, name):
#         if  name in self.books:
#             self.books.remove(name)
#             print(f' The book "{name}" has been removed from library')
#             print("\n")
#         else: 
#             print(f' The book "{name}" nor found in library')
#             print("\n")
#     def display_books(self):
#         if self.books: 
#             print("The books currently in library: ")
#             print("\n")
#             index =1 
#             for book in self.books:
#                 print(index, book)
#                 index+=1 
#         else: 
#             print("The library is empty") 
#         print("\n")
        
# Library = Library()

# Library.add_book("SAPIENS")
# Library.add_book("HOMO DEUS")
# Library.add_book("THE UNENDING GAME")
# Library.add_book("THE INDIA WAY")
# Library.add_book("KITNE GHAAZI AAYE KITNE GHAAZI GAYE")
# Library.add_book("WAFADAARI, IMAANDAARI, ZIMMEDAARI")
# Library.add_book("A CRACK IN CREATION")
# Library.add_book("WHAT IS LIFE ?")
# Library.add_book("GOING VIRAL")
# Library.add_book("INDIA THAT IS BHARAT")
# Library.add_book("OBSTACLE IS THE WAY")
# Library.add_book("THE THEORY OF EVERYTHING")
# Library.add_book("INNER ENGINEERING")
# Library.display_books() 

# Library.remove_book("INNER ENGINEERING")
# Library.remove_book("KITNE GHAAZI AAYE KITNE GHAAZI GAYE")
# Library.remove_book("GOING VIRAL")
# Library.remove_book("INDIA THAT IS BHARAT")
# Library.display_books() 
