import turtle
#to make the bg black like the universe
turtle.bgcolor('black')

#to draw the sun
turtle.setpos(-60,-30)
turtle.color("red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.hideturtle()


#to draw the eight planets in proper position
sx=turtle.Turtle()
sx.shape('circle')
sx.setpos(125,0)
sx.shapesize(0.5)
sx.color('green')
sx.speed(0)

jx=turtle.Turtle()
jx.shape('circle')
jx.setpos(170,0)
jx.shapesize(0.5)
jx.color('yellow')
jx.speed(0)

dq=turtle.Turtle()
dq.shape('circle')
dq.setpos(208,0)
dq.shapesize(1)
dq.color('blue')
dq.speed(0)

hx=turtle.Turtle()
hx.shape('circle')
hx.setpos(260,0)
hx.shapesize(0.75)
hx.color('white')
hx.speed(0)

mx=turtle.Turtle()
mx.shape('circle')
mx.setpos(350,0)
mx.shapesize(1.5)
mx.color('orange')
mx.speed(0)

tx=turtle.Turtle()
tx.shape('circle')
tx.setpos(440,0)
tx.shapesize(1.2)
tx.color('brown')
tx.speed(0)

twx=turtle.Turtle()
twx.shape('circle')
twx.setpos(530,0)
twx.shapesize(1)
twx.color('pink')
twx.speed(0)

hwx=turtle.Turtle()
hwx.shape('circle')
hwx.setpos(687.5,0)
hwx.shapesize(1)
hwx.color('purple')
hwx.speed(0)


#to let them go with different speeds
i=0
import math
while True:
    sx.goto(125*math.cos(i/20),90*math.sin(i/20))
    jx.goto(152*math.cos(i/40)+18,105*math.sin(i/40))
    dq.goto(180*math.cos(i/75)+28,120*math.sin(i/75))
    hx.goto(213*math.cos(i/100)+47,135*math.sin(i/100))
    mx.goto(270*math.cos(i/135)+80,165*math.sin(i/135))
    tx.goto(335*math.cos(i/180)+105,195*math.sin(i/180))
    twx.goto(390*math.cos(i/220)+140,235*math.sin(i/220))
    hwx.goto(487.5*math.cos(i/250)+200,287.5*math.sin(i/250))
    i+=1




    
