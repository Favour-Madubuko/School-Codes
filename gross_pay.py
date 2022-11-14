#This program calculates the hourly pay for employee
print('Welcome to the salary calculator')
#User inputs the number of hours
number_of_hours = int(input("How many hours did you work: "))
#Initialized or fixed rate
rate = int(input("What is your payrate: "))
#initialized number of hours
hours = 40

#This block of conditional calculates if the number of hours equals the initialized number of hours
#if number_of_hours == 40:
#    calculated_1 = hours * rate
#    print (f"Your total pay is: ${calculated_1}")

#This block of conditional calculated it the number of hour is less than the initialized number of hours
if number_of_hours <= 40:
    calculated_2 = number_of_hours * rate
    print(f"Your total pay is: ${calculated_2}")
#This block finally checks if the number of hours is greater than the initialized number of hours for the rate given
else:
    number_of_hours > 40
    Extra_hour = number_of_hours - 40
    finalized = (rate * hours) + Extra_hour * (rate * 1.5)
    print(f"Your total pay is: ${finalized}")

