import turtle as t

# Setup
t.setup(500, 500)                   # make window set size
win = t.Screen()                    # refer to the screen as win
win.title( "Mouse Clicks!")         # change the window title
win.bgcolor( "black")               # change background color

# Create 2 turtles for fun
crush = t.Turtle()                  # Crush from Finding Nemo!
crush.color( "blue")                # make crush blue
crush.setx( 10)                     # he starts at position 10, 0

squirt = t.Turtle()                 # Squirt from Finding Nemo!
squirt.color( "green")              # make squirt green


# This is for when the crush turtle is clicked!
def crush_handler( x, y):
    win.title( "Crush was clicked! {}:{}".format( x, y))
    crush.goto( 200, 200)
    crush.goto( 10, 200)
    
# This is for when the squirt turtle is clicked!    
def squirt_handler( x, y):
    win.title( "Squirt was clicked! {}:{}".format( x, y))
    squirt.goto( -200, 200)
    squirt.goto( 0, 200)


crush.onclick( crush_handler)
squirt.onclick( squirt_handler)


win.mainloop()
