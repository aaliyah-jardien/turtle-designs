# PLOTTING USING TURTLE
# IMPORTING THE TURTLE LIBRARY (to make use of turtle methods and functionalitites)
import turtle
from turtle import *

# CREATE A NEW WINDOW (this is the drawing board) - wn or window?
# & CREATE A TURTLE TO CONTROL - skk
window = turtle.Screen()
window.bgcolor("green")
window.title("Turtle Design by Aaliyah")
window.resizable = (0, 0)
skk = turtle.Turtle()
color("white")

# DRAW AROUND USING THE TURTLE METHODS
# NOW TO MOVE THE TURTLE - i'm moving it forward by 100 pixels
skk.forward(100)

# RUN TURTLE
turtle.done()













# import colorsys

# # turtle design
# t = turtle.Turtle()
# s = turtle.Screen()
#
# s.bgcolor("black")
# t.speed(0)
#
# n = 36
# h = 0
#
# for i in range(460):
#     c = colorsys.hsv_to_rgb(h,1,0.9)
#     h += 1/n
#     t.color(c)
#     t.left(145)
#
#     for j in range(5):
#         t.forward(300)
#         t.left(150)
#
