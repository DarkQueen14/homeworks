from turtle import*

#we wannt to paint house 
#steo 1: draw a square 
speed(30)
width(7)
color("purple")

forward(200)
left(90)


forward(200)
left(90)



forward(200)
left(90)



forward(200)
left(90)

#end of square 
#draw a door 

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)  #height of the door 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200 ,200)
pendown()

color("red")
begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draew windows

left(30)
color("purple")
forward(50)
begin_fill()
color("brown")
left(90)
forward(50)
left(270)
forward(50)
left(270)
forward(50)
end_fill()

penup()
goto(200, 200)
pendown()

left(90)
color("purple")
forward(50)
begin_fill()
color("brown")
left(270)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()







exitonclick()
