import turtle as trtl
import random
Jay = trtl.Turtle()
Jay.speed(0)
Jay.ht()
Jay.pensize(3) 



player = trtl.Turtle()
count = 0 
distance = 40
Wall_width = 20
door_width = 20



def drawDoor():
    Jay.penup()
    Jay.forward(door_width)
    Jay.pendown()

def drawWall():
    Jay.left(90)
    Jay.forward(Wall_width*2)
    Jay.backward(Wall_width*2)
    Jay.right(90)

while (count < 26):
    if count > 4:
        Wall = random.randint(2*Wall_width, distance - 2*door_width)
        door = random.randint(door_width, distance - 2*door_width)
        if door < Wall:
            Jay.forward(door)
            drawDoor()
            Jay.forward(Wall - door - door_width)
            drawWall()
            Jay.forward(distance - Wall)
        else:
            Jay.forward(Wall)
            drawWall()
            Jay.forward(door - Wall)
            drawDoor()
            Jay.forward(distance - door - door_width)
    Jay.left(90)
    distance += Wall_width
    count = (count + 1)



wn = trtl.Screen()

player.pencolor("Green")
def Up():
    player.setheading(90)
    player.forward(10)

def Down():
    player.setheading(270)
    player.forward(10)

def Left():
    player.setheading(180)
    player.forward(10)

def Right():
    player.setheading(0)
    player.forward(10)


wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Left,"Left")
wn.onkeypress(Right, "Right")
wn.listen()

wn.mainloop()
