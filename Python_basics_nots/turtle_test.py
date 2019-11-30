rom turtle import *
import turtle
import random

color_pen = ['red', 'yellow', 'blue', 'grey', 'cyan', 'purple', 'green']
color_back = ['red', 'yellow', 'blue', 'grey', 'cyan', 'purple', 'green']

print(color_pen[2])
print(color_back[3])

def color_fill(pen_color, back_color):
    turtle.color(pen_color, back_color)

def f():
    turtle.fd(50)
    turtle.lt(60)

while True:
    i = 0
    for p in range(len(color_pen)):
        for b in range(len(color_back)):
                i += 1
                if i > 10:
                    for i in range(1,100):
                        turtle.begin_fill()
                        turtle.forward(200)
                        turtle.left(170)
                        turtle.end_fill()
                        continue
                    i = 0
                turtle.speed('fastest')
                turtle.color(color_pen[p], color_back[b])
                #if j > 20:
                #    turtle.bgcolor(color_back[b])
                #    turtle.clear()
                #print(turtle.window_height())
                #print(turtle.window_width())
                turtle.penup()
                turtle.goto(random.randrange(-turtle.window_width(), turtle.window_width()), random.randrange(-turtle.window_height(), turtle.window_height()))
                #turtle.goto(0, 0)
                turtle.pendown()
                #print(random.randrange(turtle.window_height()))
                #print(random.randrange(turtle.window_width()))
                #turtle.ht()
                turtle.pensize(random.randrange(20))
                turtle.hideturtle()
                turtle.begin_fill()
                #turtle.circle(random.randrange(200))
                turtle.fd(random.randrange(200))
                turtle.lt(random.randrange(200))
                turtle.bk(random.randrange(200))
                turtle.rt(random.randrange(200))
                turtle.end_fill()
                turtle.penup()
                turtle.goto(random.randrange(-turtle.window_width(), turtle.window_width()), random.randrange(-turtle.window_height(), turtle.window_height()))
                turtle.pendown()
                turtle.bk(random.randrange(200))
                turtle.penup()
                #turtle.goto(random.randrange(-turtle.window_width()/2, turtle.window_width()/2), random.randrange(-turtle.window_height()/2, turtle.window_height()/2))
                turtle.goto(random.randrange(-turtle.window_width(), turtle.window_width()), random.randrange(-turtle.window_height(), turtle.window_height()))
                turtle.pendown()
                turtle.pensize(random.randrange(100))
                turtle.lt(random.randrange(200))
                #turtle.circle(random.randrange(200))
                turtle.penup()
                turtle.pen(fillcolor="black", pencolor="red", pensize=10)