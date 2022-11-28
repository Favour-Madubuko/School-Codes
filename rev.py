#1
#a = [1,2,3] = a[:]
#b = a = [1,2,3]
#b[0] = 1 = 5
#print(b) yeilds [5,2,3]

#2
my_list = list()
my_list.append(76) 
my_list.append(92.3)
my_list.append("hello")
my_list = my_list+[True, 4, 76]
print(my_list)

#3
my_list.append("apple")
my_list.append(76)
my_list.insert(3, "cat")
my_list[0] = 99
my_list.index("hello")
my_list.count(76)
my_list.pop(my_list.index(76))
my_list.pop(my_list.index(True))
print(my_list)

#4
def sum_of_squares(xs):
    new = list()
    for i in xs:
        i = i**2
        new.append(i)
    print(sum(new))
    
sum_of_squares([2,3,4])
