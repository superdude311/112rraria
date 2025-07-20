#simple image test

from PIL import Image as Img
import numpy as np
from cmu_graphics import *

def onAppStart(app):
    app.rows, app.cols = 100, 100
    app.img = Img.fromarray(np.zeros((app.rows, app.cols, 3), dtype=np.uint8))
    app.img = app.img.convert('RGB')
    app.img.save('test-png.png', format='PNG')
    app.step = 0
    app.stepsPerSecond = 1

def onStep(app):
    app.step += 1
    if app.step % 2 == 0:
        print("a")
        app.img = Img.fromarray(np.zeros((app.rows, app.cols, 3), dtype=np.uint8))
        app.img = app.img.convert('RGB')
        app.img.save('test-png.png', format='PNG')
    else:
        print("b")
        app.img = Img.fromarray(np.full((app.rows, app.cols, 3), 255, dtype=np.uint8))
        app.img = app.img.convert('RGB')
        app.img.save('test-png.png', format='PNG')  

def redrawAll(app):
    drawImage('test-png.png', app.width // 2, app.height // 2, width=app.cols, height=app.rows, align='center')
    drawLabel("Image Test", app.width // 2, 50, size=24, fill='black')
    drawLabel(f"Step: {app.step}", app.width // 2, app.height - 50, size=16, fill='black')

runApp(width=800, height=600)