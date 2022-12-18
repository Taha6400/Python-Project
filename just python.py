import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)

# the player
player = turtle.Turtle()
player.color("white")
player.shape("square")

# main game loop
while True:
    wn.update()
