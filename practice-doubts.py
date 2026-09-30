

  
  
num=int(input("enter the number: "))
num_1=num
last=num%10
count=1
while num>9:
    num=num//10
    count*=10
first=num 

num_1=num_1-first*count
num_1=num_1//10
num_1=num_1*10+first
num_1=num_1+last*count

print(num_1) 



