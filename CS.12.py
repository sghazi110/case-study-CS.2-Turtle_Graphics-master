#CS.12
import turtle
def jump(n,x,y):
    n.penup()
    n.goto(x,y)
    n.pendown()
s=turtle.Screen()
s.bgcolor('black')
t=turtle.Turtle()                 #for text
t.color('deep pink')
style=('courier',16,'bold')
jump(t,-460,360)
t.write('Waxing cresent',font=style, align='left')
t.hideturtle()
g=turtle.Turtle()                 #for each background colour
g.pencolor('grey')
g.fillcolor('grey')
g.begin_fill()
jump(g,-460,250)
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
a=turtle.Turtle()                 #wasing cresent
a.pencolor('white')
a.fillcolor('white')
a.begin_fill()
jump(a,-400,260)
a.circle(40)
a.end_fill()
g.fillcolor('grey')
g.begin_fill()
jump(g,-420,260)
g.circle(40)
g.end_fill()

jump(t,-200,360)                # first quater
t.write('First Quater',font=style, align='left')
jump(g,-200,250)
g.fillcolor('grey')
g.begin_fill()
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
jump(a,-140,260)
a.begin_fill()
a.circle(40,180)
a.end_fill()

jump(t,10,360)                # waxing gibbous 
t.write('waxing gibbous',font=style,align='left')
jump(g,10,250)
g.begin_fill()
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
jump(a,60,260)
a.circle(40)





jump(t,220,360)              # full moon
t.write('full moon',font=style,align='left')
jump(g,220,250)
g.begin_fill()
for i in range(4):
    g.forward(110)
    g.left(90)
g.end_fill()
jump(a,270,260)
a.begin_fill()
a.circle(40)
a.end_fill()
g.hideturtle()
a.hideturtle()




