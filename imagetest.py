# test program to draw images

from cmu_graphics import *
from worldsetup import *
from PIL import Image as Img
from perlin import *

def onAppStart(app):
    app.world = sample_gradient(scale)
    app.rows, app.cols = worldrows, worldcols
    app.img = Img.fromarray(app.world)
    app.img = app.img.convert('RGB')
    app.url = 'test-png.png'
    app.img.save(app.url, format='PNG')    
    app.step = 0
    app.stepsPerSecond = 1

def redrawAll(app):
    drawImage('test-png.png', 0, 0, width = 400, height = 300)
    drawLabel(f"step: {app.step}", app.width // 2, app.height // 2, size = 20, fill = 'black')

def onStep(app):
    app.img.close()  # close the previous image to avoid memory leaks
    app.step += 1
    if app.step % 2 == 0:
        app.world = sample_gradient(scale)
        app.img = Img.fromarray(app.world)
        app.img = app.img.convert('RGB')
        app.img.save('test-png.png', format='PNG')
    else:
        app.img = Img.fromarray(np.zeros((app.rows, app.cols, 3), dtype=np.uint8))
        app.img = app.img.convert('RGB')
        app.img.save('test-png.png', format='PNG')


runApp(width = 600, height = 600)