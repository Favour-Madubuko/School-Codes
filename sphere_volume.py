"""
3.
A program calculating the volume of a sphere
"""

#Formula for Volume of Sphere is given to be = (1/3).pi.radius**2 * height

#The math module is imported for the math operation
import math

def Volume_of_sphere():
    radius = 2.5
    height = 4
    sphere_volume = round((1/3) * math.pi * (radius **2) * height, 2)
    print(sphere_volume, "cubic centimeters")
Volume_of_sphere()