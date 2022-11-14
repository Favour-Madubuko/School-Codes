'''
1. The difference between the int() function and the round() function is that
during mathematical operations and its output,
the int() function converts the value passed into it to a standalone
integer number by truncating the decimal and returning only the numeric integer equivalent
'''

#Example of an operation using int() function
Length = 12.5
Breadth = 10.45
Area = 12.5 * 10.45    #130.625
print(Area)            #130.625
print(int(Area))       #130

'''
while
the round() function returns the floating point number rounded to the user's specified number of decimals
and does not truncate the decimals
'''
#Example of an operation using round() function
Length = 12.5
Breadth = 10.45
Area = 12.5 * 10.45     #130.625
print(Area)             #130.625
print(round(Area,2))    #130.62, rounded to 2 decimal places

'''
2. Surface area of a cone is given by: Surface Area = Pi*r(r + sqrt(h**2 + r**2))
'''
#Importing the Math module
import math


#Defining the function to solve the surface area of cone
def Surface_area(radius,height):
    #Calling the radius and height values inside the variable, Area
    Area = math.pi * radius *(radius + (math.sqrt((height**2 + radius**2))))
    print(int(Area))            #1086       
Surface_area(13,4)


'''
3. Volume of a cone is given by: Volume = 1/3 * Pi * r**2 * h
'''
#Defining the function to solve the Volume of a cone 
def Volume(radius,height):
    #Calling the radius and height values inside the variabel, Area
    Area = (1/3) * math.pi * (radius ** 2) * height
    print(int(Area))        #707
Volume(13,4)

print(round(24.5))