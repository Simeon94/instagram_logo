## Simple code to draw instagram logo ##

from turtle import* 
hideturtle()
pensize(10) #pen thickness
circle(50) # radius of the circle

up() #Lift the pen of the drawing
goto(-50,-25) #Go to the new location
down() #Put pen down ready to draw

for i in range(4):
    forward(100)
    circle(25,90)

up() #Lift the pen of the drawing
goto(55,95) #Go to the new location
down() #Put pen down ready to draw

circle(5,360)