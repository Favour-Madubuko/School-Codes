#from turtle import Turtle, Screen
#window = Turtle()
#window. shape("classic")
#window.color("blue")
#window.forward(100)
#view = Screen()
#view.exitonclick()
#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()

user_input = int(input("Enter a number to check the month: "))
month = ["Jan.","Feb.","Mar.","Apr.","May","Jun.","Jul.","Aug.","Sept.","Oct.","Nov.","Dec."]

display = month[user_input -1]
print(display)


the_weight = float(input("What is the weight of the order: "))
#Before Shipping
cost_before_shipping = (the_weight * 10.5)
cost_with_shipping = (the_weight * 10.5) + (0.86 * the_weight) + 1.5
print(f"The cost of shipping goods is ${cost_with_shipping}")