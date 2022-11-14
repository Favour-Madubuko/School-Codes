'''
1.
A program calculating the percentage increase between two semesters
'''
#Initialized Global Variables
first_semester = 62
second_semester = 133

#Function definition for the percent increase
def PercentIncrease():
    the_difference = (second_semester - first_semester) #71
    #Percent increase is calculated by dividing the_difference by the value of first_semester and multiplying by 100
    percent_increase = round((the_difference/first_semester) * 100) #115
    print(f"The percentage increase between the students that took programming in the second semester compared to the first semesters is {percent_increase}")
PercentIncrease()

    
    
    
    