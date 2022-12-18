from re import X
import turtle

wn = turtle.Screen()
wn.title("Python-Project")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.shapesize(stretch_wid=2.5, stretch_len=2.5)
player.penup()
player.goto(00,0)

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
