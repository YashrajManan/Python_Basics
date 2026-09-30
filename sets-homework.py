#question 1
fruits= set(("apple","banana","mango","orange"))
print(fruits)
fruits.add("grapes")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("mango")
print(fruits)

#question 2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2)
print(set3)

#question 3
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)

#question 4
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.difference(set2)
print(set3)

#question 5
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.symmetric_difference(set2)
print(set3)

#question 6
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)

#question 7
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

#question 8
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10,20,30})
print(set1)

#question 9
subset_set = {10, 20}
main_set = {10, 20, 30, 40}
print(subset_set.issubset(main_set))

#question 10
set1 = {10, 20}
set2 = {10, 20, 30, 40}
print(set2.issuperset(set1))

#question 11
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print("set1 and set2 dont have any common element")
else: 
    print("set1 and set2 have common elements", set1.intersection(set2))

#question 12
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)

#question 13
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)

#question 14
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
set1 = set(list1)
set2 = set(list2)
set1.intersection_update(set2)
print(set1)

#question 15
my_list = [10, 20, 30]
frozen_set = frozenset(my_list)
print(frozen_set) 

#question 16
sentence = "dog is a simple animal dogs is selfless animal"
words = sentence.lower().split()
my_set = set(words)
print(len(my_set))


