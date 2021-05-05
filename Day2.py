'''Accept a list of numbers from user and

print a sum of those values

print minimum value

print only unique values from those

print the list of numbers in ascending order

print the list of numbers in descending order'''

 

num_list = input("Enter the number list: ") # Getting input from user e.g: 12 13 14 15 16

new_list = [int(num) for num in num_list.split(" ")] # Actually we are getting the input as string. Using split method and int to standardize it

 

#Minimum value

print(f'Minimum number in a list: {min(new_list)}')

 

#Unique values in list

print(f'Unique value of list : {list(set(new_list))}')

 

#ascending order

new_list.sort()

print(f'Ascending order: {new_list}')

#descending order

new_list.sort(reverse = True)

print(f'Descending order: {new_list}')

 

 

 

'''

Write a name creator app

Ask user's first name

Ask user's last name

Print like Firstname Lastname (capialized first and last names)

'''

 

first_name = input("Enter your first name : ")

last_name = input("Enter your last name : ")

 

print(f'{first_name.capitalize()} {last_name.capitalize()}')

 

 

'''

Accept 2 lists of numbers from user and

print numbers present in both the lists

print numbers in one list and not another and vice versa

'''

 

list_1 = input("Enter the first list: ") # Getting input from user e.g: 12 13 14 15 16

list_2 = input("Enter the second list: ")

new_list1 = set([int(num) for num in list_1.split(" ")])

new_list2 = set([int(num) for num in list_2.split(" ")])

 

print(f'Intersection of List: {new_list1 & new_list2}')

 

print(f"Differ from List2: {new_list1 - new_list2}")

print(f"Differ from List 1: {new_list2 - new_list1}")

 

 

 

'''

Try reversing the name above

Accept a name from a user

Print First and Last name separately

'''

 

name = input("Enter your full name: ")

first_name,last_name  = name.split(" ")



print(f'First name: {first_name.upper()} Last name: {last_name.upper()}')

 
