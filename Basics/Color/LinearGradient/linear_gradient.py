"""
Simple Linear Gradient

The lerpColor() function is useful for interpolating between two colors.
"""
from mewnala import (
    Color,
    size,
    no_fill,
    stroke,
    line,
    run,
    no_loop,
)

# Constants
Y_AXIS: int = 1
X_AXIS: int = 2

# color b1, b2, c1, c2

def setup():
    size(640, 360)

    # Define colors
    # FIXME:
    #   Defining these in a function doesn't make them accessible in outer scope,
    #   which causes linting issues with IDEs even when libprocessing provides access to the variables.
    b1: Color = Color(255)
    b2: Color = Color(0)
    c1: Color = Color(204, 102, 0)
    c2: Color = Color(0, 102, 153)

    no_loop()

def draw():
    # Background
    set_gradient(0, 0, width / 2, height, b1, b2, X_AXIS);
    set_gradient(width / 2, 0, width / 2, height, b2, b1, X_AXIS)

    # Foreground
    set_gradient(50, 90, 540, 80, c1, c2, Y_AXIS)
    set_gradient(50, 190, 540, 80, c2, c1, X_AXIS)


def set_gradient(x: int, y: int, w: float, h, c1: Color, c2: Color, axis: int):
    no_fill()

    # Top to bottom gradient
    if axis == Y_AXIS:
        for i in range(y, y + h):
            inter = map(i, y, y+h, 0, 1);
            c: Color = lerp_color(c1, c2, inter)
            stroke(c);
            line(x, i, x+w, i)

    # Left to right gradient
    elif axis == X_AXIS:
        for i in range(x, x + w):
            inter: float = map(i, x, x+w, 0, 1)
            c: Color = lerp_color(c1, c2, inter)
            stroke(c);
            line(i, y, i, y+h);


run()
