import turtle

turtle.shape('classic')

def drawShape(angle,len,sides):
    for i in range(sides):
        turtle.forward(len)
        turtle.left(angle)
    #print(turtle.heading())

for j in range(6):
    #my code - for _ in range(3):
    drawShape(60,100,6)
    turtle.forward(100)
    turtle.right(60)
        #my code - turtle.left(120)
        #print(turtle.heading())
    #my code - turtle.right(360)
    #my code -turtle.forward(100)
turtle.exitonclick()
