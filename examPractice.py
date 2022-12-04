#Leap year question
def is_a_leap_year(year):
    #year = int(input("Enter the year you want to check: "))
    if ((year%400) == 0 or (year%100) != 0) and (year%4 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")
is_a_leap_year(1600)


open_file = open('thedata.csv')
open_file.readlines()

the_dates = []
the_rates = []

def allfiles(filename):
    open_file = open(filename)
    open_file.readlines()
    the_dates = []
    the_rates = []
    for lines in open_file:
        the_data = lines.strip()
        the_data = the_data.split(',')
        the_dates.append(the_data[0])
        the_rates.append(the_data[1])
        the_difference = (the_rates[-1] - the_rates[0])
    filename.close()
    return the_difference
