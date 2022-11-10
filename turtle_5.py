#Question 5
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

def arc(t,r,angle):
    the_length = 2 * math.pi * r * (angle/360)
    n = int(the_length/3) + 1
    new_length = the_length/n
    the_angle = float(angle) / n
    polygon(t,new_length,n)
bob = turtle.Turtle()

arc(bob,1000,40)

turtle.exitonclick()

