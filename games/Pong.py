# a simple game
# a exercise sample


import random
import turtle


color = ["white", "yellow", "blue", "green", "cyan", "grey"]
speed_num = [1, 3, 6, 10, 0]

# Score
score_a = 0
score_b = 0

score = turtle.Turtle()
score.color("purple")
score.penup()
score.hideturtle()
score.goto(0, 350)
score.write("Player A: 0  Player B: 0", font="Arial", align="center")



# Screen def
win = turtle.Screen()
win.title("Pong by stevenux")
win.bgcolor("black")
win_width = turtle.window_width()
win_height = turtle.window_height()
print(win_height)
print(win_width)
win.setup(width=win_width, height=win_height)
win.tracer(0)

# Paddle A left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=8, stretch_len=1)
paddle_a.color("yellow")
paddle_a.penup()
paddle_a.goto(-(win_width/2 - 20), 0)
paddle_a.dy = 0.5

# Paddle B right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=8, stretch_len=1)
paddle_b.color("yellow")
paddle_b.penup()
paddle_b.goto((win_width/2 - 30), 0)
paddle_b.dy = 0.5

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Flag
flag = turtle.Turtle()
flag.shape('circle')
flag.color('yellow')
flag.goto(0, 0)
# distance measure

print(paddle_a.distance(-win_width/2, 0))
print(ball.distance(-win_width/2, 0))

# Move paddle_a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 60
    paddle_a.sety(y)
    rand_color = color[random.randint(0, 5)]
    paddle_a.color(rand_color)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)
    rand_color = color[random.randint(0, 5)]
    paddle_a.color(rand_color)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 60
    paddle_b.sety(y)
    rand_color = color[random.randint(0, 5)]
    paddle_b.color(rand_color)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)
    rand_color = color[random.randint(0, 5)]
    paddle_b.color(rand_color)

# Speed ctrl

# Key binding

win.listen()
win.onkey(paddle_a_up, "w")
win.onkey(paddle_a_down, "s")
win.onkey(paddle_b_up, "Up")
win.onkey(paddle_b_down, "Down")

while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #paddle_a.sety(paddle_a.ycor() + paddle_a.dy)

    if ball.ycor() > win_height/2 - 10:
        ball.sety(win_height/2 - 10)
        ball.dy *= -1

    if ball.ycor() < -win_height/2 + 20:
        ball.sety(-win_height/2 + 20)
        ball.dy *= -1

    if ball.xcor() > win_width/2:
        #ball.setx(win_width/2)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A: {} | Player B: {}".format(score_a, score_b), font="Arial", align="center")
        ball.dx = float(random.uniform(0.1, 1))
        print(ball.dx)
        ball.dx *= -1

    if ball.xcor() < -win_width/2:
        #ball.setx(-win_width/2)
        ball.goto(0, 0)
        score_b += 1
        score.clear()
        score.write("Player A: {} | Player B: {}".format(score_a, score_b), font="Arial", align="center")
        ball.dx = float(random.uniform(0.1, 1))
        print(ball.dx)
        ball.dx *= -1

    if ball.xcor() > win_width/2 - 50 and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() - 80):
        ball.setx(win_width/2 - 50)
        ball.dx = float(random.uniform(0.1, 1))
        rand_color = color[random.randint(0, 5)]
        ball.color(rand_color)
        ball.dx *= -1

    if ball.xcor() < -win_width/2 + 40 and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() - 80):
        ball.setx(-win_width/2 + 40)
        rand_color = color[random.randint(0, 5)]
        ball.color(rand_color)
        ball.dx *= -1
        ball.dx = float(random.uniform(0.1, 1))



