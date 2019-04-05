

#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 10229825
#    Student name: Levi Breakwell
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *
from random import randint, choice 

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]


#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan


#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#

# Erect buildings as per the provided city plan
def build_city(city_plan):
    #makes new list of site locations for easy use
    site_location = []
    for coordinate in sites:
        site_location.append(coordinate[1])
   #gathers random details and puts them into variables
    for building_details in city_plan:
        site = building_details[0]      
        building_type = building_details[1]
        levels = building_details[2] -1
        global construction
        construction = building_details[3]
        goto (site_location[site - 1])
        if building_type == "A":
            build_a(site,levels)
        elif building_type == "B":
            build_b(site,levels)
        elif building_type == "C" :
            build_c(site,levels)
        else:
            build_d(site,levels)

# draw under construction level
def under_construction():
    pencolor("black")
    width(3)
    pendown()
    setheading(90)
    forward(30)
    #left zigzag
    left(90)
    forward(60)
    right(90)
    forward(45)
    right(90)
    forward(10)
    right(135)
    forward(14)
    left(90)
    forward(14)
    right(90)
    forward(14)
    left(90)
    forward(14)
    setheading(270)
    forward(5)
    #getting to otherside
    setheading(90)
    forward(45)
    right(90)
    forward(110)
    right(90)
    forward(45)
    right(90)
    forward(10)
    #right zigzag
    setheading(45)
    forward(14)
    left(90)
    forward(14)
    right(90)
    forward(14)
    left(90)
    forward(14)
    setheading(90)
    forward(5)
    setheading(270)
    #creating sign
    fillcolor('red')
    begin_fill()
    forward(45)
    right(90)
    forward(100)
    right(90)
    forward(45)
    right(90)
    forward(100)
    end_fill()
    right(90)
    forward(45)
    right(90)
    forward(50)
    penup()
    forward(25)
    right(90)
    forward(25)
    write("UNDER",font=('ariel',16,'normal'))
    setheading(270)
    forward(15)
    right(90)
    forward(20)
    write("CONSTRUCTION", font=('ariel',11,'normal'))
    penup()
    

           
def build_a(site,levels):
    global construction
    build_a_bottom()
    build_a_levels(levels)
    if construction == "X" :
        under_construction()
    else:
        build_a_top()
def build_b(site,levels):
    build_b_bottom()
    build_b_levels(levels)
    if construction == "X" :
        under_construction()
    else:
        build_b_top()
def build_c(site,levels):
    build_c_bottom()
    build_c_levels(levels)
    if construction == "X" :
        under_construction()
    else:
        build_c_top()
def build_d(site,levels):
    build_d_bottom()
    build_d_levels(levels)
    if construction == "X" :
        under_construction()
    else:
        build_d_top()


    
#Function for building the base of building type A
def build_a_bottom():
 #   drawing outlines
 #   goto()
    pencolor("black")
    fillcolor("brown")
    setheading(0)
    begin_fill()
    forward(100)
    left(180)
    width(5)
    pendown()
    circle(-50,extent=90)
    penup()
    left(90)
    forward(100)
    left(90)
    pendown()
    circle(-50,extent=90)
    end_fill()
    penup()
    left(180)
    forward(25)
    #Drawing inner lines
    width(3)
    pendown()
    fillcolor("brown4")
    begin_fill()
    circle(50,extent=90)
    penup()
    right(90)
    forward(50)
    right(90)
    pendown()
    circle(50,extent=90)
    end_fill()
    #Getting to correct position for next movement
    penup()
    forward(25)
    left(180)
    circle(-50,extent=90)
    global position_x
    global position_y
    position_x = xcor()
    position_y = ycor()

#Function to draw branches on left
dot_locationsl=[]
def branch_on_left():       
    width(3)
    penup()
    left(90)
    forward(25)
    left(90)
    pendown()
    fillcolor("brown4")
    begin_fill()
    forward(8)
    setheading(170)
    global num_of_levels
    forward(50 - num_of_levels*5)
    penup()
    setheading(90)
    forward(16)
    pendown()
    setheading(350)
    forward(50 - num_of_levels*5)
    setheading(90)
    forward(15)
    penup()
    right(90)
    forward(50)
    right(90)
    pendown()
    forward(41)
    end_fill()
    #drawing leaves
    penup()
    right(90)
    forward(50)
    right(90)
    forward(8)
    left(80)
    forward(50 - num_of_levels*5)
    pencolor("dark green")
    dot(24)
    setheading(90)
    forward(9)
    dot(24)
    setheading(150)
    global dot_locationsl
    
    for leaves in range (10):
        right(randint(-40,50))
        forward(3)
        position = (xcor(),ycor())
        dot_locationsl.append(position)
    global position_x
    global position_y
    goto(position_x,position_y)
    setheading(90)
