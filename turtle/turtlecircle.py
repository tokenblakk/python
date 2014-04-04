__author__ = 'Tramel Jones'
'''
Turtle drawing application draws circle using OOP
'''
import turtle
import math
from turtle import Turtle


def drawCircle(t,x,y,rad):
    t.hideturtle()
    t.up()
    t.setposition(x,y+rad)
    dist = (2*math.pi*rad)/120
    t.color('green','blue')
    t.down()
    t.showturtle()
    t.begin_fill()
    while True:
        t.forward(dist)
        t.left(3)
        if abs(t.pos()) <1:
            break
    t.end_fill()
    turtle.done()

_x = int(input("Enter an x value: "))
_y = int(input("Enter a y value: "))
_rad = int(input("Enter a radius: "))

t = Turtle()
window = turtle.Screen()
draw = t
drawCircle(t,_x,_y,_rad)
window.mainloop()





