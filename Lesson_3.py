Year = int(input("Which year do you want to check? "))

def Leap_Year():
    if Year%4 == 0 and Year%100 ==0 and Year%400 == 0:
        print("This is a leap year")
    else:
        return 
        #print("This is not a leap year")
Leap_Year()