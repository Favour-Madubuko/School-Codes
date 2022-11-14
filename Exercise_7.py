#This program checks the days of the week using the user input
checked = int(input("Which number do you choose: "))
list_of_weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#This line of code loops through the list of weekdays
for i in range(len(list_of_weekdays)):
    #This line checks the input against the looped value
    if checked == i:
       #It prints the weekday the user inputs
       print(list_of_weekdays[checked-1])