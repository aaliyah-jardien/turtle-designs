# PYTHON PROGRAM TO DRAW A SQUARE
# USING TURTLE PROGRAMMING
# IMPORTING THE TURTLE MODULE
import turtle
from turtle import *

skk = turtle.Turtle()
color("pink")

# CREATE A WINDOW AND A TURTLE TO DRAW
window = turtle.Screen()
window.bgcolor("aqua")
window.title("Square turtle design by Aaliyah")

# DRAW USING THE TURTLE METHODS
for i in range(4):
    skk.forward(200)
    skk.left(90)

# RUN TURTLE
turtle.done()
