""" Turtle_Tutorial."""

# Lines and turning
# leo.forward(50)
# leo.left(30)
# leo.right(40)

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# Change the speed
leo.speed()
leo.hideturtle()
# Color filled (two ways- 1. basic color: string "pink"；2. complex color: RGB )
# RGB
colormode(255)
# pen + filled color
#leo.color("green","yellow")
# pen
leo.pencolor("pink")
# fill color
#leo.fillcolor(32,67,93)

# Begin to fill the color
leo.begin_fill()
# Goto, penup and pendown
leo.penup()
leo.goto(-150,-50)
leo.pendown()

# Exercise 1: repeat something a certain times
i:int = 0
while(i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
# Stop the filling of the color
leo.end_fill()
# Maintain the turtle


bob: Turtle = Turtle()
colormode(225)
bob.color(17,17,17)
bob.penup()
bob.goto(-150,-50)
bob.pendown()
bob.speed(5)
bob.hideturtle()
i:int = 0
while(i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
bob.end_fill()

bob_2: Turtle = Turtle()
colormode(225)
bob_2.fillcolor(17,17,17)
bob_2.penup()
bob_2.goto(-150,-50)
bob_2.pendown()
bob_2.speed(5)
bob_2.hideturtle()
side_length: int = 300
i:int = 0
while(i < 100):
    bob_2.forward(side_length)
    bob_2.left(120)
    side_length *= 0.97
    i = i + 1
bob.end_fill()
done()