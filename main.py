from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def mover_forwards():
    tim.forward(10)
def mover_backwards():
    tim.back(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)
def clockwise():
    tim.circle(50)
def clear():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=mover_forwards)
screen.onkey(key="s", fun=mover_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
