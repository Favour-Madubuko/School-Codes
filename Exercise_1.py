#Grosspay Calculator
print("Welcome to grosspay Calculator")
hours = float(input("How many hours do you work? "))
rate = float(input("How much are you paid per hour? "))
#
Grosspay = round((hours * rate),2)
print(f"Your gross pay is Ghc{Grosspay}")