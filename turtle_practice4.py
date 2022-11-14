#Question 4
import turtle
import math


def polygon(t,length,n):
    sides = 360/n
    #The loop considers that for any n sides, it will draw the required shape
    for i in range(n):
        t.fd(length)
        t.lt(sides)

def circle(t,r):
    circumference = 2 * math.pi * r
    
    n = int(circumference/3) + 1
    #since circumference = length * n
    length = circumference/n
    polygon(t,length,n)
    
bob = turtle.Turtle()

circle(bob,180)

turtle.exitonclick()
