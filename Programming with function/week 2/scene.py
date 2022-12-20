# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_gird(canvas, scene_width, scene_height, 50)
    draw_sky(canvas, scene_width, scene_height)
    draw_cloud(canvas, 150, 390, 200, 100, "azure2", 'seashell2' )
    draw_ground(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 300, 400)
    draw_pine_tree(canvas, 400, 360)
    draw_pine_tree(canvas, 700, 400)
    draw_pine_tree(canvas, 50, 400)
    draw_flower(canvas, 800, 100)
   

    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_gird(canvas, width, height, interval, color ='blue' ):
    label_x = 15
    for x in range(interval, width, interval):
       draw_line(canvas, x, 0, x, height, fill= color)
       draw_text(canvas, x, label_x, f'{x}', fill=color)
    
    label_y = 15
    for y in range(interval, height, interval):
       draw_line(canvas, 0, y, width, y, fill= color)
       draw_text(canvas,  label_y, y, f'{y}', fill=color)
       
    
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0,  scene_height / 3, scene_width, scene_height, width=0, fill='deepSkyBlue2',) 

def draw_ground(canvas, scene_with, scene_height):
    draw_rectangle(canvas, 0, 0, scene_with, scene_height / 3, width=0, fill='burlywood3')

def draw_cloud(canvas, x0, y0,  width, height, color, border_color ):
    draw_oval(canvas, x0, y0, x0 + width, y0 + height, fill=color, outline=border_color)
    draw_oval(canvas, x0+ 100, y0-80, + width/2, y0 -50 + height/3,  fill=color, outline=border_color)
    draw_oval(canvas, x0+ 100, y0-100, + width/3, y0 -50 + height/2,  fill=color, outline=border_color)
    # diameter = 15
    # space = 5
    
def draw_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 60
    skirt_right = peak_x + 60
    skirt_bottom = peak_y - 250
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 300

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom, trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen" )

def draw_flower(canvas, scene_height, scene_width):
    # diameter = 15
    # space = 5
    # interval = diameter + space

    # # Draw a rectangular series of circles.
    # y = 100
    # for row in range(6):
    #     x = 100
    #     for cell in range(20):
    #         draw_oval(canvas, x, y,
    #                 x + diameter, y + diameter, fill="orange")
    #         x += interval
    #     y += interval
    half_height = round(scene_width )
    min_diam = 15
    max_diam = 30

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(60):
        x = random.randint(0, scene_height - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="green3")

    


    # half_height = round(scene_height)
    # half_width = (scene_width)
    # min_diam = 300
    # max_diam = 350

    # Draw 100 circles, each with
    # a random location and diameter.
  #  for i in range(100):
  #      x = random.randint(150,  scene_height - max_diam)
  #      y = random.randint(250,  half_height)
  #      diameter = random.randint(min_diam, max_diam)
  #      draw_oval(canvas, x, y, x + diameter, y + diameter, fill="azure2")


# Call the main function so that
# this program will start executing.
main()