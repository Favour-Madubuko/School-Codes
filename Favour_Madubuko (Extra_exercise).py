'''Problem 5'''
'''def greatest_common_divisor(a,b):
    if b == 0:
        return a
    c = a % b
    return greatest_common_divisor(b,c)

greatest_common_divisor(3,2)'''


'''Problem 6'''
'''def product():
    count = 1
    while True:
        user_input = int(input("Enter your number: \n"))
        if user_input == -1:
            print(product)
            break
        else:
            return count = count * user_input
        
print(product())'''
'''Problem 7'''
''''proficiency = float(input("What is your proficiency on a scale of 1-10: \n"))
available = input("Are you available to start [Y/N]: \n").lower()
while True:
    if ((proficiency >= 7.5) and (available == 'y')):
        print("Hired")
        break
    more_candidates = input("Are there more candidates? [Y/N]").lower()
    if more_candidates == 'y':
        proficiency = float(input("What is your proficiency on a scale of 1-10: \n"))
        available = input("Are you available to start [Y/N]: \n").lower()
    else:
        break
'''

some_list = [1,2,3]
len_of_sl = len(some_list)

for index in range (len_of_sl):
    print(some_list[index])
    some_list[index] += 2
    some_list[index] *= 2
    print(some_list[index])
