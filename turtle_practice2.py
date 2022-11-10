#Question 2
import turtle


def square(t,length):
    #The loop considers that a square has 4 sides
    for i in range(4):
        t.fd(length)
        t.rt(90)

bob = turtle.Turtle()

square(bob,300)

turtle.exitonclick()