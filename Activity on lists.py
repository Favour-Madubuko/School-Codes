'''PART 1'''
a = [1,2,3]
b = a[:]

#BEFORE
# a -----> [1,2,3]
# b -----> [1,2,3]
b[0]=5

#AFTER
# a -----> [1,2,3]
# b ---->  [5,2,3]


'''PART 2'''
my_list = []
my_list.append(76)
my_list.append(92.3)
my_list.append("hello")

my_list = my_list + [True]
my_list = my_list + [4]
my_list = my_list + [76]



'''PART 3'''
#Appending apple and 76
my_list.append("apple")
my_list.append(76)

#Inserting the value cat at position 3 but the position on the list is 2
my_list.insert(2,"cat")
#Inserting 99 at the start of the list
my_list.insert(0,99)

#Finding the index of hello
hello_index = my_list.index("hello")

#Counting the number of 76
count_of_76 = my_list.count(76)

#Removing the first occurence of 76
my_list.remove(76)

#Removing True using pop and index
my_list.pop(my_list.index(True))


'''PART 4'''
def sum_of_squares(xs):
    the_sum = 0
    for numbers in xs:
        the_square = i**2
        the_sum += the_square
    return the_sum


