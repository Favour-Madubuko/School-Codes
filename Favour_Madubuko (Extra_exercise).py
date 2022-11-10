'''Problem 5'''
def greatest_common_divisor(a,b):
    if b == 0:
        return a
    c = a % b
    return greatest_common_divisor(b,c)

greatest_common_divisor(3,2)


'''Problem 6'''
def product():
    user_input = int(input("Enter your number: \n"))
    count = 1
    while user_input >= 0:
        count = count * user_input
        user_input = int(input("Enter your number: \n"))
    return count
print(product())


'''Problem 7'''
proficiency = float(input("What is your proficiency on a scale of 1-10: \n"))
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






    
