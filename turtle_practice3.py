#Question 3
import turtle


def polygon(t,length,n):
    sides = 360/n
    #The loop considers that for any n sides, it will draw the required shape
    for i in range(n):
        t.fd(length)
        t.lt(sides)
bob = turtle.Turtle()

polygon(bob,100,6)

turtle.exitonclick()
