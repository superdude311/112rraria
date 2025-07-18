# 112rraria
# a 15-112 Term Project, created by Matthew Kibarian
# This project is a 2D game inspired by the classic game Terraria
# It features a procedurally generated world, player character, and various game mechanics
# including mining, building, and combat (maybe)

from cmu_graphics import *
from worldsetup import *
from worldgen import *


# initialize variables n things 
def onAppStart(app):
    init_titlescreen(app) #initialize titlescreen variables

def init_world(app):
    app.world = []

def init_titlescreen(app): # put this in a diff function to avoid confusion with variables used for other things
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
    app.bbx = 50 #back btn coords
    app.bby = 50
    app.bbw = 50
    app.bbh = 25 #back btn width/height

##########################################################
# initialize game                                        #   
# generate world, show some kind of loading indicator    #
##########################################################

def create_world(app):
    app.world = worldgen()

def draw_loading(app):
    drawRect(0, 0, app.width, app.height, fill = 'black')
    drawLabel("Loading...", app.width / 2, app.height / 2, size = 36, fill = 'white')


###################
# run titlescreen #
###################

def draw_titlescreen(app):
    # draws the title screen with buttons for start, credits, and options, dpending on which tag is active
    if app.ts_tag:
        drawRect(app.sbx, app.sby, app.sbw, app.sbh, fill = 'lightGray', align = 'center')
        drawRect(app.cbx, app.cby, app.cbw, app.cbh, fill = 'lightGray', align = 'center')
        drawRect(app.obx, app.oby, app.obw, app.obh, fill = 'lightGray', align = 'center')
        drawLabel("Start Game", app.sbx, app.sby, align = 'center')
        drawLabel("Credits", app.cbx, app.cby, align = 'center')
        drawLabel("Options", app.obx, app.oby, align = 'center')
    elif app.o_tag:
        drawLabel("Options", 200, 75, size = 36)
        drawRect(app.bbx, app.bby, app.bbw, app.bbh, fill = 'lightGray', align = 'center')
        drawLabel("Back", app.bbx, app.bby, align = 'center')
    elif app.c_tag:
        drawLabel("Credits", 200, 75, size = 36)
        drawRect(app.bbx, app.bby, app.bbw, app.bbh, fill = 'lightGray', align = 'center')
        drawLabel("Back", app.bbx, app.bby, align = 'center')

def in_ts_button(app, mouseX, mouseY): #returns s, c, o depending on which button is pressed
    if app.sbx <= mouseX <= app.sbx + app.sbw and app.sby <= mouseY <= app.sby + app.sbh:
        return 's'
    elif app.cbx <= mouseX <= app.cbx + app.cbw and app.cby <= mouseY <= app.cby + app.cbh:
        return 'c'
    elif app.obx <= mouseX <= app.obx + app.obw and app.oby <= mouseY <= app.oby + app.obh:
        return 'o'
    elif app.bbx <= mouseX <= app.bbx + app.bbw and app.bby <= mouseY <= app.bby + app.bbh:
        return 'b'

def ts_button_press(app, mouseX, mouseY):
    if in_ts_button(app, mouseX, mouseY) == 's':
        gamestate = 'game'
    elif in_ts_button(app, mouseX, mouseY) == 'c':
        app.c_tag = True
        app.ts_tag = False
    elif in_ts_button(app, mouseX, mouseY) == 'o':
        app.o_tag = True
        app.ts_tag = False
    elif in_ts_button(app, mouseX, mouseY) == 'b':
        app.o_tag = False
        app.c_tag = False
        app.ts_tag = True

def ts_button_bounce(app, mouseX, mouseY):
    if in_ts_button(app, mouseX, mouseY) == 's':
        app.sbw = 75 + 7.5
        app.sbh = 32.5 + 3.25
    elif in_ts_button(app, mouseX, mouseY) == 'c':
        app.cbw = 55
        app.cbh = 27.5
    elif in_ts_button(app, mouseX, mouseY) == 'o':
        app.obw = 55
        app.obh = 27.5
    elif in_ts_button(app, mouseX, mouseY) == 'b':
        app.bbw = 55
        app.bbh = 27.5
    else:
        app.sbw = 75
        app.cbw, app.obw = 50, 50
        app.sbh = 32.5
        app.cbh, app.obh = 25, 25


#############################################################
# gameloop -- calculated every frame, updates game state    #
# update world state, update player state, update inventory #
#############################################################

# probably can just call a function from a different file?

######################################
# general MVC functions for the game #
######################################

def redrawAll(app):
    if gamestate == 'worldgen':
        pass
    elif gamestate == 'title':
        draw_titlescreen(app)
    elif gamestate == 'game':
        pass

def onMousePress(app, mouseX, mouseY):
    if gamestate == 'title':
        ts_button_press(app, mouseX, mouseY)
    elif gamestate == 'worldgen':
        pass
    elif gamestate == 'game':
        pass

def onMouseMove(app, mouseX, mouseY):
    if gamestate == 'title':
        ts_button_bounce(app, mouseX, mouseY)
    elif gamestate == 'worldgen':
        pass
    elif gamestate == 'game':
        pass

runApp(width = 1200, height = 800, title = '112rraria')