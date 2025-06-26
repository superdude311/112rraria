#112rraria
# this code generates the world for the game, and is run once at the start of the game

# pseudocode mapping
def terraingen():
    # generates terrain for the world
    # carson recommendation:use a numpy array and set the dtype to uint8 and use that for your big tile grid
    # uses perlin noise (so I can flex) to create terrain with caves and hills
    return #2d array of terrain tiles

def ores():
    # generates ores in blobs in the world using a different random noise function
    # ores are generated inside rocks, with a chance to poke out into caves
    # ores get more common as the player goes deeper into the world
    return #2d array of ore tiles

def water():
    # generates water bodies in the world
    # water is generated above certain depth, with a smaller chance to generate in caves
    # water (somehow) checks for terrain and flows down if able
    return #2d array of water tiles

def trees():
    #adds trees to the world at random positions
    #trees are between x and y tiles tall, with leaves on top
    #when broken, all adjacent wood tiles are dropped, and leaves have a chance to drop saplings
    #trees are generated in a way that they don't overlap with terrain or other trees
    return #2d array of tree tiles


def worldgen():
    terraingen()
    ores()
    water() 
    trees() #worst case i can get rid of trees
    # initializes the game world
    

