import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)

def circle(t, r):
    n = int((2*math.pi*r / 3) + 1)
    polygon(t, (2 * math.pi * r) / n, n)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t,r):
    arc(t, r, 360)

myturtle = turtle.Turtle()

#square(myturtle,50)

#polygon(myturtle,50,5)

circle(myturtle, 100)

arc(myturtle,50, 90)

turtle.mainloop()
