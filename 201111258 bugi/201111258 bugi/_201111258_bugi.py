import turtle
import math
import time
import random

def addTurtle():
    global num
    bugi.append('bugi')
    bugi[num] = turtle.Turtle()
    bugi[num].shape('turtle')
    bugi[num].goto(0,0)
    bugi[num].color(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    bugi[num].penup()
    num = num + 1

def speedUp() :
    global speed
    if speed < 10 :
        speed = speed+1

def speedDown() :
    global speed
    if speed > 0 :
        speed = speed-1

def moveTurtle(radius):
    while True:
        global speed
        screen.onkey(speedUp, "Up")
        screen.onkey(speedDown, "Down")
        screen.onkey(addTurtle, "space")
        screen.listen()
        for turtle in screen.turtles():
            if turtle.distance(0,0) > radius:
                turtle.forward(-(speed*2))
                turtle.setheading(random.randrange(0,360,10))
            else :
                turtle.forward(speed)


screen = turtle.Screen()
screen.title('201111258 GoGwangWoon')
screen.colormode(255)

num = 0
speed = 3
nSides = 5
bugi = []

addTurtle()
bugi[0].goto(-screen.window_width()/2+20,screen.window_height()/2-40)
bugi[0].write("거북이 추가 : Space, 속도 :↑,↓", move=False, align="left", font=("Arial", 10, "normal"))
bugi[0].goto(0,-200)
bugi[0].begin_fill()
bugi[0].circle(200)
bugi[0].end_fill()
time.sleep(1)

bugi[0].color('red')
bugi[0].circle(200)
bugi[0].goto(0,0)
time.sleep(1)

        

moveTurtle(200)
