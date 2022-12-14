#Leap year question
'''
def is_a_leap_year(year):
    #year = int(input("Enter the year you want to check: "))
    if ((year%400) == 0 or (year%100) != 0) and (year%4 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")
is_a_leap_year(1600)'''

'''
def allfiles(filename):
    open_file = open(filename)
    the_file = open_file.readline()
    the_dates = []
    the_rates = []
    for lines in the_file[1:]:
        the_data = lines.strip()
        the_data = the_data.split('\t')
        the_dates.append(the_data[0])
        the_rates.append(the_data[1])
    the_difference = (the_rates[-1] - the_rates[0])
    return the_difference
    filename.close()
print(allfiles('exchange rates.txt'))
'''
my_dict = {"Monday": "Lundi","Tuesday":"Mardi"}
for some_variable in my_dict:
    print(some_variable)
my_dict["Friday"] = "Vendredi"
some_day = my_dict.get("Friday","Unknown")
print(some_day)

words = ["go","come","up","down","stop","laugh","cry"]
i = 0
while (words[i] != "stop"):
    print(words[i],end="")
    i= i+1
    
text = "December is almost here"
ind = text.find("here")
new1 = text[:ind] + "xxx"
new2 = text.replace("almost","nearly")
print(new1)
print(new2)


def evaluate(age,gender):
    if (age >= 15):
        print("You can marry in Estonia")
    if (age >= 18):
        print("You can marry in Ghana")
        if (gender == "female"):
            print("You can marry in India")
        print("you can marry in most US States")
    if (age >= 21):
        if (gender == "male"):
            print("You can marry in India")
evaluate(17,"male")


