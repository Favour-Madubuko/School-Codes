'''EXERCISE 2.2, QUESTION 2'''
#The defined function calculates the discount and performs computation based on the question given
def book_cost():
    discount = (40/100) * 24.95    #9.98
    new_price = 24.95 - discount   #14.97
    first_copy = 3
    additional_copy = (60 - 1) * (new_price + 0.75) #927.48
    total_cost = round((new_price + first_copy + additional_copy),2)
    print(f"The total cost is ${total_cost}")
book_cost()


'''EXERCISE 2.2, QUESTION 3'''
'''
The time I leave my house (6:52am) is in the form of 6 hours, 52 minutes which
will be converted to seconds, but the time 8:15 is in the form 8 minutes, 15 seconds,
same with 7:12 in the form 7 minutes, 12 seconds.
'''
#Converting my start time to seconds by multiplying minutes 60 and seconds by 3600
time_of_start = (6*3600) + (52*60)    #24720

'''Converting the time for easy pace by multiplying minutes by 60 and the output multiplied
twice because the easy pace is repeated twice'''
time_of_easypace = 2*((8*60) + 15)   #990


'''Converting the time of tempo by multiplying minutes by 60 and the total output multiplied
thrice because the pace is in seconds covered per mile'''
time_of_tempopace = 3*((7*60) + 12)  #1296

#The hour to get home for breakfast divived by 3600 to get the number of hours
hour_of_breakfast = int((time_of_start + time_of_easypace + time_of_tempopace)/3600)

#The minute to get home for breakfast in remaining seconds multiplied by the standard minutes
minute_of_breakfast = int((((time_of_start + time_of_easypace + time_of_tempopace)/3600) - hour_of_breakfast) * 60)

print(f"I get home at {hour_of_breakfast}.{minute_of_breakfast}am")








