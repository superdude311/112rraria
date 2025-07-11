#test file for 112rraria
#tests drawing world array to screen

import numpy as np
from cmu_graphics import *
from perlin import *
from worldsetup import *

def onAppStart(app):
    app.rows, app.cols = worldrows, worldcols #vars from worldsetup
    app.setMaxShapeCount(app.rows * app.cols)
    app.testarray  = create_gradient()
    print(app.testarray)

def redrawAll(app):
    for i in range(app.rows):
        for j in range(app.cols):
            
            drawRect(i * 20, j * 20, 20, 20, fill = rgb(int(app.testarray[i][j]), int(app.testarray[i][j]), int(app.testarray[i][j])))

runApp(width = 400, height = 200)
#draw black and white array to screen with x,y being testarray[y][x]