"""
setup and draw

The code inside the draw() function runs continuously from top to bottom until the program is stopped.
The code in setup() is run once when the program starts.
"""

from mewnala import (
    background,
    line,
    run,
    size,
    stroke,
)

y: int = 180


def setup():
    """
    The statements in the setup() function
    execute once when the program begins.
    """
    size(640, 360)  # Size should be the first statement
    stroke(255)  # Set line drawing color to white


def draw():
    """
    The statements in draw() are executed until the
    program is stopped. Each statement is executed in
    sequence and after the last line is read, the first
    line is executed again.
    """
    global y

    background(0)  # Clear the screen with a black background
    line(0, y, width, y)

    y = y - 1

    if y < 0:
        y = height


run()
