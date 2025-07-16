# this code draws the starting screen of the game

# draw background image
# draw title text
# create buttons (using another function maybe?)
# buttons should be clickable
# 5 buttons: new game, load game, exit, options, credits

from cmu_graphics import *

def onAppStart(app):
    app.sbx = 200
    app.sby = 250 #start btn coords
    app.sbw = 75
    app.sbh = 32.5 #start btn width/height
    app.cbx = app.sbx - 100#credits btn coords
    app.cby = app.sby + 25
    app.cbw = 50
    app.cbh = 25 #credits btn width/height
    app.obx = app.sbx + 100#options btn coords
    app.oby = app.sby + 25
    app.obw = 50
    app.obh = 25 #options btn w/h
    app.ts_tag = True #title screen tag
    app.o_tag = False #opts tag
    app.c_tag = False #creds tag
    app.bbx = 100 #back btn coords


def redrawAll(app):
    if app.ts_tag:
        drawRect(app.sbx, app.sby, app.sbw, app.sbh, fill = 'lightGray', align = 'center')
        drawRect(app.cbx, app.cby, app.cbw, app.cbh, fill = 'lightGray', align = 'center')
        drawRect(app.obx, app.oby, app.obw, app.obh, fill = 'lightGray', align = 'center')
        drawLabel("Start Game", app.sbx, app.sby, align = 'center')
        drawLabel("Credits", app.cbx, app.cby, align = 'center')
        drawLabel("Options", app.obx, app.oby, align = 'center')
    elif app.o_tag:
        drawLabel("Options", 200, 75, size = 36)
        drawRect()
    

def in_button(app, mouseX, mouseY): #returns s, c, o depending on which button is pressed
    if app.sbx <= mouseX <= app.sbx + app.sbw and app.sby <= mouseY <= app.sby + app.sbh:
        return 's'
    elif app.cbx <= mouseX <= app.cbx + app.cbw and app.cby <= mouseY <= app.cby + app.cbh:
        return 'c'
    elif app.obx <= mouseX <= app.obx + app.obw and app.oby <= mouseY <= app.oby + app.obh:
        return 'o'
    

def onMousePress(app, mouseX, mouseY):
    if in_button(app, mouseX, mouseY) == 's':
        pass
    elif in_button(app, mouseX, mouseY) == 'c':
        pass
    elif in_button(app, mouseX, mouseY) == 'o':
        pass
    pass

def onMouseMove(app, mouseX, mouseY):
    if in_button(app, mouseX, mouseY) == 's':
        app.sbw = 75 + 7.5
        app.sbh = 32.5 + 3.25
    elif in_button(app, mouseX, mouseY) == 'c':
        app.cbw = 55
        app.cbh = 27.5
    elif in_button(app, mouseX, mouseY) == 'o':
        app.obw = 55
        app.obh = 27.5
    else:
        app.sbw = 75
        app.cbw, app.obw = 50, 50
        app.sbh = 32.5
        app.cbh, app.obh = 25, 25

runApp()