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







open_file = open('thedata.csv')
open_file.readlines()

the_dates = []
the_rates = []

def allfiles(filename):
    open_file = open(filename)
    open_file.readlines()
    the_dates = []
    the_rates = []
for lines in open_file:
    the_data = lines.strip()
    the_data = the_data.split(',')
    the_dates.append(the_data[0])
    the_rates.append(the_data[1])
    the_difference = (the_rates[-1] - the_rates[0])
filename.close()
return the_difference
    
    
    

