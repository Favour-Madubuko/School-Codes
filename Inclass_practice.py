'''1.  
enter_name = input("Enter your string: ").lower()
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
    print(letter, list_name.count(letter))
'''

'''2.

#enter_name = input("Enter your string: ")
def lower_upper_count(enter_name):
    lowercase_count = 0
    uppercase_count = 0
    for letter in enter_name:
        if letter.islower():
            lowercase_count += 1
        elif letter.isupper():
            uppercase_count += 1
    final = {'lower': lowercase_count, 'upper': uppercase_count}
    return final
print(lower_upper_count("Kwabena Bamfo"))
'''

'''3.
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
'''

'''4
'''



