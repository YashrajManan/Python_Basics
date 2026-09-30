#Python List
#Collection of Data
# x= 10
# y= 20
# z= 30

# y= 5

# l= [10,20,30,40,50,60]

#Ordered
#Changable
#Allow Duplicates
#Different Type of Data


#List Methods
# x= [1,2,3,4,2,2,2]

# x.reverse()
# x.sort()
# print( x )

# print(x.count(2))
# print( x.index(2) )

# y= x.copy()
# x[0]= 100

# print(x)
# print(y)


#Insert
# x.append(5)
# x.extend( [5,6,7,8] )
# x.insert( -3, 100 )

#Delete
# x.pop()
# x.pop( 2 )

#x.remove( 12 )
#x.clear()

# del x[1:3]
# del x[3]
# del x

# print(x)


#Print all items of list??
# i= 0
# while i<len(l):
#   print(l[i])
#   i+= 1

# i= len(l)-1
# while i>=0:
#   print(l[i])
#   i-=1

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon","guava"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


#How to update list values??
# l[1]= 5
# print(l)

#Total items
# print( len(l)  )

#Indexing [+ve or -ve]
# print(l[0], l[-3])
# print(l[1], l[-2])
# print(l[2], l[-1])


# print(l)
# print( type(l) )


day = 3
num= 2
match day*2:
  case 1 | 2 | 3 if num==1:
    print("Monday")
 
  case 4 if num==2:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
      print("Invalid")
