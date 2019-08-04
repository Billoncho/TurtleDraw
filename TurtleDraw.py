# TurtleDraw.py
# Billy Ridgeway
# Creates a program to draw lines on the screen by using screen clicks.

import turtle                   # Imports the turtle library.
t = turtle.Pen()                # Creates a pen named t.
t.speed(0)                      # Sets the pen's speed to fast.
turtle.onscreenclick(t.setpos)  # When the screen is clicked it
                                # will call the function t.setpos
                                # and set the pen to the x y coordinates
                                # where the screen was clicked.
