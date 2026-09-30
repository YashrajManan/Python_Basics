#Print Variables and Messages
# print("Hello world")

# a= 10
# b= 5

#Value of a= ?? and b= ??
# print("Value of a= "+ str(a) +" and b= "+str(b))

# print(f"Value of a= {a} and b= {b} and sum= {a+b}")
# print("Value of a=",a," and b=",b)


#Escape Characters
#\n - Enter
#\t - Tab
#\b - Backspace
#\" - "
#\' - '
#\\ - \

# print("Hello\nworld")
# print("Hello\t\t\nworld")
# print("Hello\bworld")


#We can use "" or '' inside "" or ''

# print("Hello\\world")

# print(" 'Hello' world ")
# print(' "Hello" world ')
# print(" \"Hello\" world ")

#Print always prints string in new line
#Hello*world\n
# print("Hello",end= "*")
# print("World")


#Strings
#Anything written within "" or '' or {'''''' or """""" -> Multiline Strings}

# You can use quotes inside a string, as long as
# they don't match the quotes surrounding the string

# a= "Hello
# World"

# a= """
# Hello
# world
# """

# a= "Hello"
#H   e   l   l   o 
#0   1   2   3   4
#-5 -4  -3  -2  -1

#Slicing
#variable_name[ start:end+1 ]
#start: first character
#end  : last character


# print(a[2:2])

# print(a[4:-3])
# print(a[-4:4])
# print(a[-3:-1])

# print(a[:3])
# print(a[1:])
# print(a[1:4])


#variable_name[start:end : steps]
#steps: +1
#a= "Hello"

# print(a[-4:4:2])

# print(a[::2])
# print(a[::-2])

#Indexing [-ve or +ve]
#Extract one character
#variable_name[ index ]

# print( a[0] )
# print( a[1] )
# print( a[2] )
# print( a[3] )
# print( a[4] )


#How to get length of string??
#len(string)
# a= "Hello"

# print( len(a) )
# print( len("Hello") )

#How to check characters or word ??
a= "Hello world"

# print( "llo" not in a)

# print( "llo" in a)
# print( "Hd" in a)
# print( "w" in a)
