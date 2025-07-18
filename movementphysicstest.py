# player movement physics test
from cmu_graphics import *

def onAppStart(app):
    app.px = app.width // 2
    app.py = app.height - 20
    app.vx = 0
    app.vy = 0
    app.ax = 0.5
    app.ay = -0.5
    app.vxcap = 5  # velocity cap (x)
    app.vycap = 10 # velocity cap (y)

# general notes

# while the player presses left/right, app.px will change by app.vx, which will increase by app.ax until it reaches app.vcap
# while the player stops pressing left/right, app.vx will decrease by app.ax until it reaches 0
# while the player presses up, app.py will change by app.vy, which will decrease by app.ay until it reaches 0, and the player will fall

# def onKeyPress(app, key):
#     if key == 'left':
#         app.vx += app.ax
#     elif key == 'right':
#         app.vx -= app.ax
#     elif key == 'up' and app.vy == 0:  # jump only if on the ground
#         app.vy = app.vycap

def onKeyHold(app, keys):
    if 'left' in keys and app.vx <= app.vxcap:
        app.vx -= app.ax
    elif 'right' in keys and app.vx >= -app.vxcap:
        app.vx += app.ax
    else:
        if app.vx > 0:
            app.vx += app.ax
        elif app.vx < 0:
            app.vx -= app.ax
    # separate if statement so that the player can jump while moving left/right
    if 'up' in keys and app.vy < app.vycap:
        app.vy -= app.ay
    elif app.py < app.height - 20: #if not on ground, fall
        app.vy += app.ay


def onStep(app):
    if abs(app.vx) > app.vxcap:
        app.vx = app.vxcap
    elif abs(app.vy) > app.vycap:
        app.vy = app.vycap
    if app.py <= app.height - 20:
        app.px += app.vx
        app.py -= app.vy

def redrawAll(app):
    drawRect(app.px, app.py, 20, 20, fill = 'blue')
    drawLabel(f'Position: ({app.px}, {app.py})', app.width // 2, 20, size = 16, fill = 'black')
    drawLabel(f'Velocity: ({app.vx}, {app.vy})', app.width // 2, 40, size = 16, fill = 'black')
    drawLabel(f'Acceleration: ({app.ax}, {app.ay})', app.width // 2, 60, size = 16, fill = 'black')

runApp(width=800, height=600)