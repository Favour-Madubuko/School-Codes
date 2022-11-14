from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake game")
screen.tracer(0)

#Making a list of tuples with the position of the snake
body_positions =[(0,0),(-20,0),(-40,0)]

#Creating a list for the snake bodies so that once the snake increases the squares increase
snake_bodies = []
#A loop through the positions which has been refactored using the for loop.
for positions in body_positions:
    body = Turtle("square")
    body.color("white")
    body.penup()
    body.goto(positions)
    snake_bodies.append(body)

    
#This section of code deals with makin the snake move
snake_active = True

while snake_active:
    for bodies in snake_bodies:
        bodies.forward(20)
        
screen.update()








screen.exitonclick()