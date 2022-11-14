#A program that computes for the seven days of the week

#This line welcomes the user
print('Welcome to the Weekday Checker')
#Collects the input from the user
checked = int(input('Choose a number between 1-7: '))

#Using conditionals to check the user input against the numbers available
if checked == 1:
    print("The day of the week chosen is Sunday")
elif checked == 2:
    print("The day of the week chosen is Monday")
elif checked == 3:
    print("The day of the week chosen is Tuesday")
elif checked == 4:
    print("The day of the week chosen is Wednesday")
elif checked == 5:
    print("The day of the week chosen is Thursday")
elif checked == 6:
    print("The day of the week chosen is Friday")
elif checked == 7:
    print("The day of the week chosen is Saturday")
else:
    print("The number is not a weekday")