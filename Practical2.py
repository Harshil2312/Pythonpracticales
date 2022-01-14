# Name : Harshil Padasala
# Id : 20CE064

# ********************************************** Dictionary Practicals **********************************************

print("********************************************** Dictionary **********************************************")
# --> a. Write a Python script to check whether a given key already exists in a dictionary.
my_dict1 = {'firstName': 'Harshil',
            'id': '20ce064',
            'lastName': 'Padasala'}

print(f"my_dict1: {my_dict1}")
print(f"\n'firstName' in my_dict1: {'firstName' in my_dict1}")
# --> or print(f"\n 'firstName' in my_dict1: {'firstName' in my_dict1.keys()}")
print(f"'middleName' in my_dict1: {'middleName' in my_dict1}")

# --> b. Write a Python script to merge two Python dictionaries.

my_dict2 = {'FirstName': 'Krishna',
            'LastName': 'Padasala'}

# --> update() function update the my_dict1 dictionary
my_dict1.update(my_dict2)
print(f'\n\nmerge dictionary: {my_dict1}')

# --> c. Write a Python program to sum all the items in a dictionary.

my_dict = {1: 10,
           2: 20,
           3: 30,
           4: 40}

print(f"\n\nSum of values is {sum(my_dict.values())}")  # --> print the sum of values
print(f"Sum of keys is {sum(my_dict)}")  # --> print the sum of keys

# --> d. Write a Python script to add a key to a dictionary. Sample Dictionary : {0: 10, 1: 20}
#       Expected Result : {0: 10, 1: 20, 2: 30}


sample = {0: 10, 1: 20}
print(f"\nsample = {sample}")
sample.update({2: 30})
print(f"after adding sample = {sample}")

# --> e. Write a Python script to concatenate following dictionaries to create a new one.
#       Sample Dictionary :   dic1={1:10, 2:20}   dic2={3:30, 4:40}
#                               dic3={5:50,6:60}
#       Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

extended = {}
print(f"\nextended = {extended}")
extended.update(dic1)  # --> update dictionary extended after adding dic1
extended.update(dic2)
extended.update(dic3)
print(f"After adding other dictionaries extended = {extended}")

# ********************************************** Tuple Practicals **********************************************

print("\n\n\n********************************************** Tuple **********************************************")
# --> a. Write a Python program to create a tuple with different data types.

tup = ('Harshil', 64, ['list', 'krishna'], {1: 'dictionary'}, {'Set', '20CE064'})
print(f"\n\nTuple with different datatype\n\ttup = {tup}")

# --> b. Write a Python program to create a tuple with numbers and print one item.

numbers = tuple(range(1, 50))  # --> create tuple in range 1 to 50
print(f"\nnumbers[2] = {numbers[2]}")

# --> c. Write a Python program to add an item in a tuple.

tup = ('Harshil', '20CE064')
print("\n", tup)
tup += (1, 2, 3)  # --> add list in tuple
print(f"After adding list in tuple tup = {tup}")

# --> d. Write a Python program to convert a tuple to a string.

tup = ('H', 'a', 'r', 's', 'h', 'i', 'l')
string = "".join(tup)
print(f"\nTuple tup = {tup}\n string = {string}")

# --> e. Write a Python program to find the length of a tuple.

tup = ('Harshil', 64, ['list', 'krishna'], {1: 'dictionary'}, {'Set', '20CE064'})
print(f"tup = {tup}\nLength of tup = {len(tup)}")

# ********************************************** Set **********************************************

print("\n\n\n********************************************** Set **********************************************")
# --> a. Write a Python program to add member(s) in a set and clear a set.
set1 = {'Harshil', (12, 4)}
print(f"\n\nset1 = {set1}")
set1.add('harshil')
print(f"After adding set1 = {set1}")
set1.clear()
print(f"Clear the set\nset1 = {set1}")

# --> b. Write a Python program to remove an item from a set if it is present in the set.
set1 = {'Harshil'}
print(f"\n'Harshil' in set1 = {'Harshil' in set1}")
if 'Harshil' in set1:
    set1.remove('Harshil')
print(set1)

# --> c. Write a Python program to create an intersection, Union, difference of sets.
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {5, 6, 7, 8, 9, 10}

intersection_ = set1.intersection(set2)
union_ = set1.union(set2)
difference_ = set1.difference(set2)

print(f"\nset1 = {set1}\nset2 = {set2}\nintersection = {intersection_}\nunion = {union_}\ndifference = {difference_}")

# --> d. Write a Python program to find maximum and the minimum value in a set.
set1 = {4, 9, 8, 12}
temp_list = list(set1)
temp_list.sort()
max_number = temp_list[-1]
min_number = temp_list[0]
print(f"max number = {max_number} \t\t\t min number = {min_number}")

# --> e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
list1 = [1, 2, 3, 4, 1, 2, 3, 6, 8, 9, 1, 2, 7, 9, 9, 92, 1, 2, ]
set1 = set(list1)
for number in set1:
    print(f"number = {number}, \tcount in list = {list1.count(number)}")
