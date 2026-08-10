from mewnala import (
    background,
    ellipse,
    window_resizable,
    run,
    size,
)


def setup():
    # TODO:
    #   Renderer type is missing, revisit
    #   https://github.com/processing/processing-examples-mewnala/issues/290#issuecomment-5243157971
    size(400, 400)
    window_resizable(True)


def draw():
    background(255, 0, 0)
    ellipse(width / 2, height / 2, 100, 50)


run()
