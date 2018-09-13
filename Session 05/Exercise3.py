import turtle
import math


def l_polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def l_arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    l_polyline(t, n, step_length, step_angle)

def r_polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def r_arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    r_polyline(t, n, step_length, step_angle)

def circle(t,r):
    l_arc(t, r, 360)

def polygon(t, n, length):
    angle = 360.0 / n
    r_polyline(t, n, length, angle)


def shape1(t, r):
    circle(t,r)
    t.lt(60)
    for i in range(3):
        l_arc(t,r,120)
        t.lt(120)
    t.rt(60)
    l_arc(t,100,60)
    t.lt(60)
    for i in range(3):
        l_arc(t,r,120)
        t.lt(120)
    


def shape2(t, r):
    t.pensize(3)
    circle(t, r)
    t.lt(180)
    r_arc(t, r/2, 180)
    l_arc(t, r/2, 180)
    t.lt(90)
    t.penup()
    t.fd(r/3)
    t.pendown()
    t.rt(90)
    circle(t, r/6)
    t.penup()
    t.lt(90)
    t.fd(r)
    t.rt(90)
    t.pendown()
    circle(t, r/6)


myturtle = turtle.Turtle()
myturtle.speed(0)


shape1(myturtle, 100)
myturtle.penup()
myturtle.rt(60)
l_arc(myturtle, 100, 120)
myturtle.lt(90)
myturtle.fd(450)
myturtle.lt(90)
myturtle.pendown()
shape2(myturtle, 100)

turtle.mainloop()
