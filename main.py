# 112rraria
# a 15-112 Term Project, created by Matthew Kibarian
# This project is a 2D game inspired by the classic game Terraria
# It features a procedurally generated world, player character, and various game mechanics
# including mining, building, and combat (maybe)

# titlescreen logo generated with Terraria Logo Maker: https://terraria-logo-maker.darthmorf.co.uk/
# titlescreen background image created by MiltVala: https://forums.terraria.org/index.php?threads/terraria-desktop-wallpapers.12644/


from cmu_graphics import *
from worldsetup import *
from worldgen import *


# initialize variables n things 
def onAppStart(app):
    app.setMaxShapeCount(20000)
    app.step = 0
    app.gamestate = gamestate
    app.stepsPerSecond = 60
    init_titlescreen(app) #initialize titlescreen variables
    init_world(app) #initialize world variables
    init_gamevars(app) #initialize game variables
    app.tile_dict = {0:(255, 255, 255), 1:(0, 160, 0), 2:(160, 80, 0), 3:(160, 160, 160), 4:(0, 0, 0), 10:(184, 115, 51),
                     11:(211, 212, 213), 12:(78, 79, 85), 13:(231, 191, 4), 14:(230, 230, 230), 15:(46, 44, 148), 16:(196, 26, 26),
                     17:(28, 252, 159), 18:(28, 230, 252)}

def init_world(app):
    app.stepsPerSecond = 1
    create_world(app)

def init_titlescreen(app): # put this in a diff function to avoid confusion with variables used for other things
    app.stepsPerSecond = 30
    app.sbx = app.width // 2
    app.sby = app.height // 2 #start btn coords
    app.sbw = 150
    app.sbh = 75 #start btn width/height
    app.cbx = app.sbx - 300 #credits btn coords
    app.cby = app.sby + 100
    app.cbw = 100
    app.cbh = 50 #credits btn width/height
    app.obx = app.sbx + 300 #options btn coords
    app.oby = app.sby + 100
    app.obw = 100
    app.obh = 50 #options btn w/h
    app.ts_tag = True #title screen tag
    app.o_tag = False #opts tag
    app.c_tag = False #creds tag
    app.bbx = 50 #back btn coords
    app.bby = 50
    app.bbw = 50
    app.bbh = 25 #back btn width/height
    app.logo = 'custom-terraria-logo.png' #titlescreen logo
    app.titlescreen_image = 'ts-bg-image.png' #titlescreen image
    app.credits_img = 'credits-bg-img.png' #credits image
    app.options_img = 'opt-bg-img.png' #options image

def init_gamevars(app):
    app.stepsPerSecond = 60
    app.px = app.width // 2 #player x position
    app.py = 300 #player y position
    app.vx = 0 #player x velocity
    app.vy = 0 #player y velocity
    app.ax = 0.5 #friction (x axis)
    app.grav = -0.5 #gravity
    app.vxcap = 10  #velocity cap (x)
    app.vycap = 15 #velocity cap (y)
    app.lflag = False #press left flag
    app.rflag = False #press right flag
    app.pw = 20
    app.ph = 40 #player width/height
    app.camx, app.camy = app.px // tilesize, app.py // tilesize

##########################################################
# initialize game                                        #   
# generate world, show some kind of loading indicator    #
##########################################################

def create_world(app):
    app.world = worldgen()
    app.gamestate = 'title'

###################
# run titlescreen #
###################

