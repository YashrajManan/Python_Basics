#homework 3 if else questions

#question 1

num1= int(input("enter input1: "))
num2= int(input("enter input2: "))
if num1>num2: 
    print("maximum no is:", num1)
elif num1==num2:
    print("both are equal")
else: 
    print("maximum no is:", num2)

#question 2

num1= int(input("enter input1: "))
num2= int(input("enter input2: "))
num3= int(input("enter input3: "))
if num1>num2 and num1>num3:
    print("maximum no is:", num1)
elif num2>num1 and num2>num3:
    print("maximum no is:", num2)
elif num3>num1 and num3>num2: 
    print("maximum no is:", num3)

#question 3

num= int(input("enter the no.: "))
if num>1:
    print("the no. is poitive")
elif num==0:
     print("the no. is neither positive nor negative but zero(0)")
elif num<0:
     print("the no. is negative")

#question 4

num=int(input("enter the no.: "))
if num%5==0 and num%11==0:
    print("the no. is divisible by 5 and 11")
else:
    print("the no. is not divisible by 5 and 11")

#question 5

num=int(input("enter the no.: "))
if num%2==0:
    print("the no. is even")
else:
    print("the no. is odd") 

#question 6

Year=int(input("enter the year: "))
if Year%4==0 and Year%100!=0 or Year%400==0:
     print("the entered year is leap year")
else:
     print("the entered year is a common year")

#question 7

character=input("enter the character: ")
if character.isalpha():
    print("the character is alphabet")
else:
    print("the character is not alphabet")
    
#question 8

character=input('enter the character: ')
if character.isalpha():
    print("the character is alphabet")
elif character.isalnum():
    print("the character is number")
else:
    print("the character is a special character")

#question 9

alphabet= str(input('enter the alphabet: ')) 
if alphabet in ('a','e','i','o','u','A','E','I','O','U'):
    print("the alphabet is vowel")
else: 
    print("the alphabet is not vowel" )
    
#question 10

character=input('enter the character:')
if character.isalpha() and character==character.lower():
    print("the character is in lowercase")
elif character.isalpha() and character==character.upper():
    print("the character is in uppercase")

#question 11

day_no=int(input("enter the no. of day:"))
if day_no==1:
    print("Monday")
elif day_no==2:
    print("Tuesday")
elif day_no==3:
    print("Wednesday")
elif day_no==4:
    print("Thursday")
elif day_no==5:
    print("Friday")
elif day_no==6:
    print("Saturday")
elif day_no==7:
    print("Sunday")

#question 12

month_no=int(input("enter the month no.: "))
if month_no in (1,3,5,7,8,10,12):
    print("the month has 31 days")
elif month_no==2:
    print("the month has 28(common year) or 29(leap year) days")
elif month_no in (4,6,9,11): 
    print("the month has 30 days")

#question 13

