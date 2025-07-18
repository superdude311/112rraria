#test file for 112rraria
#tests drawing world array to screen

import numpy as np
from cmu_graphics import *
from perlin import *
from worldsetup import *

def onAppStart(app):
    app.square_size = 10 #size of each square in the grid
    app.rows, app.cols = worldrows, worldcols #vars from worldsetup
    app.setMaxShapeCount(app.rows * app.cols)
    app.testarray  = sample_gradient(scale)
    for i in range(app.rows):
        for j in range(app.cols):
            if app.testarray[i][j] < 115: #air threshold
                app.testarray[i][j] = 0
            elif app.testarray[i][j] > 130: #stone threshold
                app.testarray[i][j] = 255

def redrawAll(app):
    for i in range(app.rows):
        for j in range(app.cols):
            if app.testarray[i][j] != 255:
                drawRect(i * app.square_size, j * app.square_size, app.square_size, app.square_size, fill = rgb(0, int(app.testarray[i][j]), 0))
            else:
                drawRect(i * app.square_size, j * app.square_size, app.square_size, app.square_size, fill = rgb(160, 160, 160))

runApp(width = 2000, height = 1500)
#draw black and white array to screen with x,y being testarray[y][x]