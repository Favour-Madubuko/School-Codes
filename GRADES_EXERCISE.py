print("Choose the number for operation option below:")
response = input("1. Register students\n2. Enter student's grades\n3. Display list of students:\n\t")


def Register_Students():
    number_of_students = int(input("What number of students do you want to register:\n"))
    registered_students = []
    for students in range(number_of_students):
        name = input("Enter student name").capitalize()
        registered_students.append(name)