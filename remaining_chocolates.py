"""
2.
A program calculating the chocolate bars each person gets and the remaining chocolates after division
"""

#Function definition calculating chocolates per student and remaining chocolates
def chocolates():
    chocolate_bars = 213
    registered_students = 133
    chocolate_per_student = (chocolate_bars // registered_students) #1
    remaining_chocolates = (chocolate_bars % registered_students) #80
    print(chocolate_per_student, "chocolates")
    print(remaining_chocolates, "chocolates")
chocolates()