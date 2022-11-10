#Spring: 20 march - 20 june
#summer: 21 june - 21 sept.
#fall: 22 sept - 20 dec.
#winter: 21 dec - 19 march


month = input("Enter the month of the year: ").lower()
#months = ['january','february','march','april','may','june','july','august','september','october','november','december']
date = int(input("Enter the date of the month: "))
#all_dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

def spring():
    if month == "march" and date >= 20 and date < 31:
        print("spring")
    elif month == "april" and date >= 1 and date <= 30:
        print("spring")
    elif month == "may" and date >= 1 and date <= 31:
        print("spring")
    elif month == "june" and date >= 1 and date <= 20:
        print("spring")
    elif month == "june" and date >= 21 and date <=30:
        print("summer")
    elif month == "july" and date >= 1 and date <= 31:
        print ("summer")
    elif month == "august" and date >= 1 and date <= 31:
        print ("summer")
    elif month == "september" and date >= 1 and date <=21:
        print("summer")
    elif month == "september" and date >= 21 and date <= 30:
        print("fall")
    elif month == "october" and date >= 1 and date <= 31:
        print("fall")
    elif month == "november" and date >=1 and date <=30:
        print("fall")
    elif month == "december" and date >=1 and date <=20:
        print("fall")
    elif month == "december" and date >= 21 and date <= 31:
        print("winter")
    elif month == "january" and date >= 1 and date <= 31:
        print("winter")
    elif month == "february" and date >= 1 and date <=29:
        print("winter")
    elif month == "march" and date >= 1 and date <=19:
        print("winter")
spring()