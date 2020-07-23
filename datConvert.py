from turtle import *
import numpy as np
from array import array
import ctypes

screen = Screen()
turtle3 = Turtle()
turtle2 = Turtle()
turtle = Turtle()
screen.setup(1000, 600)
turtle.hideturtle()
turtle2.hideturtle()
turtle3.hideturtle()
turtle2.color("red")
turtle3.color('blue')
turtle3.penup()
turtle3.goto(500, 0)
turtle3.pendown()
turtle3.goto(-500, 0)
with open('n1201.dat', 'rb') as file:
    # data = bytes(file.read(16))
    # data = int.from_bytes(file.read(), "little")
    data = file.read()
    hexData = data.hex(':', 2)
    thing = hexData.split(':')
    final = []
    for item in thing:
        temp = ctypes.c_short(item)
        final.append(temp.value)
    ch1 = []
    ch2 = []
    for x in range(0, final.__len__()):
        if(x % 2 == 0):
            ch2.append(final[x])
        else:
            ch1.append(final[x])

    # turtle.color('green')
    # turtle.penup()
    # turtle.goto(500, 0)
    # turtle.pendown()
    # turtle.goto(-500, 0)
    # turtle.color('black')
    turtle.penup()
    turtle.goto(-500, 150)
    turtle2.penup()
    turtle2.goto(-500, -150)
    for x in range(0, ch1.__len__()):
        turtle.goto(turtle.xcor()+2, (ch1[x]/250)+150)
        turtle.pendown()
        turtle2.goto(turtle2.xcor()+2, (ch2[x]/250)-150)
        turtle2.pendown()
        if x % 500 == 0:
            turtle.clear()
            turtle2.clear()
            turtle.color('green')
            turtle2.color('green')
            turtle.penup()
            turtle2.penup()
            turtle.goto(500, 150)
            turtle2.goto(500, -150)
            turtle.pendown()
            turtle2.pendown()
            turtle.goto(-500, 150)
            turtle2.goto(-500, -150)
            turtle.color('black')
            turtle2.color('red')
            turtle.penup()
            turtle2.penup()
            turtle.setx(-500)
            turtle2.setx(-500)
    turtle.exitonclick()
    # for x in range(-300, 300):
    #     turtle.goto(x,x)
    #     turtle.pendown()