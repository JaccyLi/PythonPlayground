import turtle
from turtle import *
import random


s = turtle.Screen()

def f():
    fd(random.randint(0, 100))

def l():
    lt(90)

def r():
    rt(90)

s.listen()
s.onkey(f, "Up")
s.onkey(l, "Left")
s.onkey(r, "Right")

turtle.mainloop()
