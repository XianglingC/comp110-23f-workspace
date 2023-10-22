"""TODO: Really simple version of go to the light house."""
__author__: str = "730658974"

"""The final 15% of the project: 
1. random: please see the draw_square function(startfrom line40)
2. new function/knowledge from the doc: please see the draw_circle and draw_semicircle part(the last two function).
    (lines 96 and 122)."""

from turtle import Turtle, colormode, done

def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    # The rectangle form the road
    i = 0
    x = -307
    size = 70
    # Using while and algbra to reset the position of next rectangle
    while i < 5:
        x += size
        draw_square(ertle, x, -50, 70)
        i += 1
    draw_rectangle(ertle, 100, -120, 100, 180)
    draw_tringle(ertle, 50, 60)
    draw_circle(ertle, 150, 230, 25)
    # Using loop to form the clouds
    idx = 0
    x = -300
    gap = 20
    while idx < 5:
        x += gap
        draw_cloud(ertle, x, 260, 15)
        idx += 1
    draw_semicircle(ertle, 10, -180, 35)
    draw_semicircle(ertle, -70, -200, 35)
    draw_semicircle(ertle, -150, -230, 35)
    draw_semicircle(ertle, 50, -135, 35)
    done()

def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width"""
    colormode(225)
    """Wanting to use random color for the color in this part."""
    import random
    """Introducing the string and the list for the random"""
    """I understand this function and how to use this by looking at this website: https://pynative.com/python-random-choice/"""
    colors: list[str] = ["green", "blue", "orange", "grey"]
    selected_color = random.choice(colors)
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.setheading(0)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.color(selected_color)
    a_turtle.begin_fill()
    i:int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float,length: float) -> None:
    """Draw the body of the light house"""
    colormode(225)
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.setheading(0) # magic plus
    a_turtle.pendown()
    a_turtle.pencolor("pink")
    a_turtle.fillcolor("brown")
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(length)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()

def draw_tringle(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw the head of the light house"""
    colormode(225)
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.setheading(0) # magic plus
    a_turtle.pendown()
    a_turtle.fillcolor("grey")
    a_turtle.begin_fill()
    i: int = 0
    while i < 3:
        a_turtle.forward(200)
        a_turtle.left(120)
        i += 1
    a_turtle.end_fill()

def draw_circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw the light by using circle"""
    colormode(225)
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.setheading(0) # magic plus
    a_turtle.pendown()
    a_turtle.fillcolor("yellow")
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()

def draw_cloud(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw the cloud using several circles"""
    colormode(225)
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.setheading(0) # magic plus
    a_turtle.pendown()
    a_turtle.pencolor("blue")
    a_turtle.fillcolor("blue")
    a_turtle.begin_fill()
    """Trying to use the circle from the documents, and want to use it to form the clouds."""
    a_turtle.circle(radius)
    a_turtle.end_fill()

def draw_semicircle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw the very very simple boat by using the semicircle."""
    colormode(225)
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.setheading(270)
    a_turtle.pendown()
    a_turtle.pencolor("red")
    a_turtle.fillcolor("red")
    a_turtle.begin_fill()
    """Wanting to use semicircle to draw the boat, but I don't think this is a beautiful one."""
    a_turtle.circle(radius, 180)
    a_turtle.end_fill()

if __name__ == "__main__":
    main()
