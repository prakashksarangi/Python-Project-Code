from turtle import *
from random import *
import turtle
import time



#changing title of screen
turtle.title("turtle Race game")

turtle.setheading(0)
#changing backgroundcolor
turtle.bgcolor("forestgreen")
#header
penup()
turtle.goto(-60,250)
turtle.write("Turtle Race Game",font=("fruktur",20,"bold"))


#setting the racing field
turtle.penup()
turtle.colormode(255)
turtle.color(255, 153, 51)

turtle.goto(-300,200)
turtle.pendown()
turtle.speed(0)
turtle.begin_fill()
for i in range(2):
    turtle.forward(650)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
turtle.end_fill()


#start line
goto(-260,y=200)
color("white")
turtle.right(90)
pensize(5)
turtle.forward(408)

#race finish line
penup()
goto(280,230)
color("white")
turtle.write("Finish Line",font=20)

turtle.color("black")
penup()
goto(300,200)
pendown()
turtle.right(0)
turtle.shape("square")
turtle.shapesize(0.3)
turtle.speed(0)
for i in range(26):
    turtle.speed(0)
    stamp()
    color("cyan")
    turtle.forward(10)
    color("black")
    stamp()
    turtle.forward(5)



#all racer
# greeen turtle
green_turtle=turtle.Turtle()
green_turtle.speed(0)
green_turtle.shape("turtle")
green_turtle.shapesize(1.2)
green_turtle.color('green')
green_turtle.penup()
green_turtle.goto(-260,y=0)
green_turtle.pendown()

#Red turtle
red_turtle=turtle.Turtle()
red_turtle.speed(0)
red_turtle.shape("turtle")
red_turtle.shapesize(1.2)
red_turtle.color('red')
red_turtle.penup()
red_turtle.goto(-260,180)
red_turtle.pendown()


#blue turtle
blue_turtle=turtle.Turtle()
blue_turtle.speed(0)
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.color('blue')
blue_turtle.penup()
blue_turtle.goto(-260,100)
blue_turtle.pendown()


#pink turtle
perple_turtle=turtle.Turtle()
perple_turtle.speed(0)
perple_turtle.shape("turtle")
perple_turtle.shapesize(1.5)
perple_turtle.color('purple')
perple_turtle.penup()
perple_turtle.goto(-260,-180)
perple_turtle.pendown()


#black turtle
black_turtle=turtle.Turtle()
black_turtle.speed(0)
black_turtle.shape("turtle")
black_turtle.shapesize(1.5)
black_turtle.color('black')
black_turtle.penup()
black_turtle.goto(-260,-100)
black_turtle.pendown()


#pause
time.sleep(1)

#moving all turtle
for i in range(100):
    green_turtle.forward(randint(1,10))
    red_turtle.forward(randint(1,10))
    blue_turtle.forward(randint(1,10))
    perple_turtle.forward(randint(1,10))
    black_turtle.forward(randint(1,10))






turtle.exitonclick()