#test file for 112rraria
#tests drawing world array to screen

import numpy as np
from cmu_graphics import *
from perlin import *
from worldsetup import *
from worldgen import *
import copy

def onAppStart(app):
    app.square_size = 3 #size of each square in the grid
    app.rows, app.cols = worldrows, worldcols #vars from worldsetup
    app.setMaxShapeCount(app.rows * app.cols * 2)
    app.testarray  = worldgen()


def redrawAll(app):
    # draw map border
    drawRect(90, 0, 10, app.height, fill = None, border = 'black', borderWidth = 1)
    drawRect(100 + app.rows * app.square_size, 0, 10, app.height, fill = None, border = 'black', borderWidth = 1)

    # draw world array to screen
    for i in range(app.rows):
        for j in range(app.cols):
            if app.testarray[i][j] != 0:
                if app.testarray[i][j] == 1: #grass
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(0, 160, 0))
                elif app.testarray[i][j] == 2: #dirt
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(160, 80, 0))
                elif app.testarray[i][j] == 4: #barrier
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(0, 0, 0))
                elif app.testarray[i][j] == 10: #copper
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(184, 115, 51))
                elif app.testarray[i][j] == 11: #tin
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(211, 212, 213))
                elif app.testarray[i][j] == 12: #iron
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(78, 79, 85))
                elif app.testarray[i][j] == 13: #gold
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(231, 191, 4))
                elif app.testarray[i][j] == 14: #silver
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(230, 230, 230))
                elif app.testarray[i][j] == 15: #lead
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(46, 44, 148))
                elif app.testarray[i][j] == 16: #palladium
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(196, 26, 26))
                elif app.testarray[i][j] == 17: #mithril
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(28, 252, 159))
                elif app.testarray[i][j] == 18: #platinum
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(28, 230, 252))
                else:
                    drawRect(100 + i * app.square_size, 100 + j * app.square_size, app.square_size, app.square_size, fill = rgb(160, 160, 160))

runApp(width = 1200, height = 800)
#draw black and white array to screen with x,y being testarray[y][x]