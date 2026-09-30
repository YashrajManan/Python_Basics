#question 1
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict['profession']='Doctor'
print(my_dict)
my_dict['age']=40
print(my_dict)
print(my_dict['city'])

#question 2
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'} 
del my_dict['profession']
print(my_dict) 

for x in my_dict.items():
    print((x))

print('age' in my_dict)

#question 3
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict= dict()

for i in range(len(keys)):
    my_dict.update({keys[i]:values[i]})
print(my_dict)

#question 4
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict.clear()
print(my_dict)

#question 5
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

#question 6
string1 = 'Jessa'
freq_dict= {}
for char in string1:
    if char in freq_dict: 
        freq_dict[char]+=1 
    else:
        freq_dict[char]=1
print("Frequencies for 'Jessa':", freq_dict)

#question 7
data = {'person': {'name': 'Alice', 'age': 30}}
print(data['person']['age'])

#question 8
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

#question 9
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
nested_student_dict['class']['student']['name']="Jessa"
print(nested_student_dict)

#question 10
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
new_dict = {}
for i in range(len(employees)):
    new_dict.update({employees[i]: defaults})
print(new_dict)

#question 11
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york" 
}
    
keys = ["name", "salary"]
new_dict= {i: sample_dict[i] for i in keys}
print(new_dict)

#question 12
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]
for i in keys: 
    sample_dict.pop(i)
print(sample_dict)

#question 13
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 is present in the dictionary")
else:
    print("200 is not present in the dictionary")
    
#question 14
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

del sample_dict["city"]
sample_dict["location"]="New York"
print(sample_dict)

#question 15
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict))
        
#question 16
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
} 

sample_dict['emp3']['salary']=8500 
print(sample_dict)

#question 17
original_dict = {'a': 1, 'b': 2, 'c': 3} 
inverted_dict = {} 
for key in original_dict:
    value = original_dict[key]
    inverted_dict[value] = key 
print("Original dictionary :", original_dict)
print("Inverted dictionary :", inverted_dict)
    
#question 18
my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

keys = []
for key in my_dict:
    keys.append(key)

n = len(keys)
for i in range(n):
    for j in range(0, n - i - 1):
        if keys[j] > keys[j + 1]:
            keys[j], keys[j + 1] = keys[j + 1], keys[j]

sorted_dict = {}
for key in keys:
    sorted_dict[key] = my_dict[key]

print("Original dictionary:", my_dict)
print("Sorted dictionary by keys:", sorted_dict)

#question 19
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
items = list(my_dict.items())

n = len(items)
for i in range(n):
    for j in range(0, n-i-1):
        if items[j][1] > items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]

sorted_dict = {}
for key, value in items:
    sorted_dict[key] = value

print("Original dictionary:", my_dict)
print("Sorted dictionary by values:", sorted_dict)

#question 20


