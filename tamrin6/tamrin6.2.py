import turtle

p = turtle.Pen()
side=3
size = 40
penup=10
p.shape("turtle")
while True:
    angle = 360/side
    for i in range(side):

        p.forward(size)
        p.left(angle)
   
    p.right(90)
    p.penup()
    p.forward(penup)
    p.right(90)
    p.forward(5)
    p.left(180)
    p.pendown()
    side+=1
    size+=10
    penup+=3
    if side==10:
        break
turtle.done()