dot_locationsr=[]
#function to build branches on right
def branch_on_right():   
    width(3)
    penup()
    left(90)
    forward(75)
    left(90)
    pendown()
    fillcolor("brown4")
    begin_fill()
    forward(8)
    setheading(10)
    global num_of_levels
    forward(50 - num_of_levels*5)
    penup()
    setheading(90)
    forward(16)
    pendown()
    setheading(190)
    forward(50 - num_of_levels*5)
    setheading(90)
    forward(15)
    penup()
    left(90)
    forward(50)
    left(90)
    pendown()
    forward(41)
    end_fill()
#drawing leaves
    penup()
    left(90)
    forward(50)
    left(90)
    forward(8)
    right(80)
    forward(50 - num_of_levels*5)
    pencolor("dark green")
    dot(24)
    setheading(90)
    forward(9)
    dot(24)
    setheading(30)
    global dot_locationsr
    for leaves in range (10):
        left(randint(-40,50))
        forward(3)
        position = (xcor(),ycor())
        dot_locationsr.append(position)
    global position_x
    global position_y
    goto(position_x,position_y)
    setheading(90)

# to build the levels of building a
def build_a_levels(amount_of_levels):
    for Num_of_levels in range(amount_of_levels):
        #drawing outline of tree levels
        global num_of_levels
        global num_of_levels
        num_of_levels = Num_of_levels
        width(5)
        pendown()
        pencolor("black")
        fillcolor("brown")
        begin_fill()
        forward(40)
        #remimbering coordinates to draw next level
        global position_x
        global position_y
        position_x = xcor()
        position_y = ycor()
        
        penup()
        left(90)
        forward(100)
        left(90)
        pendown()
        forward(41)
        end_fill()
        #drawing inner lines and branch on left side
        choose=["L","R"]
        randomside = choice(choose)
        if randomside == "L" :

            branch_on_left()
        else:
            branch_on_right()
    #Draw dots(leaves) on branches
    penup()
    global dot_locationsr
    global dot_locationsl
    if dot_locationsr != []:        
        for dots in dot_locationsr:
            goto(dots)
            dot(24)
        dot_locationsr = []
    if dot_locationsl != []:
        for dots in dot_locationsl:
            goto(dots)
            dot(24)
        dot_locationsl = []
    goto(position_x,position_y)
    setheading(180)
    forward(50)


# to build the top of building a           
def build_a_top():
    setheading(0)
    forward(50)
    pencolor('darkgreen')
    penup()
    dot(70)
    setheading(180)
    forward(50)
    dot(70)
    forward(50)
    dot(70)
    setheading(115)
    fillcolor("darkgreen")
    begin_fill()
    for dotss in range (10):
        circle(-50,extent=22)
        dot(randint(30,59))
    end_fill()
    
# to build the base of building b

def build_b_bottom():
    width(4)
    setheading(0)
    pencolor('black')
    fillcolor("tan")
    begin_fill()
    pendown()
    forward(120)
    left(90)
    forward(60)
    left(90)
    forward(240)
    left(90)
    forward(60)
    left(90)
    forward(120)
    end_fill()
    forward(120)
    left(90)
    forward(60)

#defining a triangle to use in building b levels
def triangle(direction):
    fillcolor("tan")
    if direction == 0 :
        begin_fill()
        setheading(180)
        forward(24)
        left(120)
        forward(24)
        left(120)
        forward(24)
        end_fill()
        left(120)
        forward(24)
        left(120)
        forward(24)
        setheading(180)
        
    else:
        begin_fill()
        setheading(180)
        forward(24)
        left(-120)
        forward(24)
        left(-120)
        forward(24)
        end_fill()
        left(-120)
        forward(24)
        left(-120)
        forward(24)
        setheading(180)
        

# to build building b levels

def build_b_levels(levels):
    num_levels = levels
    offput = 10 - levels
    setheading(180)
    forward(24*offput/2)
    
    for each_level in range (levels):
        for triangles in range (num_levels - 1):
            triangle(1)
            triangle(0)
        triangle(1)                      
        setheading(0)
        forward(24 * (num_levels-1))
        num_levels = num_levels -1

#to build building b top
def star():
    pendown()
    forward(30)
    penup()
    forward(27)
    pendown()
    forward(30)
    left(144)
    pendown()
    forward(30)
    penup()
    forward(27)
    pendown()
    forward(30)
    left(144)
    pendown()
    forward(30)
    penup()
    forward(27)
    pendown()
    forward(30)
    left(144)
    pendown()
    forward(30)
    penup()
    forward(27)
    pendown()
    forward(30)
    left(144)
    pendown()
    forward(30)
    penup()
    forward(27)
    pendown()
    forward(30)

def build_b_top():
    setheading(0)
    fillcolor('yellow')
    begin_fill()
    circle(45)
    end_fill()
    circle(45, extent = 180)
    fillcolor('tan')
    begin_fill()
    setheading(252)
    star()
    setheading(270)
    end_fill()
    penup()
    forward(45)
    pencolor('tan')
    dot(34)
    penup()

