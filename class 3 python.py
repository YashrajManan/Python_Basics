#String Methods
#variable_name.method_name()
#string.method_name()
text= "Hello world"

#upper 
#new= text.upper()

#lower
# new= text.lower()

#capitalize
# new= text.capitalize()

# new= text.casefold()

new= text.center(10,"-")
new= text.count("ll")
new= text.encode('utf-8')
new= text.endswith("")
new= text.expandtabs(24)
new= text.find("H",2)
new= text.format(10,"**")
new= text.index("l")
new= text[0].islower()
new= "->".join(['Aman',"Raju","Pankaj"])
new= text.ljust(10,"=")
new= text.rjust(10,"-")

new= text.lstrip()
new= text.rstrip()
new= text.strip()

new = text.partition(" ")
new = text.split(" ")

new = text.replace("l","*")

new= text.find("l")
new= text.rfind("l")
new= text.swapcase()

print(new)

# x= str.maketrans({"l":"*","H":"^"})
# print(text.translate(x))


#String is immutables
#Cannot be changed once created

# a= "Hello"
# a[1]= '3'
