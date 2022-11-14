#A program that computes for the seven days of the week

#This line welcomes the user
#print('Welcome to the Weekday Checker')

weekdays = {
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    7:"Saturday"
    }
#Collects the input from the user
checked = int(input('Choose a number between 1-7: '))

for key in weekdays.keys():
    if key == checked:
        wordday = weekdays[key]     
print(wordday)