# building c bottom
def build_c_bottom():
    penup()
    setheading(0)
    pencolor('black')
    fillcolor('grey')
    begin_fill()
    forward(85)
    left(90)
    forward(35)
    left(90)
    forward(170)
    left(90)
    forward(35)
    left(90)
    forward(85)
    end_fill()
    fillcolor('darkgrey')
    begin_fill()
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(200)
    left(90)
    forward(20)
    left(90)
    forward(100)
    end_fill()
    fillcolor('black')
    begin_fill()
    forward(115)
    left(90)
    forward(5)
    left(90)
    forward(230)
    left(90)
    forward(5)
    left(90)
    forward(115)
    end_fill()

#build building c levels
def window() :
    width(1)
    pencolor('black')
    fillcolor('skyblue')
    pendown()   
    begin_fill()   
    forward(7)
    left(90)
    forward(11)
    left(90)
    forward(7)
    left(90)
    forward(11)
    location= (xcor(),ycor())
    end_fill()
    left(150)
    penup()
    forward(3)
    pencolor('white')
    pendown()
    forward(9)
    penup()
    goto(location)
    setheading(180)


def build_c_levels(levels) :
    num_levels = levels
    width(1)
    setheading(90)
    penup()
    forward(35)
    fillcolor('grey')
    
    for floors in range (levels):
        pendown()
        pencolor('black')
        setheading(0)
        fillcolor('grey')
        begin_fill()
        forward(num_levels * 8 )
        left(90)
        forward(50)
        location = (xcor(),ycor())
        left(90)
        forward(num_levels * 16)
        left(90)
        forward(50)
        left(90)
        forward(num_levels * 8)
        end_fill()
        setheading(0)
        penup()
        forward(num_levels * 7 - 4)
        left(90)
        forward(30)
        left(90)
        for windows in range (num_levels):
            window()
            forward(15)
        goto(location)
        setheading(180)
        forward(num_levels*8)
        num_levels = num_levels - 1
        
#draw building c top
def build_c_top():
    width(4)
    pendown()
    setheading(90)
    pencolor('black')
    forward(20)
    pencolor('red')
    dot(7)
    penup()

#draw building d bottom

def build_d_bottom():
    pencolor('black')
    penup()
    width(4)
    setheading(0)
    fillcolor('white')
    begin_fill()
    forward(50)
    pendown()
    setheading(90)
    circle(50, extent = 180)
    setheading(0)
    penup()
    forward(50)
    end_fill()

#draw building d levels

def build_d_levels(levels):
    setheading(90)
    forward(40)
    setheading(0)
    pendown()
    for balls in range (levels):
        pendown()
        begin_fill()
        width(4)
        circle(25)
        location = (xcor(),ycor())
        end_fill()
        #drawing right arm
        circle(25,extent=90)
        pencolor('brown')
        width(1)
        setheading(30)
        forward(30)
        left(180)
        forward(10)
        left(150)
        forward(9)
        left(180)
        forward(9)
        right(90)
        forward(9)
        penup()
        #drawing left arm
        goto(location)
        setheading(180)
        circle(-25,extent=90)
        setheading(150)
        pendown()
        forward(30)
        left(180)
        forward(10)
        left(150)
        forward(9)
        left(180)
        forward(9)
        right(90)
        forward(9)
        penup()
        goto(location)
        penup()
        pencolor('black')
        setheading(90)
        forward(16)
        dot(8)
        forward(16)
        dot(8)
        goto(location)
        setheading(90)
        forward(40)
        setheading(0)


def build_d_top():
    pendown()
    begin_fill()
    circle(40)
    end_fill()
    setheading(90)
    penup()
    forward(35)
    pencolor('orange')
    dot(8)
    pencolor('black')
    left(45)
    forward(14)
    dot(15)
    left(180)
    forward(14)
    left(90)
    forward(14)
    dot(15)
    left(180)
    forward(14)
    setheading(180)
    forward(20)
    setheading(280)
    for mouth in range (11):
        circle(20,extent=13)
        dot(5)
    setheading(90)
    width(6)
    forward(40)
    setheading(173)
    pendown()
    forward(35)
    left(180)
    forward(11)
    setheading(86)
    fillcolor('black')
    begin_fill()
    forward(30)
    right(90)
    forward(12)
    right(90)
    forward(30)
    end_fill()
    penup()
    forward(22)
    setheading(45)
    pendown()
    forward(25)
    left(180)
    forward(25)
    setheading(180)
    penup()
    forward(10)
    pendown()
    setheading(135)
    forward(25)
    penup()

    
    
    





#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('normal')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Centipede Snowman Army Attacks City with Pyramids")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
#build_city(fixed_plan_9) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment



# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()


#
#--------------------------------------------------------------------#

