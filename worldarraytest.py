#test file for 112rraria
#tests drawing world array to screen

import numpy as np
from cmu_graphics import *
from perlin import *
from worldsetup import *

def onAppStart(app):
    app.rows, app.cols = worldrows, worldcols #vars from worldsetup
    app.setMaxShapeCount(app.rows * app.cols)
    app.testarray  = sample_gradient(scale)
    for i in range(app.rows):
        for j in range(app.cols):
            app.testarray[i][j] = np.interp(app.testarray[i][j], (-1, 1), (0, 255)) #normalize values to 0-255 for drawing

def redrawAll(app):
    for i in range(app.rows):
        for j in range(app.cols):
            
            drawRect(i * 20, j * 20, 20, 20, fill = rgb(int(app.testarray[i][j]), int(app.testarray[i][j]), int(app.testarray[i][j])))

runApp(width = 1200, height = 1000)
#draw black and white array to screen with x,y being testarray[y][x]