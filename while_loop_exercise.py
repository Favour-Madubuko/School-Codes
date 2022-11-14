total = 0
count = 0
average = 0

while True:
    number = input("Enter a number: ")
    try:
        if number.lower() == "done":
            break
        total += float(number)
        count +=1
        average = total/count
    except:
        print("Invalid Input")
print(total,count,average)
