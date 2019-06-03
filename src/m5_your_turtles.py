"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Xiaoze Sun.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  Xiaoze Sun  with your own name.
########################################################################
# Ninja turtle
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(2)
don= rg.SimpleTurtle('turtle')
don.pen = rg.Pen('purple', 5)
don.left(270)
don.forward(200)
leo=rg.SimpleTurtle('turtle')
leo.pen=rg.Pen('blue',5)
leo.left(90)
leo.forward(100)
leo.draw_circle(50)
mikey=rg.SimpleTurtle('turtle')
mikey.pen=rg.Pen('orange',5)
size=150
for k in range(6):
    mikey.draw_circle(size)
    mikey.pen_up()
    mikey.right(45)
    mikey.forward(10)
    mikey.left(45)
    mikey.pen_down()
    size = size - 12
raph=rg.SimpleTurtle('turtle')
raph.pen=rg.Pen('red',5)
size=250
for k in range(6):
    raph.left(135)
    raph.draw_square(size)
    raph.pen_up()
    raph.right(45)
    raph.forward(10)
    raph.left(45)
    raph.pen_down()
    size = size - 12
window.close_on_mouse_click()
rg.SimpleTurtle().backward(100)
########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

