# question 1 
my_tuple=tuple((1,2,3,4,5))
print(my_tuple[2])
print(len(my_tuple))

# question 2 
original_tuple=('a','b')
print(3*original_tuple)

# question 3 
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[3:7])

# question 4 
tuple1 = (10, 20, 30, 40, 50) 
print(tuple1[::-1])

# question 5 
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

# question 6 
my_tuple = (50,)
print(my_tuple)

# question 7
tuple1 = (10, 20, 30, 40)
a,b,c,d = tuple1
print(a,b,c,d)
a= tuple1[0]
b= tuple1[1]
c= tuple1[2]
d= tuple1[3]
print(a,b,c,d)

# question 8
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1 
print(tuple1)
print(tuple2)

# question 9
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
print(tuple2)

# question 10 
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)

# question 11


# question 12
t1 = (1, 2, 3)
t2 = (1, 2, 4)
sum(t1)
sum(t2)
if sum(t1)>sum(t2):
    print("t1 is greater than t2")
elif sum(t2)>sum(t1):
    print("t2 is greater than t1")
else:
    print("both are equal")
    
# question 13
my_tuple = (1, 2, 2, 3, 4, 4, 5)
my_list = list(my_tuple)
newlist=[]
i=0 
while i<len(my_list):
    if my_list[i] not in newlist:
        newlist.append(my_list[i])
    i+=1
newtuple=tuple(newlist)
print(newtuple)

# question 14
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# question 15
t = (1, 2, 3, 4)
l = list(t)
nl=[]
i=0  
while i<len(l):
    nl.append(l[i]**2)
    i+=1 
nt=tuple(nl)
print(nt)

# question 16 
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)

# question 17
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

# question 18
tuple1 = (50, 10, 60, 70, 50)
list1 = list(tuple1)
print(list1.count(50))

# question 19
tuple1 = (45, 45, 45, 45)
i=0 
while i<len(tuple1):
    if tuple1[i]== tuple1[-i+1]:
        print("all items in tuple are same")
    i+=1 




