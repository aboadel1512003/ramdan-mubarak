# ramdan-mubarak
import turtle
import time
import turtle
import random
wn=turtle.Screen()
turtle.bgcolor('black')
turtle.shape('turtle')
time.sleep(2)
tr=turtle.Turtle()
ts=turtle.Turtle()
tt=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
move=1
t5.speed('fastest')
for i in range (10):
    for i in range (4):
        t5.pu()
        t5.goto(500,200)
        t5.pd()
        t5.color('cyan')
        t5.pensize(3)
        t5.circle(50,steps=4)
        t5.right(100)

t=turtle.Turtle()
turtle.left(520)
w=turtle.Screen()

turtle.speed(3)
w.bgcolor("black")

t.color("white")
w.title("Ramdan Mubarak " "Made by:Abdelrahman Adel")
t.up()
t.goto(0,-300)
t.down()
t.color("white")
t.begin_fill()
t.circle(200)
t.end_fill()
t.hideturtle()
t.up()
t.goto(50,-300)
t.down()
t.color("black")
t.begin_fill()
t.circle(200)
t.end_fill()
t.hideturtle()

import turtle as t
t.speed(10000)
angle=150
side=90
pointies=5
ROTATION=360/pointies
angle_left=angle
angle_right=angle
t.color("gray","ghost white")
for j in range(10):
    t.begin_fill()
    for k in range (pointies):
        t.forward(side)
        t.right(angle_right)
        t.forward(side)
        t.left(angle_left)
        t.right(ROTATION)
    t.end_fill()
    t.right(2)
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.color("white")
turtle.right(100)
turtle.write("Ramdan Mubarak",font=('Verdana',28,"bold"))
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.color("white")
turtle.right(100)
turtle.write("       Made By:",font=('Verdana',28,"bold"))

turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
turtle.color("white")
turtle.right(100)
turtle.write("Abdelrahman Adel",font=('Verdana',28,"bold"))
ts.speed("fastest")
t5.speed("fastest")
for i in range (10):
    for i in range (4):
        t5.pu()
        t5.goto(-500, 200)
        t5.pd()
        t5.color("yellow")
        t5.pensize(3)
        t5.circle(50,steps=4)
        t5.right(100)
t5.speed("fastest")
for i in range (10):
    for i in range (4):
        t5.pu()
        t5.goto(500, -200)
        t5.pd()
        t5.color("pink")
        t5.pensize(3)
        t5.circle(50,steps=3)
        t5.right(100)
for i in range (10):
    for i in range (4):
        t5.pu()
        t5.goto(-500, -200)
        t5.pd()
        t5.color("green")
        t5.pensize(3)
        t5.circle(50,steps=3)
        t5.right(100)

for i in range (20):
    for i in range (2):
        ts.pensize(2)
        ts.pu()
        ts.goto(0, 300)
        ts.pd()
        ts.forward(100)
        ts.circle(6, steps=3)
        ts.right(70)
        ts.color("purple")
        ts.forward(50)
        ts.right(120)
    ts.left(30)
ts.speed("fastest")
t3.speed("fastest")
for i in range (10):
    for i in range (2):
        t3.pensize(3)
        t3.pu()
        t3.goto(-320, 300)
        t3.color("light green")
        t3.begin_fill()
        t3.pd()
        t3.forward(30)
        t3.right(50)
        t3.color("green")
        t3.right(50)
        t3.circle(5, steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)
t3.speed("fastest")
for i in range (10):
    for i in range (2):
        t3.pensize(3)
        t3.pu()
        t3.goto(320, -300)
        t3.color("red")
        t3.begin_fill()
        t3.pd()
        t3.forward(30)
        t3.right(50)
        t3.color("orange")
        t3.right(50)
        t3.circle(5, steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)
t3.speed("fastest")
for i in range(10):
    for i in range(2):
        t3.pensize(3)
        t3.pu()
        t3.goto(320, 300)
        t3.pd()
        t3.color("light blue")
        t3.begin_fill()

        t3.forward(30)
        t3.right(50)
        t3.color("blue")
        t3.right(50)
        t3.circle(5, steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)
t3.speed("fastest")
for i in range(10):
    for i in range(2):
        t3.pensize(3)
        t3.pu()
        t3.goto(-320, -300)
        t3.pd()
        t3.color("orange")
        t3.begin_fill()

        t3.forward(30)
        t3.right(50)
        t3.color("red")
        t3.right(50)
        t3.circle(5, steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)
t3.speed("fastest")
'''for i in range(10):
    for i in range(4):
        t5.pu()
        t5.goto(600, 0)
        t5.pd()
        t5.color("white")
        t5.pensize(1)
        t5.circle(40, steps=5)
        t5.right(100)

    t5.right(60)'''
t5.speed("fastest")
t5.speed("fastest")
painter=turtle.Turtle()
painter.pencolor("green")

for i in range(50):
        painter.pu()
        painter.goto(600, 0)
        painter.pd()
        painter.forward(100)
        painter.left(123)

painter=turtle.Turtle()
painter.pencolor("red")

for i in range(50):
        painter.pu()
        painter.goto(-600, 0)
        painter.pd()
        painter.forward(100)
        painter.left(123)
turtle.done()
