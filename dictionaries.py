'''
Some things are identified by some token/name
- Index number of a student
- bank account number
- url of a website
- telephone number

A dictionary is a mapping from keys to their corresponding values

A mapping is a relationship in which each element of one set corresponds to an element of another set

A dictionary key must be of a type that is immutable e.g
a. List and dictionaries cannot be used as keys
b. Integer, float, string, boolean

RULES FOR KEYS IN DICTIONARIES:
i. A dcitionary key is unique (No duplicates)
ii. We can have mixed keys
iii. Keys are case sensitive

RULES FOR VALUES IN DICTIONARIES
i. They can be of any data type
'''


my_dict1 = {
    "John": 3.35,
    "Dorcas": 2.98,
    "Doe": 3.47
    }

my_dict2 = {
    3.35:"John",
    2.98:"Dorcas",
    3.47:"Doe"
    }

#This creates a dictionary from keyword arguments with dict function
my_dict_2 = dict(
    firstname = "Kwabena",
    lastname = "Bamfo",
    age = 33
    )
'''Dictionary LookUP'''

#Given a dictionary and a key, we can eaily find the corresponding value
print(my_dict_2["age"])
print(my_dict_2["firstname"])

'''Adding/Updating Items'''
#We use the square bracket operator to add an itme to a dictionary
my_dict = {
    "firstname":"kwabena",
    "lastname":"Bamfo"
    }
my_dict["age"] = 33
my_dict["nationality"] = "Ghana"

print(my_dict)

'''Dictionaries: Iteration'''



'''Reverse Lookup'''
#When we have a value and we want to find the corresponding key?
# There is no simple syntax for this in Python. We need to search through our dictionary
myDict = {
    "firstname":"kwabena",
    "lastname":"Bamfo"
    }
for key,value in myDict.items():
    if value == "kwabena":
        print(key)


'''raise statement'''
# raise LookUpError()
# raise IndexError()
# raise ValueError()

my_dict = {0:"kwame",1:"Kwasi"}

def reverse_lookup():

"""HASHTABLE. The underlying data structure for dictionaries is hashtable"""












#1
enter_name = input("Enter your string: ")
#An empty list is initialized
list_name = []
#The for loop loops through the given string
for letter in enter_name:
    if letter not in list_name:
        list_name.append(letter)
list_name = sorted(list_name)
#The for loop loops through the list
for letter in list_name:
    #The count method counts the number of times a letter occurs in the string
    print(letter, enter_name.count(letter)) 
    
#2.
enter_name = input("Enter your string: ")
def lower_upper_count():
    lowercase_count = 0
    uppercase_count = 0
    for letter in enter_name:
        if letter.islower():
            lowercase_count += 1
        elif letter.isupper():
            uppercase_count += 1
    final = {'lower': lowercase_count, 'upper': uppercase_count}
    return final
print(lower_upper_count())

#3.
def OddEvenCount(integers):
   list_name = integers
   even_element = 0
   odd_element = 0
   for each_element in list_name:
       if each_element % 2 == 0:
           even_element += 1
       elif each_element % 2 != 0:
           odd_element += 1
       elif list_name == []:
           even_element == 0
           odd_element == 0
   the_dict = {'odd': odd_element, 'even': even_element}
   return the_dict
print(OddEvenCount([1,2,3,4,5,6,8,66,55,34,12]))
print(OddEvenCount([]))

#4.
pi = "3.1415926535897932384626433832795028841971693993751"
the_list = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for value in pi:
    if value == '.':
        continue
    else:
        the_list[int(value)] += 1
print(the_list)

#print(f"The digit {letter} has count {enter_name.count(letter)})
#5. 
def digit_count(float_number):
    the_list = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for number in float_number:
        if number == '.':
            continue
        else:
            the_list[int(number)] += 1
    return the_list
print(digit_count("1.332"))








    
    
    

