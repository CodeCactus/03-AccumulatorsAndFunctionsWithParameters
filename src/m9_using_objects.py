"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and LIAM GROOM.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    two_circles()
    circle_and_rectangle(100,200,200,100,300,300)
    lines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window=rg.RoseWindow()
    fill=rg.Circle(rg.Point(200,200),13)
    unfill = rg.Circle(rg.Point(100, 100), 26)
    fill.fill_color=rg.Color(20,200,255)
    unfill.attach_to(window)
    fill.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle(x,y,a,b,a1,b1):
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window=rg.RoseWindow()

    phil=rg.Circle(rg.Point(x,y),13)

    phil.outline_thickness=4

    unphil = rg.Rectangle(rg.Point(a,b), rg.Point(a1,b1))

    phil.fill_color='blue'

    philmid = phil.center
    unphilmid = unphil.get_center()
    unphil.attach_to(window)
    phil.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    print(phil.outline_thickness)
    print(phil.fill_color)
    print(philmid)
    print(philmid.x)
    print(philmid.y)
    print(unphil.outline_thickness)
    print(unphil.fill_color)
    print(unphilmid.x)
    print(unphilmid.y)
def lines():
    window1=rg.RoseWindow()
    thiccboi=rg.Line(rg.Point(100,100),rg.Point(200,200))
    thiccboi.thickness=15
    thinboi = rg.Line(rg.Point(200, 100), rg.Point(100, 200))
    thinboi.attach_to(window1)
    thiccboi.attach_to(window1)
    thiccboimid=thiccboi.get_midpoint()
    window1.render()
    window1.close_on_mouse_click()
    print(thiccboimid)
    print(thiccboimid.x)
    print(thiccboimid.y)
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
