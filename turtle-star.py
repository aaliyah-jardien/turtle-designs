# PYTHON PROGRAM TO DRAW A STAR
# IMPORTING THE TURTLE MODULE
import turtle
from turtle import *

#  CREATE A WINDOW
window = turtle.Screen()
window.bgcolor("blue")
window.title("Turtle star design by Aaliyah")

# COLOR OF MY PEN
color('white')
fillcolor("yellow")

# CREATE TURTLE TO DRAW A STAR
star = turtle.Turtle()

# DRAW A STAR
# USING TURTLE METHODS
star.right(65)
star.forward(100)

#  starts with zero, then, 1, 2, 3, 4 (5 points in total)
for i in range(4):
    star.right(144)
    star.forward(100)

# RUN TURTLE
turtle.done()

# HOSH