def draw_titlescreen(app):
    # draws the title screen with buttons for start, credits, and options, dpending on which tag is active
    if app.ts_tag:
        drawImage(app.titlescreen_image, app.width // 2, app.height // 2, width = 1200, height = 800, align = 'center', opacity = 85)
        drawRect(app.sbx, app.sby, app.sbw, app.sbh, fill = 'lightGray', align = 'center')
        drawRect(app.cbx, app.cby, app.cbw, app.cbh, fill = 'lightGray', align = 'center')
        drawRect(app.obx, app.oby, app.obw, app.obh, fill = 'lightGray', align = 'center')
        drawImage(app.logo, app.width // 2, 150, width = 578, height = 190, align = 'center') #width and height are from the original image
        drawLabel("Start Game", app.sbx, app.sby, align = 'center', size = 24)
        drawLabel("Credits", app.cbx, app.cby, align = 'center', size = 18)
        drawLabel("Options", app.obx, app.oby - 10, align = 'center', size = 18)
        drawLabel("How to Play", app.obx, app.oby + 10, align = 'center')
    elif app.o_tag:
        drawImage(app.options_img, app.width // 2, app.height // 2, width = 1200, height = 800, align = 'center', opacity = 85)
        drawLabel("Options (and how to play)", app.width / 2, 75, size = 36)
        drawLabel("Press the up arrow or space to jump", app.width // 2, 125, size = 24)
        drawLabel("Press left/right arrow or a/d to move", app.width // 2, 150, size = 24)
        drawLabel("Left click with item in hand to place", app.width // 2, 175, size = 24)
        drawLabel("Left click with tool in hand to break", app.width // 2, 200, size = 24)
        drawRect(app.bbx, app.bby, app.bbw, app.bbh, fill = 'lightGray', align = 'center')
        drawLabel("Back", app.bbx, app.bby, align = 'center')
    elif app.c_tag:
        drawImage(app.credits_img, app.width // 2, app.height // 2, width = 1200, height = 800, align = 'center', opacity = 85)
        drawLabel("Credits", app.width / 2, 75, size = 36)
        drawLabel("Created by Matthew Kibarian", app.width / 2, 150, size = 24)
        drawLabel("Inspirations: Terraria (created by Re-Logic) and 112Craft (created by Carson Swoveland)", app.width / 2, 200, size = 18)
        drawLabel("Asset sources:", app.width / 2, 250, size = 18)
        drawLabel("Logo: Terraria Logo Maker by DarthMorf", app.width / 2, 275, size = 16)
        drawLabel("Backgrounds: MiltVala on Terraria Forums", app.width / 2, 300, size = 16)
        drawLabel("Other assets: Likely from Terraria source code, unless otherwise stated", app.width / 2, 325, size = 16)
        drawLabel("Perlin Noise: Wikipedia page and original papers by Ken Perlin", app.width / 2, 350, size = 16)
        drawRect(app.bbx, app.bby, app.bbw, app.bbh, fill = 'lightGray', align = 'center')
        drawLabel("Back", app.bbx, app.bby, align = 'center')

def in_ts_button(app, mouseX, mouseY): #returns s, c, o depending on which button is pressed
    if (app.sbx - (app.sbw / 2) <= mouseX <= app.sbx + (app.sbw / 2)
        and app.sby - (app.sbh / 2) <= mouseY <= app.sby + (app.sbh / 2)):
        return 's'
    elif (app.cbx - (app.cbw / 2) <= mouseX <= app.cbx + (app.cbw / 2) 
        and app.cby - (app.cbh / 2) <= mouseY <= app.cby + (app.cbh / 2)):
        return 'c'
    elif (app.obx - (app.obw / 2) <= mouseX <= app.obx + (app.obw / 2) 
        and app.oby - (app.obh / 2) <= mouseY <= app.oby + (app.obh / 2)):
        return 'o'
    elif (app.bbx - (app.bbw / 2) <= mouseX <= app.bbx + (app.bbw / 2) 
        and app.bby - (app.bbh / 2) <= mouseY <= app.bby + (app.bbh / 2)):
        return 'b'

def ts_button_press(app, mouseX, mouseY):
    if in_ts_button(app, mouseX, mouseY) == 's':
        print("Start Game Pressed")
        app.gamestate = 'game'
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
        app.sbw = 165
        app.sbh = 82.5
    elif in_ts_button(app, mouseX, mouseY) == 'c':
        app.cbw = 110
        app.cbh = 55
    elif in_ts_button(app, mouseX, mouseY) == 'o':
        app.obw = 110
        app.obh = 55
    elif in_ts_button(app, mouseX, mouseY) == 'b':
        app.bbw = 55
        app.bbh = 27.5
    else:
        app.sbw = 150
        app.cbw, app.obw = 100, 100
        app.sbh = 75
        app.cbh, app.obh = 50, 50


#############################################################
# gameloop -- calculated every frame, updates game state    #
# update world state, update player state, update inventory #
#############################################################

# probably can just call a function from a different file?

def draw_tile(app, tile, i, j):
    x = (i - app.camx) * tilesize + app.width // 2
    y = (j - app.camy) * tilesize + app.height // 2
    drawRect(x, y, x + tilesize, y + tilesize, fill = rgb(*app.tile_dict[tile]))

def draw_game(app):
    if not isinstance(app.world, np.ndarray):
        print("not an array")
        return
    drawRect(app.px, app.py, app.pw, app.ph, fill = 'blue') #draw player
    tiles_onscreen_x = app.width // tilesize
    tiles_onscreen_y = app.height // tilesize
    start_x = int(app.camx - (tiles_onscreen_x // 2))
    end_x = int(app.camx + (tiles_onscreen_x // 2) + 1)
    start_y = int(app.camy - (tiles_onscreen_y // 2))
    end_y = int(app.camy + (tiles_onscreen_y // 2) + 1)
    print(tiles_onscreen_x, tiles_onscreen_y, start_x, start_y, end_x, end_y)
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if 0 <= i < worldcols and 0 <= j < worldrows:
                tile = app.world[i][j]
                draw_tile(app, tile, i, j)

######################################
# general MVC functions for the game #
######################################

def redrawAll(app):
    if app.gamestate == 'worldgen':
        pass
    elif app.gamestate == 'title':
        draw_titlescreen(app)
    elif app.gamestate == 'game':
        draw_game(app)
        

def onMousePress(app, mouseX, mouseY):
    if app.gamestate == 'title':
        ts_button_press(app, mouseX, mouseY)
    elif app.gamestate == 'worldgen':
        pass
    elif app.gamestate == 'game':
        pass

def onMouseMove(app, mouseX, mouseY):
    if app.gamestate == 'title':
        ts_button_bounce(app, mouseX, mouseY)
    elif app.gamestate == 'worldgen':
        pass
    elif app.gamestate == 'game':
        pass

def onStep(app):
    app.step += 1
    app.px += 1
    
    if app.gamestate == 'game':
        app.camx = app.px // tilesize
        app.camy = app.py // tilesize

runApp(width = 1200, height = 800)