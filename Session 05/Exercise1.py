import turtle

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

myturtle = turtle.Turtle()

square(myturtle)

turtle.mainloop()
