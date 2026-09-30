#homework 1

question 1

a=int(input("enter integer:"))
b=float(input("enter float:")) 
c=str(input("enter string"))
d=bool(input("enter bool"))
e=complex(input("enter complex"))

print(a)
print(b)
print(c)
print(d)
print(e)

question 2

x= int(input("1st no.: "))
y= int(input("2nd no.: "))

print(x+y)

question 3

a=int(input("1st no.: "))
b= int(input("2nd no.:"))

print(a+b)
print(a-b)
print(a*b)
print(a/b)


question 4 and 5

x=int(input("length:"))
y=int(input("breadth:"))

perimeter= 2*(x+y)
area= (x*y)

print(perimeter)
print(area)

question 6

r= int(input("radius of circle:"))

diameter= (2*r)
circumference=(2*3.14*r)
area=(3.14*r*r)

print(diameter)
print(circumference)
print(area)

question 7

x= int(input("length in centimeter:"))

meter_length= (x/100)
kilometer_length= (x/100000)

print(meter_length)
print(kilometer_length)

question 8 and 9

c= int(input("temperature in celsius:"))

temp_farenheit= ((c*9/5)+32)

print(temp_farenheit)

f= int(input("temperature in farenheit:"))

temp_celsius= ((f-32)*5/9)

print(temp_celsius)

question 10

d=int(input("no. of days:"))

years= (d/365)
weeks= (d/7)
months= (d/30)

print(years)
print(weeks)
print(months)

question 11

x=int(input("base:"))
y=int(input("exponent:"))

print(x**y)

question 12

r=int(input("no. whose square root you want:"))

square_root=(r**0.5)

print(square_root)

question 13

a=int(input("first angle:"))
b=int(input("second angle:"))

third_angle= (180-(a+b))

print(third_angle)

question 14

h=int(input("height of triangle:"))
b=int(input("base of triangle:"))

area_triangle=(h*b*0.5)

print(area_triangle)

question 15

a= int(input("side of traingle:"))

triangle_area= (((3**0.5)/4)*(a**2))

print(triangle_area)

question 16

a=int(input("marks in maths:"))
b=int(input("marks in physics:"))
c=int(input("marks in chemistry:"))
d=int(input("marks in biology:"))
e=int(input("marks in english:"))

average=((a+b+c+d+e)/5)
percentage=(((a+b+c+d+e)/500)*100)

print(average)
print(percentage)

question 17 and 18

p=int(input("principal:"))
r=int(input("rate of interest:"))
t=int(input("time:"))
n=int(input("no. of times interest applied:"))

simple_interest= ((p*r*t)/100)

print(simple_interest)

compound_interest= p*(1+(r/n))**(n*t)

print(compound_interest)