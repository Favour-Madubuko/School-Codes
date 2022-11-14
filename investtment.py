#INVESTMENT CALCULATOR
'''This program calculates the investment from information provided by the user which the program requests for'''
check=['1','2','3','4','5','6','7','8','9','0']
#This block of code contains a function which collects user's information and performs the arithmetic calculation
print("**********WELCOME TO THE INVESTMENT CALCULATOR**********")
def Principal():
    try:
        P = float(input("What is the amount you are depositing in GHC:\n "))   
    except Exception as v:
        print("Please input numbers")
        Principal()
    return P 
    
def Rate():
    try:
        i = float(input("What is the interest rate you want (in percentage):\n "))    
    except Exception as v:
        print("Please input numbers")
        Rate()
    return i
    
def Time():
    t = input("How long do you want to invest (in years):\n")
    if t not in check:
        Time()
    else:
        return int(t)
    
    
def Type():
    try:
        interest = str(input("Do you want a simple or compound interest? Press 'S' for simple and 'C' for compound\n").upper())
    except Exception as v:
        print('Invalid input')
        Type()
    return interest
    
a=Principal()
b=Rate()
c=Time()
d=Type()    
    
    #The block of code contains the conditionals and tests the user input to perform calculation
if d=='S':
    r = b/100
    #The simple interest amount calculated is rounded to two decimal places for best practices
    Amount = round((a * (1 + r*c)),2)
    print(f"You deposited GHC {a} at a rate of {b}% and your simple interest after {c} years will be: GHC {Amount}")
elif d=='C':
     r = b/100
     #The compound interest amount calculated is rounded to two decimal places for best practices
     Amount = round((a * ((1+r)**c)),2)
     print(f"You deposited GHC{a} at a rate of {b}% and your compound interest after {c} years will be: GHC{Amount}")
#The block of function is called here 


'''This part of the program solves for repetition, instead of running the program repetitively, it basically asks the user if they want to continue
or make another calculation, and depending on user choice it continues or ends'''

#This line of code requests the user to choose the investment type and the input in the string is converted to a lower case automatically
#should the user input the data while the capslock is on 
#another_calculation = input("Do you want to make another calculation. Type 'Y' to continue and type 'N' to stop: \n").lower()

#This block of code handles the repetition while the user input is true for continuation
#while another_calculation == 'y':
#    a=Principal()
#    b=Time()
#    c=Rate()
#    d=ype()
#    another_calculation = input("Do you want to make another calculation. Type 'Y' to continue and type 'N' to stop: \n").lower()
#This block of code ends the repetition of the user input is false for continuation
#if another_calculation == 'n':
print("\n<---------Thank you for calculating your interest, see you next time--------->\n")



