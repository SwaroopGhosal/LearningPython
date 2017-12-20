import turtle
import math
turtle.shape('turtle')

# function to draw a line with right angle tilt
def lineRight(tilt, length):
    turtle.right(tilt)
    turtle.pendown()
    turtle.forward(length)

# function to draw a line with left angle tilt
def lineLeft(tilt, length):
    turtle.left(tilt)
    turtle.pendown()
    turtle.forward(length)

# function to calculate the length of the hypotenuse of a triangle
# given two sides
def hypLen(side1, side2):
    len = math.sqrt(side1**2 + side2**2)
    return len
    


turtle.width(5)
lineRight(0,100)
lineLeft(120,100)
lineLeft(120,100)
lineLeft(30,100)
lineLeft(90,100)
lineLeft(90,100)
len = hypLen(100,100)
lineLeft(135,len)
turtle.penup()
turtle.right(135)
turtle.forward(100)
lineRight(135,len)


turtle.exitonclick()
