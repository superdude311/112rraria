# 112rraria
# a 15-112 Term Project, created by Matthew Kibarian
# This project is a 2D game inspired by the classic game Terraria
# It features a procedurally generated world, player character, and various game mechanics
# including mining, building, and combat (maybe)

# Note:
# I would've used screens for a lot of this, but I didn't know about them until I was far too deep to restart
# I would've also used classes, and I plan on doing so if I ever add enemies to this game 

# titlescreen logo generated with Terraria Logo Maker: https://terraria-logo-maker.darthmorf.co.uk/
# titlescreen background image created by MiltVala: https://forums.terraria.org/index.php?threads/terraria-desktop-wallpapers.12644/
# sprites found from spriters-resource.com: https://www.spriters-resource.com/pc_computer/terraria/sheet/131821/

from cmu_graphics import *
from worldsetup import *
from worldgen import *

'''
toolIDs:
5: stone pickaxe, 6: iron pickaxe, 7: golden drill
8: magic mirror
note itemIDs: 
Tier 0: 0: air, 1: grass, 2: dirt, 3: stone,
Tier 1: 10: copper, 11:tin, 12: iron
Tier 2: 13: gold, 14: silver, 15: lead
Tier 3: 16: palladium, 17: mithril, 18: platinum
Unbreakable: 4: barrier
'''

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
                     17:(28, 252, 159), 18:(28, 230, 252)} # itemID-color dict (replace w/ sprite URLs)

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
    app.ax = 2.5 #friction (x axis)
    app.grav = 2.5 #gravity
    app.vxcap = 25  #velocity cap (x)
    app.vycap = 25 #velocity cap (y)
    app.lflag = False #press left flag
    app.rflag = False #press right flag
    app.pw = tilesize
    app.ph = tilesize * 2 #player width/height
    app.camx, app.camy = app.px // tilesize, app.py // tilesize
    app.grounded = False
    app.tools = {'q':5, 'w':6, 'e':7, 'r':8} #maps key presses to toolIDs
    app.items = {'1':1, '2':1, '3':3, '4':10, '5':11, '6':12, '7':13, '8':14, '9':15, '0':16, '-':17, '=':18} # maps key presses to itemIDs
    app.toolset = set() # add to this set when the tool is gotten
    app.toolset.add(8)
    app.itemcounts = {1:0, 2:0, 3:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0} #maps itemIDs to their counts (all start = 0)
    app.IDtoname = {1:"Grass", 2:"Dirt", 3:"Stone", 5:"Stone Pickaxe", 6:"Iron Pickaxe", 7:"Golden Drill", 8:"Magic Mirror",
                    10:"Copper", 11:"Tin", 12:"Iron", 13:"Gold", 14:"Silver", 15:"Lead", 16:"Palladium", 17:"Mithril",
                    18:"Platinum"} #maps itemIDs/toolIDs to names (for displaying)
    app.held = None #held itemID
    app.bgimg = 'game-bg-img.png'
    app.debug = False
    app.fastmode = False
    #ItemID to image path dict
    #dear god, make the pain stop
    app.IDtoImage = {1:['sprites/grass0.png', 'sprites/grass1.png', 'sprites/grass2.png'],
                     2:['sprites/dirt0.png', 'sprites/dirt1.png', 'sprites/dirt2.png'],
                     3:['sprites/stone0.png', 'sprites/stone1.png', 'sprites/stone2.png'],
                     5:"sprites/'stone'_pickaxe.png", 
                     6:"sprites/'iron'_pickaxe.png", 
                     7:"sprites/'golden'_drill.png", 
                     8:'sprites/magicmirror.png',
                     10:['sprites/copper0.png', 'sprites/copper1.png', 'sprites/copper2.png'],
                     11:['sprites/tin0.png', 'sprites/tin1.png', 'sprites/tin2.png'],
                     12:['sprites/iron0.png', 'sprites/iron1.png', 'sprites/iron2.png'],
                     13:['sprites/gold0.png', 'sprites/gold1.png', 'sprites/gold2.png'],
                     14:['sprites/silver0.png', 'sprites/silver1.png', 'sprites/silver2.png'],
                     15:['sprites/lead0.png', 'sprites/lead1.png', 'sprites/lead2.png'],
                     16:['sprites/pallad0.png', 'sprites/pallad1.png', 'sprites/pallad2.png'],
                     17:['sprites/mith0.png', 'sprites/mith1.png', 'sprites/mith2.png'],
                     18:['sprites/plat0.png', 'sprites/plat1.png', 'sprites/plat2.png']}
    

