import turtle
from time import sleep
import random

window = turtle.Screen()
window.title("space inavader ")
window.setup(width=500,height=500)
window.bgcolor("black")
window.tracer(0)

#turtle to make score write

score = turtle.Turtle()
score.pen()
score.goto(-230,210)
score.color("blue")
score.write("Welcome to the game",align="left",font=("Arial",24,"normal"))

# to hide the write in 1 sec
sleep(1)
score.hideturtle()
score.clear()

fire = turtle.Turtle()
fire.shape('square')
fire.color('white')
fire.penup()
fire.goto(0,-220)



fire1 = turtle.Turtle()
fire1.penup()
fire1.color('red')
fire1.hideturtle()
fire1.speed(700)

body = turtle.Turtle()
body.penup()
body.shape('circle')
body.color('blue')
body.shapesize(0.5,0.5)
body.hideturtle()


def move_left():
    x = fire.xcor()
    y = fire.ycor()

    x = x - 20
    if x < -230:
        x = -230

    fire.goto(x,y)

def move_right():
    x = fire.xcor()
    y = fire.ycor()
    x = x +20
    if x > 230:
        x = 230

    fire.goto(x,y)

segment1 = []

def bullet():
    global fire1

    fire1 = turtle.Turtle()
    segment1.append(fire1)
    fire1.penup()
    fire1.color("red")
    x = fire.xcor()
    y = fire.ycor()
    fire1.goto(x+1, y+1)
    fire1.left(90)






window.listen()
window.delay(10)

window.onkeypress(move_left,'Left')
window.onkeypress(move_right,'Right')
window.onkeypress(bullet,'space')


segment = []

for _ in range(5):

   segment.append(turtle.Turtle())
#
for ball in segment:
    ball.penup()
    ball.shape('circle')
    ball.color("green")
    x= random.randint(-100,200)
    y= random.randint(-100,200)
    ball.goto(x,y)
    ball.shapesize(0.5, 0.5)
    ball.dx = 2
    ball.dy = 1
    print(ball)



value = 0

while True:

    window.update()


    sleep(0.04)
    for segm in segment1:

        b = segm.ycor()
        b = b+20
        segm.sety(b)


    for ball in segment:

        ball.setx(ball.xcor()+ball.dx)

        if fire1.distance(ball) <= 15:
            score.clear()
            value = value + 1
            ball.hideturtle()
            score.write("Score ={} ".format(value),align="left", font=("Arial", 24, "normal"))

            segment.append(ball)
            ball.goto(-230,200)
            ball.showturtle()



        if ball.distance(body)<=10:
            score.goto(0,0)
            score.penup()
            window.clear()
            score.write("Gameover", align="left", font=("Arial", 24, "normal"))
            sleep(2)

        if ball.xcor() > 230:



            ball.sety(ball.ycor()-(ball.dy)*20)
            ball.dx = ball.dx * -1



        if ball.xcor()<-230:
            ball.sety(ball.ycor() - (ball.dy) * 20)
            ball.dx = ball.dx * -1



































