import random
import turtle

tim = turtle.Turtle()
# tim.shape("turtle")
turtle.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)


for i in range(int(360 / 2)):
    tim.color(random_color())
    tim.circle(150)
    tim.left(2)

screen = turtle.Screen()
screen.exitonclick()