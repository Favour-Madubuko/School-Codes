"""
5.
A program that takes the age of a person in months and displays it in years and months
"""
def number_of_months(the_month):
    #Number of months in a year is 12
    Month_number = 12
    years = the_month // Month_number
    months = (the_month % Month_number)
    print(f"You are {years} years and {months} months old")
number_of_months(57)

