#INVESTMENT CALCULATOR
'''This program calculates the investment from information provided by the user which the program requests for'''

#This block of code contains a function which collects user's information and performs the arithmetic calculation
print(f"********** HELLO, WELCOME TO THE INVESTMENT CALCULATOR!**********")
def user_input():
#This line of code requests for the user's deposit data which is the PRINCIPAL and uses the float value to capture the decimals which is in pesewas
    P = float(input("What is the amount you are depositing in GHC:\n "))
    #This line of code requests the user's INTEREST rate in percentage and uses the float to capture the decimals should the user input a decimal rate
    i = float(input("What is the interest rate you want (in percentage):\n "))
    #This line of code requests the user's TIME in years and captures the data in float value should the user decide to include months
    t = float(input("How long do you want to invest (in years):\n"))
    #This line of code requests the user to choose the investment type and the input in the string is converted to a lower case automatically
    #should the user input the data while the capslock is on
    interest = input("Do you want a simple or compound interest? Press 'S' for simple and 'C' for compound  \n").lower()
    
    #The block of code contains the conditionals and tests the user input to perform specific interest calculation
    if interest == 's':
        r = i/100
        #The simple interest amount calculated is rounded to two decimal places for best practices
        Amount = round((P * (1 + r*t)),2)
        #The result is displayed
        print(f"If you deposit GHC {P} at a rate of {i}%, your simple interest after {t} years will be GHC {Amount}")
    elif interest == 'c':
         r = i/100
         #The compound interest amount calculated is rounded to two decimal places for best practices
         Amount = round((P * ((1+r)**t)),2)
         #The result is displayed
         print(f"If you deposit GHC{P} at a rate of {i}%, your compound interest after {t} years will be GHC {Amount}")
#The block of function is finally called here 
user_input()
#The final message for the user is printed
print("\nThank you for calculating your interest, see you next time\n")


