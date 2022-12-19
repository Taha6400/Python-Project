
from playsound import playsound
from re import X
import turtle
import os

wn = turtle.Screen()
wn.title("Python-Project")
wn.bgpic("s.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player

player = turtle.Turtle()
player.color("green")
player.shapesize(stretch_wid=2.5, stretch_len=2.5)
player.penup()
player.speed(3)
player.goto(00,-170)
player.shape("circle")

# Object

o = turtle.Turtle()
o.color("yellow")
o.penup()
o.shape("circle")
o.goto(219,-108)
o.shapesize(stretch_wid=2, stretch_len=2)

# Function


def paddle_a_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def paddle_a_down():
    y = player.ycor()
    y -= 20
    player.sety(y)
    
def paddle_a_right():
    x = player.xcor()
    x += 20
    player.setx(x)

def paddle_a_left():
    x = player.xcor()
    x -= 20
    player.setx(x)



#Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")


# Main game loop
while True:
    wn.update()