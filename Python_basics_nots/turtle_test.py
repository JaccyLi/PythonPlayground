import random
import turtle

rr = [i for i in range(100)]
ran_turn = random.choice([90, 45])

ran = random.choice(rr) * 50


def po_flower(x, y):
        color_r = random.choice([r for r in range(256)])
        color_g = random.choice([g for g in range(256)])
        color_b = random.choice([b for b in range(256)])
        turtle.colormode(255)
        turtle.pencolor(color_r, color_g, color_b)
        ran = random.choice(rr)
        turtle.speed('fastest')
        turtle.hideturtle()
        turtle.penup()

        turtle.goto(x, y)
        turtle.pensize(1)
        turtle.pencolor(color_r, color_g, color_b)
        turtle.fillcolor(color_r, color_g, color_b)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
        turtle.end_fill()
        ran_turn = random.choice([90, 45])
        turtle.lt(ran_turn)


while True:
    for i in range(8):
        po_flower(random.randrange(-600, 600, 300), random.randrange(-600, 600, 300))
