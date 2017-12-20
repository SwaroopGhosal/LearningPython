import turtle

turtle.shape('classic')

def drawShape(angle,len,sides):
    for i in range(sides):
        turtle.forward(len)
        turtle.left(angle)

for _ in range(9):
    drawShape(60,100,6)
    turtle.left(60)

turtle.exitonclick()
