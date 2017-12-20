import turtle

def mysquare(side,angle, tilt1, colored):
    turtle.color(colored,'blue')
    turtle.right(tilt1)
    for i in range(4):
        turtle.forward(side)
        turtle.right(angle)

turtle.shape('turtle')
turtle.width(10)
side = 100
angle = 90
num = 0
tilt = 0
colors = ['red','blue','green']
for num in range(3):
    mysquare(side, angle, tilt, colors[num])
    if num == 0:
        tilt = 20
turtle.exitonclick()


    
    
