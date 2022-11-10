

'''def product():
    user_input = int(input("Enter a number:\n"))
    if user_input < 0:
        return 1
    return user_input * product()

print(product())'''
'''user_input = int(input("Enter a number:\n"))
def product(user_input):
    if user_input == 0:
        return 1
    return user_input * product(user_input-1)

print(product(user_input))'''


# Python program to display the Fibonacci sequence
'''tL = ['ban','key','list']
tt = 'blend'
print(tL[::1])
print(tt[1::-1])'''
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(9))

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))

number = int(input("Enter a number\n"))
if number <= 0:
    print("Invalid")
else:
    for i in range(number):
        print(Fibonacci(i))








