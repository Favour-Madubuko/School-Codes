"""
6.
Grading policy at Ashesi University
"""
#Function that takes a numerical score as a parameter and returns the correponding letter_grade and grade_point
def the_score(numerical_score):
    if numerical_score >= 85:
        the_grade = "A+"
        grade_point = 4.00
    elif numerical_score >= 80:
        the_grade = "A"
        grade_point = 4.00
    elif numerical_score >= 75:
        the_grade = "B+"
        grade_point = 3.50
    elif numerical_score >= 70:
        the_grade = "B"
        grade_point = 3.00
    elif numerical_score >= 65:
        the_grade = "C+"
        grade_point = 2.50
    elif numerical_score >= 60:
        the_grade = "C"
        grade_point = 2.00
    elif numerical_score >= 55:
        the_grade = "D+"
        grade_point = 1.50
    elif numerical_score >= 50:
        the_grade = "D"
        grade_point = 1.00
    elif numerical_score < 50:
        the_grade = "E"
        grade_point = 0.00
    else:
        the_grade = "I"
        grade_point = "---"
    #Since each conditional and its alternate returns 'the_grade' and 'grade_point', it is only called once and returned as a tuple for any result, which is immutable
    return (the_grade, grade_point)

#A function that takes the GPA and returns the corresponding honor categories
def GPA(CGPA):
    if CGPA >= 3.85:
        return "Summa Cum Laude"
    elif CGPA >= 3.70:
        return "Magna Cum Laude"
    elif CGPA >= 3.50:
        return "Cum Laude"
    else:
        return 'no'
#This takes the user's input for the number of courses they want to enter
numberofCourses = int(input("How many courses do you want to enter information for: \n"))

#The initialized list that stores 'the_grade' for the numberofCourses entered
result = []

#The total for 'grade_point' is initialized and the sum is updated after each iteration 
the_total = 0

#The iteration for the number of courses the user entered
for n in range(numberofCourses):
    enter = int(input("Enter your course scores: "))
    #The function call for the_score(numerical_score) which accepts the scores and stores the returned values in the variable 'display'
    display = the_score(enter)
    #The letter_grade and the grade_point is displayed
    print(f"Your letter grade is {display[0]} and your grade point average is {display[1]}")
    #The total for each 'grade_point'
    the_total += display[1]
    #The result is appended outside the for loop to the initialized list
    result.append(display[0])

#An initialized dictionary to store the letter_grades
the_count = {}

#An iteration of the list 'result'
for i in result:
    #Each of the looped item key and total number of occurences of the looped item in the dictionary is counted
    the_count[i] = result.count(i)

#An iteration of the dictionary to get the keys and values with the number of appearance (value) in the dictionary representing 'j' and the number of corresponding letter_grade (key) representing 'i'  
for i,j in the_count.items():
    print(f"You have {j} {i}'s")

#The total number of calculated GPA is divided by the numberofCourses
final_GPA = round(the_total/numberofCourses,2)

#The final result is displayed
print(f"Your GPA is {final_GPA} and you have {GPA(final_GPA)} honors")


# #palindrome
# def palindrome():
#     word = input('Enter a word: ')
#     if word == word[::-1]:
#         print('The word is a palindrome.')
#     else:
#         print('The word is not a palindrome.')
# palindrome()

# #Use recursion to check palindrome string
# def palindrome(word):
#     if len(word) <= 1:
#         return True
#     else:
#         if word[0] == word[-1]:
#             return palindrome(word[1:-1])
#         else:
#             return False
# print(palindrome('madam'))
    





    

    