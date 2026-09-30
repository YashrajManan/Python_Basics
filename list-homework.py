
#question 1
x=[10,20,30,40,50] 
print(x[2])

print(len(x))

list_length=len(x)
if list_length==0:
    print("the list is empty")
else:
    print("the list is not empty")
    
#question 2 
x=[10,20,30,40,50]
x[1]=200
print(x)
x.append(600)
print(x)
x.insert(2, 300)
print(x)
x.remove(600)
print(x)
del x[0]
print(x)

#question 3
x=[10,20,30,40,50]
total_sum= sum(x)
average= total_sum/len(x)
print(total_sum)
print(average)

#question 4
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#question 5
numbers = [1, 2, 3, 4, 5, 6, 7]
i=0
while i<len(numbers):
    numbers[i]=numbers[i]*numbers[i]
    i+=1
print(numbers)
 
 #or  
 
numbers = [1, 2, 3, 4, 5, 6, 7]
i=0
while i<len(numbers):
    numbers[i]=numbers[i]**2
    i+=1
print(numbers)

#question 6 
data = [8, 2, 15, 1, 9]
print(min(data))
print(max(data))  

#question 7
sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
print(sports.count('Football'))

#question 8 
numbers = [5, 2, 8, 1, 9] 
numbers.sort()
print(numbers)

#question 9
list1= [10, 20, 30]
list2 = list1.copy()
print(list2)

#question 10 
list_a = [1, 2]
list_b = [3, 4]
list_c=(list_a+list_b)
print(list_c)

#question 11
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = []
i=0 
while i<len(list1):
    if list1[i]!="":
       list2.append(list1[i])
    i+=1
print(list2)

#question 12
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
i=0 
new_list=[]
while i<len(list_with_duplicates):
    if list_with_duplicates[i] not in new_list:
        new_list.append(list_with_duplicates[i])
    i+=1 
print(new_list)

#question 13
list1 = [5, 20, 15, 20, 25, 50, 20]
new_list= []
i=0  
while i<len(list1):
    if list1[i] != 20:
        new_list.append(list1[i])
    i+=1
print(new_list)

#question 14 
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
new_list = []
i=0 
while i<len(my_list):
    if isinstance(my_list[i], int):
       new_list.append(my_list[i])
    i+=1 
print(new_list)
    
#question 15 
nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print(nested_list[1][1])

#question 16
list1 = [[1, 2], [3, 4], [5, 6, 7]]
new_list=[]
i=0 
while i<len(list1):
    j=0 
    while j<len(list1[i]):
        new_list.append(list1[i][j])
        j+=1
    i+=1 
print(new_list)

#question 17
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
final_list=[]
i=0 
while i< len(list1) and len(list2):
    final_sum= list1[i]+list2[i]
    final_list.append(final_sum)
    i+=1 
print(final_list)

#question 18 
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
i=0 
new_list= []
while i< len(list1):
    j=0 
    while j<len(list2):
        new_list.append(list1[i]+list2[j])
        j+=1
    i+=1
print(new_list)

#question 19 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
i=0 
while i<len(list1) and len(list2):
    print(list1[i],list2[-(i+1)])
    i+=1
#question 21
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#question 22
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

#question 23 
list1 = [5, 10, 15, 20, 25, 50, 20]
i=0 
while i< list1.count(20):
    index = list1.index(20)
    list1[index] = 200
i+=1
print(list1)

#question: Access the second element of the second list
lst = [[1, 2], [3, 4], [5, 6]]
print(lst[1][1]) 

#question: Replace the third element of the first list with 10
lst = [[1, 2, 3], [4, 5, 6]] 
lst[0][2]=10
print(lst)

#question: Append [7, 8] to the nested list
lst = [[1, 2], [3, 4]] 
lst.extend([[7,8]])
print(lst)

#question: Count the total number of sublists
lst = [[1], [2, 3], [], [4, 5]] 
print(len(lst))

#question: Count total number of elements in all sublists
lst = [[1], [2, 3], [], [4,5]] 
i=0 
newlist=[]
while i<len(lst):
    j=0 
    while j<len(lst[i]):
       newlist.append(lst[i][j])
       j+=1 
    i+=1 
print(len(newlist)) 

#question: Find if value 5 exists in any sublist
Input= [[1, 2], [5, 6]] 
i=0 
newlist=[]
while i<len(Input):
    j=0 
    while j<len(Input[i]):
       newlist.append(Input[i][j])
       j+=1 
    i+=1 
if newlist.index(5):
    print("True")
else:
    print("False") 
    
#question: Get all sublists that contain value 3
Input= [[3], [4, 5], [3, 6]] 
i=0 
while i<len(Input):
    j=0 
    while j<len(Input[i]):
        if Input[i][j]==3:
           print(Input[i], end="")
        j+=1 
    i+=1
    
print(" ", end="\n")

#question: Return the index of sublist that contains 4
Input_1 = [[1, 2], [3, 4], [5, 6]] 
j=0 
while j<len(Input):
    i=0 
    while i<len(Input_1[j]):
        if Input_1[j][i]==4:
            print(Input_1[j])
        i+=1 
    j+=1

#question: Find the max element from all sublists
Input= [[1, 8], [3], [7, 4]] 
newlist=[]
i=0 
while i<len(Input):
    j=0 
    while j<len(Input[i]):
        newlist.append(Input[i][j])
        j+=1 
    i+=1 
print(max(newlist))


#question: Return sublists where the sum is > 5
Input= [[1, 2], [3, 4], [2]] 
list_new=[]
i=0 
while i<len(Input):
    j=0
    while j<len(Input[i]):
        if sum(Input[i])>5:
            list_new.append(Input[i][j])
        j+=1 
    i+=1 
print(list_new)
            
#question: Reverse each sublist
Input= [[1, 2], [3, 4]] 
i=0 
while i<len(Input):
    Input[I].reverse()
    i+=1 
print(Input)

#question: Transpose a 2x3 matrix (nested list)
Input= [[1, 2, 3], [4, 5, 6]] 
list_new=[]
rows=len(Input)
cols=len(Input[0])
i=0
while i<cols:
    row=[]
    j=0
    while j<rows:
        row.append(Input[j][i])
        j+=1 
    list_new.append(row)
    i+=1 
print(list_new)

#question: Multiply each number in sublists by 2
Input= [[1, 2], [3, 4]] 
i=0 
while i<len(Input):
    j=0
    while j<len(Input[i]):
        Input[i][j]=Input[i][j]*2
        j+=1 
    i+=1 
print(Input)

#question: Filter out all odd numbers from sublists
Input= [[1, 2], [3, 4]]
newlist=[]
i=0 
while i<len(Input):
    j=0
    while j<len(Input[i]):
        if Input[i][j]%2==0:
            newlist.append([Input[i][j]])
        j+=1 
    i+=1 
print(newlist)
        
#Remove empty sublists
Input = [[1, 2], [], [3], []] 
i=0 
while i<len(Input):
    Input.remove([])
    i+=1 
print(Input)











