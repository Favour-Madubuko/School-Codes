"""
4.
A program that helps Mr. Mensah calculates the volume of water given the dimensions of the polytank
"""

#Function block to perform calculation for Mr. Mensah
def Volume_for_Mensah():
    height = float(input("Enter the height of your polytank in meters: ")) #1.5
    radius = float(input("Enter the radius of your polytank in meters: ")) #0.7
    #The volume of a cylinder is given by = pi * r**2 * h
    import math
    volume = round((float(math.pi * (radius**2)* height)),2)
    print(f"Your expected volume for the tank is {volume} cubic meters")
Volume_for_Mensah()
