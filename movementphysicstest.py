# player movement physics test
from cmu_graphics import *

def onAppStart(app):
    app.px = app.width // 2
    app.py = app.height // 2
    app.vx = 0
    app.vy = 0
    app.ax = 0.5 # friction (x axis)
    app.grav = -0.5 # gravity
    app.vxcap = 10  # velocity cap (x)
    app.vycap = 15 # velocity cap (y)
    app.lflag = False #press left flag
    app.rflag = False #press right flag

# general notes

# while the player presses left/right, app.px will change by app.vx, which will increase by app.ax until it reaches app.vcap
# while the player stops pressing left/right, app.vx will decrease by app.ax until it reaches 0
# while the player presses up, app.py will change by app.vy, which will decrease by app.ay until it reaches 0, and the player will fall

def onKeyHold(app, keys):
    if ('left' in keys or 'a' in keys) and app.vx <= app.vxcap: # if x under cap and pressing left/a
        app.lflag = True
        app.vx -= app.ax
        if app.vx < -app.vxcap: 
            app.vx = -app.vxcap

    if ('right' in keys or 'd' in keys) and app.vx >= -app.vxcap: # if x over cap and pressing right/d
        app.rflag = True
        app.vx += app.ax
        if app.vx > app.vxcap: # if x over cap
            app.vx = app.vxcap


    # separate if statement so that the player can jump while moving left/right
    # if y under cap and on ground (change to a general check), and pressing up/space
    if ('up' in keys or 'space' in keys) and app.vy < app.vycap and app.py >= app.height - 40: 
        app.vy = app.vycap # jump velocity
        if app.vy > app.vycap: # if y over cap
            app.vy = app.vycap 

def onKeyRelease(app, key):
    if key == 'left' or key == 'a':
        app.lflag = False
    if key == 'right' or key == 'd':
        app.rflag = False
    # if key == 'up' or key == 'space':
    #     app.vy = app.vy - 1


def onStep(app):
    app.vy += app.grav  # apply gravity

    if not app.lflag and app.vx < 0: # if not pressing left, and moving left
        app.vx += app.ax # decelerate by friction
    if not app.rflag and app.vx > 0: # if not pressing right, and moving right
        app.vx -= app.ax # decelerate by friction


    if app.vy < -app.vycap: # if y over cap (when falling)
        app.vy = -app.vycap # decelerate by gravity

    if 0 <= app.px + app.vx <= app.width - 40: #should change to be general check for valid points (with a map)
        app.px += app.vx # move left/right

    app.py -= app.vy # move up/down
    
    if app.py >= app.height - 40: # should change to be general check for valid points (with a map)
        app.py = app.height - 40
        app.vy = 0

def redrawAll(app):
    drawRect(app.px, app.py, 20, 40, fill = 'blue')
    drawLabel(f'Position: ({app.px}, {app.py})', app.width // 2, 20, size = 16, fill = 'black')
    drawLabel(f'Velocity: ({app.vx}, {app.vy})', app.width // 2, 40, size = 16, fill = 'black')
    drawLabel(f'Acceleration: ({app.ax}, {app.grav})', app.width // 2, 60, size = 16, fill = 'black')

runApp(width=1200, height=600)