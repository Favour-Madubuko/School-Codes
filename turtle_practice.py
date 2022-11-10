#Question 1
import turtle

def square(t):
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
  
bob = turtle.Turtle()
#Passing bob as an argument to the square
square(bob)

#The turtle screen exits on click
turtle.exitonclick()