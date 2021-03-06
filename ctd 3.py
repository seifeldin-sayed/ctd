from turtle import *
speed(0)
bgcolor("black")
colors=["red","orange","yellow","green","blue","purple"]
penup()
goto(-200,150)
pendown()
for i in range(25):
    pencolor(colors[i%6])
    pensize(5)
    circle(50)
    left(20)
penup()
goto(200,150)
pendown()
for j in range(40):
    pencolor(colors[j%6])
    pensize(3)
    left(10)
    forward(70)
    left(90)
    forward(70)
    left(90)
    forward(70)
    left(90)
    forward(70)
    left(90)
penup()
goto(-200,-150)
pendown()
for k in range(35):
    pencolor(colors[k%6])
    pensize(3)
    left(10)
    forward(100)
    dot()
    left(120)
    forward(100)
    dot()
    left(120)
    forward(100)
    dot()
    left(120)
penup()
goto(200,-150)
pendown()
for l in range(150):
    pencolor(colors[l%6])
    pensize(l/100 +1)
    forward(l)
    left(61)
done()