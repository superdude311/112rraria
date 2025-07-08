#test file for 112rraria
#tests drawing world array to screen

import numpy as np
from cmu_graphics import *
from perlin import *

def onAppStart(app):
    app.rows, app.cols = 200, 100
    app.setMaxShapeCount(app.rows * app.cols)
    app.testarray  = create_gradient()
    app.color = rgb(int(app.testarray[i, j]), int(app.testarray[i, j]), int(app.testarray[i, j]))
    print(app.testarray)

def redrawAll(app):
    for i in range(app.rows):
        for j in range(app.cols):
            drawRect(i * 10, j * 10, 10, 10, fill = app.color)

runApp(width = 2000, height = 1000)
#draw black and white array to screen with x,y being testarray[y][x]