total = 0
count = 0
average = 0
Maximum = None
Minimum = None

while True:
    number = input("Enter a number: ")
    if number.lower() == "done":
            break
    else:
        try:
            if count == 0:
                maximum = float(number)
                minimum = float(number)
                count = 1
            else:
                if float(number) > maximum:
                    maximum = float(number)
                else:
                    if float(number) < minimum:
                        minimum = float(number)
        except:
            print("Invalid Input")
print(total,count,maximum,minimum)
            
        