amt=int(input("enter the amount of money: "))
if amt>=500:
    print("500note:",(amt//500))
    amt//500
    amt%=500
    print("200note:",(amt//200))
    amt//200
    amt%=200
    print("100note:",(amt//100))
    amt//100
    amt%=100
    print("50note:",(amt//50))
    amt//50
    amt%=50
    print("20note:",(amt//20))
    amt//20
    amt%=20
    print("10note:",(amt//10))
    amt//10
    amt%=10
    print("5coin:",(amt//5))
    amt//5
    amt%=5
    print("2coin:",(amt//2))
    amt//2  
    amt%=2
    print("1coin:",(amt//1))
    amt//1
    amt%=1
    print("balance is: ",amt)
    
#question 14

angle_1=int(input("enter the value of angle 1: "))
angle_2=int(input("enter the value of angle 2: "))
angle_3=int(input("enter the value of angle 3: "))
triangle=(angle_1 + angle_2 + angle_3)
if triangle== 180:
   print("the traingle is valid with these values of angles") 
else:
    print("the triangle is not valid with these values of angles")
    
#question 15

length_1=int(input("enter length of side 1: "))
length_2=int(input("enter length of side 2: "))
length_3=int(input("enter length of side 3: "))
if length_1<(length_2+length_3) and length_2<(length_1+length_3) and length_3<(length_1+length_2):
    print("the traingle is valid with these lengths of sides")
else:
    print("the triangle is not valid with these lengths of sides")

#question 16

length_1=int(input("enter length of side 1: "))
length_2=int(input("enter length of side 2: "))
length_3=int(input("enter length of side 3: "))
if length_1==length_2==length_3:
    print("it is an equilateral triangle" )
elif length_1==length_2!=length_3 or length_2==length_3!=length_1 or length_1==length_3!=length_2:
    print("it is an isoceles triangle")
elif length_1!=length_2!=length_3 and length_1<(length_2+length_3) and length_2<(length_1+length_3) and length_3<(length_1+length_2):
    print("it is a scalane triangle")
    
#question 17

a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
d= ((b*b)-(4*(a*c)))
if d>0: 
    root1=(((-b)+d**0.5)/(2*a))
    root2=(((-b)-d**0.5)/(2*a))
    print("two distinct real roots exist","root 1 is:", root1,"root 2 is:", root2)
elif d==0:
    root1=root2= (-b/(2*a))
    print("two equal real roots exist","root 1 is:", root1,"root 2 is:", root2)
elif d<0:
    root1=root2= (-b/(2*a))
    imaginary= ((-d**0.5)/(2*a))
    print("two distinct complex roots exist", "root 1 is:", root1,imaginary, "root 2 is:", root2,imaginary )

#question 18

buying_price=int(input("enter the buying price: "))
selling_price=int(input("enter the selling price: "))
if selling_price>buying_price:
    print("hence the deal was profitable")
elif selling_price<buying_price:
    print("hence the deal resulted in loss")
elif selling_price==buying_price:
    print("the deal was neither profit nor loss" )
    
#question 19

physics=int(input("enter physics marks: "))
chemistry=int(input("enter chemistry marks: "))
maths=int(input("enter maths marks: "))
biology=int(input("enter biology marks: "))
computer=int(input("enter computer marks: "))
percentage=(((physics+chemistry+maths+biology+computer)/500)*100)
if percentage>=90:
    print("GRADE A")
elif percentage>=80:
    print("GRADE B")
elif percentage>=70:
    print("GRADE C")
elif percentage>=60:
    print("GRADE D")
elif percentage>=40:
    print("GRADE E")
elif percentage<40:
    print("GRADE F")
    
#question 20

basic_salary=int(input("enter the amount of salary: "))
if basic_salary<=10000:
    HRA=(0.2*(basic_salary))
    DA=(0.8*(basic_salary))
    print("gross salary is : ", (basic_salary+HRA+DA))
elif basic_salary<=20000:
    HRA=(0.25*(basic_salary))
    DA=(0.9*(basic_salary))
    print("gross salary is : ", (basic_salary+HRA+DA))
elif basic_salary>20000:
    HRA=(0.3*(basic_salary))
    DA=(0.95*(basic_salary))
    print("gross salary is : ", (basic_salary+HRA+DA))

#question 21

units=int(input("enter the total units of electricity: "))
if units<=50:
    electercity_charge=((units)*(0.5))
    print("the electricity bill for the month is: ",(electercity_charge+((0.2)*(electercity_charge))))

elif units>50 and units<=150:
         electercity_charge=(((50)*(0.5))+(units-50)*(0.75))
         print("the electricity bill for the month is: ",electercity_charge+((0.2)*(electercity_charge)))
          
elif units>150 and units<=250:
         electercity_charge=(((50)*(0.5))+(100)*(0.75)+(units-150)*(1.25))
         print("the electricity bill for the month is: ",electercity_charge+((0.2)*(electercity_charge)))
          
elif units>250:
         electercity_charge=((((50)*(0.5))+(100)*(0.75)+(100)*(1.25)+((units-250*(1.50)))))
         print("the electricity bill for the month is: ",electercity_charge+((0.2)*(electercity_charge)))   
     
#Loop queestions

#Question 1 (#10 to 1)

x=10
while x>=1:
    print(x)
    x-=1

#question 2 (#1 to 10 [Even])

x=2
while x<=10:
    print(x)
    x+=2

#question 3 (#1 to 10 [ODD])

x=1
while x<=10:
    print(x)
    x+=2