##########################################################
# initialize game                                        #   
# generate world, show some kind of loading indicator    #
##########################################################

def create_world(app):
    app.world = worldgen()
    app.texturevariants = texturevariants()
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
        drawImage(app.options_img, app.width // 2, app.height // 2, width = 1200, height = 800, align = 'center', opacity = 75)
        drawLabel("Options (and how to play)", app.width / 2, 75, size = 36)
        drawLabel("Press the up arrow or space to jump", app.width // 2, 125, size = 24)
        drawLabel("Press left/right arrow or a/d to move", app.width // 2, 150, size = 24)
        drawLabel("Left click with item in hand to place", app.width // 2, 175, size = 24)
        drawLabel("Left click with tool in hand to break", app.width // 2, 200, size = 24)
        drawLabel("Press 'i' to open the info/debug menu", app.width // 2, 225, size = 24)
        drawLabel("Press keys 1 through + to select different blocks", app.width // 2, 250, size = 24)
        drawLabel("Press Q, W, and E to select tools", app.width // 2, 275, size = 24)
        drawLabel("Press R to use the Magic Mirror, which warps you to the top of the map", app.width // 2, 300, size = 24)
        drawLabel('Press F to toggle Fast Mode, which renders tiles using rectangles', app.width // 2, 325, size = 24)
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
        drawLabel("Sprites: Spriters-resource.com", app.width / 2, 325, size = 16)
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

def is_player_legal(app, newx, newy):
    top = newy // tilesize
    left = newx // tilesize
    bot = (newy + app.ph - 1) // tilesize
    right = (newx + app.pw - 1) // tilesize

    for row in range(math.floor(top), math.floor(bot) + 1): #checks all the player tiles
        for col in range(math.floor(left), math.floor(right) + 1):
            if not (0 <= col < len(app.world[0])) or not (0 <= row < len(app.world)):
                return False # not legal if outside world
            if app.world[col][row] != 0:
                return False # or if in a block
    return True

def is_tile_empty(app, world_x, world_y):
    row = int(world_y // tilesize)
    col = int(world_x // tilesize)
    if (0 <= row < worldrows and 0 <= col < worldcols):
        return app.world[col][row] == 0
    return False

def break_check(app, tiletype):
    if app.held == 5:
        if tiletype <= 12 and tiletype != 4:
            return True  
        return False
    if app.held == 6:
        if tiletype <= 15 and tiletype != 4:
            return True  
        return False    
    if app.held == 7:
        if tiletype <= 18 and tiletype != 4:
            return True  
        return False
# if item in hand is tool, and item in hand can break block, break block
# else if item in hand is block, and tile is empty, place block
# else do nothing
def click_block(app, mouse_x, mouse_y):
    tile_offset_x = (mouse_x - (app.width // 2)) // tilesize
    tile_offset_y = (mouse_y - (app.height // 2)) // tilesize
    tilecol = int(app.camx + tile_offset_x)
    tilerow = int(app.camy + tile_offset_y)
    if 0 <= tilecol < worldcols and 0 <= tilerow < worldrows:
        print(app.toolset)
        if app.held in app.toolset and app.world[tilecol][tilerow] != 0:
            if break_check(app, app.world[tilecol][tilerow]):
                tiletype = app.world[tilecol][tilerow]
                app.world[tilecol][tilerow] = 0
                app.itemcounts[tiletype] += 1
        elif app.held in app.itemcounts:
            if app.itemcounts[app.held] >= 1 and app.world[tilecol][tilerow] == 0: #if you have enough items and tile empty
                app.world[tilecol][tilerow] = app.held #places block
                app.itemcounts[app.held] -= 1 #removes one from inv
            elif 0 < app.world[tilecol][tilerow] <= 3: #allows you to still break blocks if you don't have tools
                tiletype = app.world[tilecol][tilerow] # will be 1, 2, 3
                app.world[tilecol][tilerow] = 0 
                app.itemcounts[tiletype] += 1 #adds to inventory
        elif app.held == None or (app.held != 5 and app.held != 6 and app.held != 7):
            if 0 < app.world[tilecol][tilerow] <= 3: # really cursed way of checking if its stone/grass/dirt
                tiletype = app.world[tilecol][tilerow] # will be 1, 2, 3
                app.world[tilecol][tilerow] = 0 
                app.itemcounts[tiletype] += 1 #adds to inventory
                print(app.itemcounts)

def game_key_press(app, key):
    if key == 'esc' or key == 'escape':
        app.gamestate = 'title'
    if key == 'i':
        app.debug = not app.debug
    if key == 'f':
        app.fastmode = not app.fastmode

def movement_key_hold(app, keys):
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
    # if y under cap and on ground, and pressing up/space
    if ('up' in keys or 'space' in keys) and app.vy < app.vycap and app.grounded: 
        app.grounded = False
        app.vy = -app.vycap # jump velocity
        if app.vy > app.vycap: # if y over cap
            app.vy = -app.vycap 

def movement_key_release(app, key):
    if key == 'left' or key == 'a':
        app.lflag = False
    if key == 'right' or key == 'd':
        app.rflag = False


# I read over the following document for collisions as well as what we learned in tetris
# https://2dengine.com/doc/intersections.html
def movement_step(app):
    app.vy += app.grav  # apply gravity
    app.grounded = False

    if not app.lflag and app.vx < 0: # if not pressing left, and moving left
        app.vx += app.ax # decelerate by friction
    if not app.rflag and app.vx > 0: # if not pressing right, and moving right
        app.vx -= app.ax # decelerate by friction

    if app.vy < -app.vycap: # if y over cap (when falling)
        app.vy = -app.vycap 

    if is_player_legal(app, app.px + app.vx, app.py): 
        app.px += app.vx # move left/right

    if app.vy != 0: # player is moving
        step_y = 1 if app.vy > 0 else - 1 #stepping down if v > 0, else stepping up
        for i in range(math.ceil(abs(app.vy))): # check each mini-step 
            next_y = app.py + step_y
            right_x = app.px + app.pw - 1 #right edge of player hitbox
            if step_y > 0: #check foot collision if falling
                bot_y = next_y + app.ph - 1 # bottom of player hitbox (feet)
                if is_tile_empty(app, app.px, bot_y) and is_tile_empty(app, right_x, bot_y):
                    app.py = next_y
                else:
                    if step_y > 0:
                        app.grounded = True
                    app.vy = 0
                    break
            else: #check head collision if rising
                if is_tile_empty(app, app.px, next_y) and is_tile_empty(app, right_x, next_y):
                    app.py = next_y
                else:
                    app.vy = 0
                    break

def inv_keypress(app, key):
    # polls key presses and displays item
    if key == '1' and app.items[key] > 0:
        app.held = 1
    elif key == '2' and app.items[key] > 0:
        app.held = 2
    elif key == '3' and app.items[key] > 0:
        app.held = 3
    elif key == '4' and app.items[key] > 0:
        app.held = 10
    elif key == '5' and app.items[key] > 0:
        app.held = 11
    elif key == '6' and app.items[key] > 0:
        app.held = 12
    elif key == '7' and app.items[key] > 0:
        app.held = 13
    elif key == '8' and app.items[key] > 0:
        app.held = 14
    elif key == '9' and app.items[key] > 0:
        app.held = 15
    elif key == '0' and app.items[key] > 0:
        app.held = 16
    elif key == '-' and app.items[key] > 0:
        app.held = 17
    elif key == '=' and app.items[key] > 0:
        app.held = 18
    elif key == 'q' and app.tools[key] in app.toolset:
        app.held = 5
    elif key == 'w' and app.tools[key] in app.toolset:
        app.held = 6
    elif key == 'e' and app.tools[key] in app.toolset:
        app.held = 7
    elif key == 'r':
        app.held = 8 #magic mirror
        app.py = 0

# if key is pressed for tool, and you have enough items, add tool to toolset
# once there are enough items, maybe i can flash the tool on the screen
def crafting(app, key):
    if key == 'q' and 5 not in app.toolset:
        if app.itemcounts[3] >= 6: # if you have 6 stone
            app.itemcounts[3] -= 6
            app.toolset.add(5) # add pickaxe
    if key == 'w' and 6 not in app.toolset:
        if app.itemcounts[3] >= 3 and app.itemcounts[12] >= 6:
            app.itemcounts[3] -= 3
            app.itemcounts[12] -= 6
            app.toolset.add(6)
    if key == 'e' and 7 not in app.toolset:
        if app.itemcounts[3] >= 3 and app.itemcounts[13] >= 6:
            app.itemcounts[3] -= 3
            app.itemcounts[13] -= 6
            app.toolset.add(7)

def draw_tools_menu(app):
    for i in range(4):
        drawRect(25, 25 + 75 * i, 75, 75, fill = 'lightGrey', border = 'black', borderWidth = 2, opacity = 75)
    drawRect(25, 25, 75, 300, fill = None, border = 'black', borderWidth = 4)
    drawLabel('Q', 87.5, 87.5, bold = True)
    drawLabel('W', 87.5, 162.5, bold = True)
    drawLabel('E', 87.5, 237.5, bold = True)
    if 5 not in app.toolset:
        if app.itemcounts[3] < 6:
           drawLabel('need', 62.5, 50)
           drawLabel(f'{6 - app.itemcounts[3]} stone', 62.5, 62.5)
        elif app.itemcounts[3] >= 6:
            drawLabel('press Q', 62.5, 50)
            drawLabel('to craft', 62.5, 62.5)
    else:
        drawImage(app.IDtoImage[5], 37.5, 37.5, width = 50, height = 50)
        if 6 not in app.toolset:
            if app.itemcounts[3] < 3 or app.itemcounts[12] < 6:
                drawLabel('need', 62.5, 125)
                if app.itemcounts[12] < 6:
                    drawLabel(f'{6 - app.itemcounts[12]} iron', 62.5, 137.5)
                if app.itemcounts[3] < 3:
                    drawLabel(f'{3 - app.itemcounts[3]} stone', 62.5, 150)
            elif app.itemcounts[3] >= 3 and app.itemcounts[12] >= 6:
                drawLabel('press W', 62.5, 125)
                drawLabel('to craft', 62.5, 137.5)
        else:
            drawImage(app.IDtoImage[6], 37.5, 112.5, width = 50, height = 50)
            if 7 not in app.toolset:
                if app.itemcounts[3] < 3 or app.itemcounts[13] < 6:
                    drawLabel('need', 62.5, 200)
                    if app.itemcounts[12] < 6:
                        drawLabel(f'{6 - app.itemcounts[13]} gold', 62.5, 212.5)
                    if app.itemcounts[3] < 3:
                        drawLabel(f'{3 - app.itemcounts[3]} stone', 62.5, 225)
                elif app.itemcounts[3] >= 3 and app.itemcounts[13] >= 6:
                    drawLabel('press E', 62.5, 200)
                    drawLabel('to craft', 62.5, 212.5)
            else:
                drawImage(app.IDtoImage[7], 37.5, 200, width = 50, height = 24, rotateAngle = -45)
    drawImage(app.IDtoImage[8], 37.5, 262.5, width = 50, height = 50)
    drawLabel('R', 87.5, 312.5, bold = True)
    # draws the tools pane on the side/bottom/top with all of the tools (which are unlocked)
    # selected tool is a larger rectangle with text showing what it is

def draw_held(app):
    drawRect((app.width // 2) - 50, app.height - 125, 100, 100, fill = 'gold', border = 'black', borderWidth = 4, opacity = 75)
    if app.held != None and (app.held in app.toolset or app.held in app.itemcounts or app.held == 8):
        if app.held != 7 and app.held in app.toolset: # is tool
            drawLabel(app.IDtoname[app.held], app.width // 2, app.height - 137.5, size = 18, bold = True, fill = 'white')
            drawImage(app.IDtoImage[app.held], (app.width // 2) - 37.5, app.height - 112.5, width = 75, height = 75)
        if app.held in app.itemcounts and app.itemcounts[app.held] > 0: # is item, and you have item
            drawLabel(app.IDtoname[app.held], app.width // 2, app.height - 137.5, size = 18, bold = True, fill = 'white')
            drawImage(app.IDtoImage[app.held][0], (app.width // 2) - 37.5, app.height - 112.5, width = 75, height = 75)
        if app.held == 7: # is drill (needs to be rotated)
            drawLabel(app.IDtoname[app.held], app.width // 2, app.height - 137.5, size = 18, bold = True, fill = 'white')
            drawImage(app.IDtoImage[7], (app.width // 2) - 37.5, app.height - 93.75, width = 1.1 * 75, height = 1.1 * 36, rotateAngle = -45)

def draw_blocks_menu(app):
    # draws the inventory pane on the side/bottom/top with all of the blocks and their counts in it
    # selected block is a larger rectangle with text showing what it is
    drawRect(100, app.height - 100, 450, 75, fill = None, border = 'black', borderWidth = 4)
    drawRect((app.width // 2) + 50, app.height - 100, 450, 75, fill = None, border = 'black', borderWidth = 4)
    for i in range(6):
        #draw grid left side
        drawRect(100 + 75 * i, app.height - 100, 75, 75, fill = 'lightGrey', border = 'black', borderWidth = 2, opacity = 75)
        #draw grid right side
        drawRect((app.width // 2) + 50 + 75 * i, app.height - 100, 75, 75, fill = 'lightGrey', border = 'black', borderWidth = 2, opacity = 75)
    for i in range(1, 4):
        drawImage(app.IDtoImage[i][0], 37.5 + 75 * i, app.height - 87.5, width = 50, height = 50) # 1, 2, 3
        drawLabel(app.itemcounts[i], 37.5 + 75 * i, app.height - 37.5, size = 14, bold = True)
        drawImage(app.IDtoImage[i + 9][0], 262.5 + 75 * i, app.height - 87.5, width = 50, height = 50) # 10, 11, 12
        drawLabel(app.itemcounts[i + 9], 262.5 + 75 * i, app.height - 37.5, size = 14, bold = True)
        drawImage(app.IDtoImage[i + 12][0], 587.5 + 75 * i, app.height - 87.5, width = 50, height = 50) # 13, 14, 15
        drawLabel(app.itemcounts[i + 12], 587.5 + 75 * i, app.height - 37.5, size = 14, bold = True)
        drawImage(app.IDtoImage[i + 15][0], 812.5 + 75 * i, app.height - 87.5, width = 50, height = 50) # 16, 17, 18
        drawLabel(app.itemcounts[i + 15], 812.5 + 75 * i, app.height - 37.5, size = 14, bold = True)
        drawLabel(f'{i + 6}', 637.5 + 75 * i, app.height - 37.5, size = 14, bold = True) # keys 7-9
    for i in range(6):
        drawLabel(f'{i + 1}', 162.5 + 75 * i, app.height - 37.5, size = 14, bold = True) #keys 1-6
    drawLabel('0', 937.5, app.height - 37.5, size = 14, bold = True)
    drawLabel('-', 1012.5, app.height - 35, size = 14, bold = True)
    drawLabel('=', 1087.5, app.height - 37.5, size = 14, bold = True)

def draw_tile(app, tileID, tvar, i, j):
    x = (i - app.camx) * tilesize + app.width // 2
    y = (j - app.camy) * tilesize + app.height // 2
    if tileID != 0:
        if tileID == 4:
            drawRect(x, y, tilesize, tilesize, fill = rgb(0, 0, 0))
        else:
            if not app.fastmode:
                drawImage(app.IDtoImage[tileID][tvar], x, y, width = tilesize, height = tilesize)
            else:
                drawRect(x, y, tilesize, tilesize, fill = rgb(*app.tile_dict[tileID]))


def draw_game(app):
    tiles_onscreen_x = app.width // tilesize
    tiles_onscreen_y = app.height // tilesize
    start_x = int(app.camx - (tiles_onscreen_x // 2))
    end_x = int(app.camx + (tiles_onscreen_x // 2) + 1)
    start_y = int(app.camy - (tiles_onscreen_y // 2))
    end_y = int(app.camy + (tiles_onscreen_y // 2) + 1)
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if (0 <= i < worldcols) and (0 <= j < worldrows):
                tvar = int(app.texturevariants[i][j])
                tileID = app.world[i][j]
                if tileID != 0:
                    draw_tile(app, tileID, tvar, i, j)
            elif (0 <= j < worldrows):
                tvar = None
                draw_tile(app, 0, tvar, i, j) #draw white over out of bounds tiles to prevent smearing

######################################
# general MVC functions for the game #
######################################

def redrawAll(app):
    if app.gamestate == 'worldgen':
        pass
    elif app.gamestate == 'title':
        draw_titlescreen(app)
    elif app.gamestate == 'game':
        drawImage(app.bgimg, 0, 0, width = 2400, height = 1600)
        draw_game(app)
        screen_x = (app.px - app.camx * tilesize) + app.width  // 2
        screen_y = (app.py - app.camy * tilesize) + app.height // 2
        if app.debug:
            drawLabel(f"(x, y) coordinate: {(app.px, app.py)}", app.width - 100, 35)
            drawLabel(f"(x, y) velocity: {(app.vx, app.vy)}", app.width - 100, 55)
        drawRect(screen_x, screen_y, app.pw, app.ph, fill = 'blue') #draw player
        draw_tools_menu(app)
        draw_held(app)
        draw_blocks_menu(app)

def onMousePress(app, mouseX, mouseY):
    if app.gamestate == 'title':
        ts_button_press(app, mouseX, mouseY)
    elif app.gamestate == 'worldgen':
        pass
    elif app.gamestate == 'game':
        click_block(app, mouseX, mouseY)
        pass

def onKeyPress(app, key):
    if app.gamestate == 'game':
        game_key_press(app, key)
        crafting(app, key)
        inv_keypress(app, key)

def onKeyHold(app, keys):
    if app.gamestate == 'game':
        movement_key_hold(app, keys)

def onKeyRelease(app, key):
    if app.gamestate == 'game':
        movement_key_release(app, key)

def onMouseMove(app, mouseX, mouseY):
    if app.gamestate == 'title':
        ts_button_bounce(app, mouseX, mouseY)
    elif app.gamestate == 'worldgen':
        pass
    elif app.gamestate == 'game':
        pass

def onStep(app):
    app.step += 1
    if app.gamestate == 'game':
        movement_step(app)
        app.camx = app.px // tilesize
        app.camy = app.py // tilesize

runApp(width = 1200, height = 800)