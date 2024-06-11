# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name: HIMANSHU SHARMA
# PRA Section: PRA0101


################################################
# Part 1 - Finding Errors and Debugging
################################################

# provide access to the Turtle module
#import turtle

# bring the turtle to life and call it alex 
#alex = turtle.Turtle()

# tell alex where to go in order to draw a SQUARE

#alex.down()          # make alex lower its tail
#alex.setheading(90)  # make alex face north
#alex.forward(100)   # let it run 100 steps 
#alex.left(90)         # turn 90 degrees to the left
#alex.orward(100)
#alex.left(90)
#ale.forward(100)
#alex.left(45)
#alex.forward(100)
#alex.up()           # make alex lift up its tail

#turtle.done()        # close turtle when done

################################################
# Part 2 - Draw A House
################################################
# modify the above code to tell alex to draw a house





################################################
# Part 3 - Draw Out Your Name
################################################
# tell alex where to go in order to draw your initials

#Starting Turtle
import turtle
#Calling turtle by name "alex"
alex = turtle.Turtle()

#Writing letter "H"
alex.down()
alex.setheading(90)
alex.forward(300)
alex.setheading(270)
alex.forward(150)
alex.setheading(0)
alex.forward(150)
alex.setheading(90)
alex.forward(150)
alex.setheading(270)
alex.forward(300)

#Lifting turtle up and taking it to starting point of "S"
alex.up()
alex.goto(400,225)
alex.setheading(90)

#Writing letter "S"

alex.down()
alex.circle(75,270)
alex.circle(-75,270)



#Finishing up turtle command

turtle.done()
