# homework 2

question 1: Write a program to capitalize the first letter of the string msg = "python is awesome".

string_msg="python is awesome"
print(string_msg)
new=string_msg.capitalize()
print(new)

question 2: Given a string msg = " Hello World ", remove the leading and trailing whitespaces and print the cleaned string.

string_msg=" Hello World "
print(string_msg)
new=string_msg.strip()
print(new)

question 3: Write a program that takes a string and prints the string in reverse order using slicing.

string_msg= str(input("enter the string:"))
print(string_msg)
print(string_msg[::-1])

question 4: Given a string name = "john", convert it to uppercase using a string method and print the result.

string_name="john"
print(string_name)
new=string_name.upper()
print(new)

question 5: Replace all occurrences of "apple" with "banana" in the string fruits = "apple, apple, orange".

string_fruits="apple,apple,orange"
print(string_fruits)
new=string_fruits.replace("apple","banana")
print(new)

question 6: Check whether the word "code" exists in the string text = "learn to code with python" and print True or False.

string_text="learn to code with python"
print("code" in string_text)

question 7: Extract and print only the word "World" from the string s = "Hello World" using slicing.

string_s="Hello World" 
print(string_s)
print(string_s[6:11])

question 8: Take input from the user as a string and print its length.

string_input= str(input("enter the string input:"))
print(string_input)
print(len(string_input))

question 9: Join the list ["Python", "is", "fun"] into a single string with space as separator using a string method.

list=["python", "is", "fun"]
print(list)
new= " ".join(list)
print(new)

question 10: Write a program to swap the case of each character in the string s = "PyThOn123".

string_s="PyThOn123"
print(string_s)
new=string_s.swapcase()
print(new)

question 11: Create a program to print the first and last character of any string entered by the user.

string_input= str(input("kindly enter the input please:"))
print(string_input)
print(string_input[0], string_input[-1])

question 12: Print only the even-positioned characters of the string s = "Programming" using slicing.

string_s="Programming"
print(string_s)
print(string_s[::2])

question 13: Center the string "Python" in a width of 20 characters using a string method and print it.

string_input="Python"
print(string_input)
new=string_input.center(20,"-")
print(new)

question 14: Write a program that counts the number of times "a" appears in the string msg = "banana and mango".

string_msg="banana and mango"
print(string_msg)
new=string_msg.count("a")
print(new)

question 15: Find the position of the first occurrence of "@gmail" in the email string email = "example@gmail.com".

string_email="example@gmail.com"
print(string_email)
new=string_email.find("@gmail")
print(new)  

question 16: Write a program to check if a string entered by the user is a valid identifier using isidentifier().

string_input=str(input("kindly enter the string please:"))
print(string_input)
new=string_input.isidentifier()
print(new)

question 17: Convert the multiline string to a single line and print it:
text = """Hello
Python
World"""

text = """Hello
Python
World""" 
print(text)
new=text.replace('\n','')
print(new)

or 

text = """Hello
Python
World""" 
print(text)
new=''.join(text.splitlines())
print(new)

question 18: Given a = "12345", check whether all characters are digits.

a="12345"
print(a)
new=a.isdigit()
print(new)

question 19: Use escape characters to print this output exactly:
Hello    "Python"
Let's code!

print("Hello\t\"Python\"\nLet's code!")

question 20: From the string sentence = "Data Science with Python", print the substring "Science" using slicing.

string_sentence= "Data Science with Python"
print(string_sentence)
print(string_sentence[5:12])


