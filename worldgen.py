#112rraria
# this code generates the world for the game, and is run once at the start of the game

from perlin import *
# import perlin noise functions from perlin.py
import numpy as np
import random

def terraingen():
    # generates terrain for the world
    # uses perlin noise (so I can flex) to create terrain with caves and hills
    updated_world = np.empty((worldrows, worldcols))  # creates an empty world array
    base_perlin = sample_2d_gradient(scale)  # generates the base perlin noise gradient
    terrain_height = sample_1d_gradient(scale)  # generates the terrain height gradient
    for i in range(worldrows):
        for j in range(worldcols):
            height = terrain_height[i]
            # height is the height of the terrain at the given column
            if j < worldrows - height:
                updated_world[i][j] = 0  # sets the terrain to air
            elif j >= worldcols - 5:
                updated_world[i][j] = 4 # barrier at the bottom of the world
            elif (worldrows - height) <= j <= worldrows - (height - 2):
                if base_perlin[i][j] < 105:
                    updated_world[i][j] = 0
                else:
                    updated_world[i][j] = 1 # grass
            elif j <= worldrows - (height - 7):
                    if base_perlin[i][j] < 105:   # LOWER threshold than stone caves!
                        updated_world[i][j] = 0  # air cave inside dirt
                    else:
                        updated_world[i][j] = 2  # dirt
            elif worldrows - (height - 7) < j < worldrows - 5:
                if base_perlin[i][j] < 115:
                    updated_world[i][j] = 0 #air if less than 115
                else:
                    updated_world[i][j] = 3 # stone if greater than 115

    return updated_world #2d array of terrain tiles


def ores(worldmap):
    terrain = worldmap
    top_ores = ['copper', 'tin', 'iron']
    mid_ores = ['gold', 'silver', 'lead']
    bot_ores = ['palladium', 'mithril', 'platinum'] 
    top_range = (5, worldcols // 3)
    mid_range = (worldcols // 3, 2 * worldcols // 3)
    bot_range = (2 * worldcols // 3, worldcols - 1)
    ore_IDs = {'copper': 10, 'tin': 11, 'iron': 12,
                'gold': 13, 'silver': 14, 'lead': 15,
                'palladium': 16, 'mithril': 17, 'platinum': 18}
    
    # generates ores in blobs in the world 
    # ores are generated inside rocks, with a chance to poke out into caves
    # different ores get more common as the player goes deeper into the world

    def paint_ore_blob(world, x, y, ore_id, radius):
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                nx = x + dx
                ny = y + dy
                if 0 < nx < worldrows and 0 < ny < worldrows and world[nx][ny] == 3:
                    if random.randrange(1, 5) != 1:
                        world[nx][ny] = ore_id
    
    def sprinkle_blobs(world):
        blobs_per_band = 25

        for _ in range(blobs_per_band):
            for bandrange, ores in [(top_range, top_ores), (mid_range, mid_ores), (bot_range, bot_ores)]:
                x = random.randint(0, worldrows - 1)
                y = random.randint(*bandrange)

                if world[x][y] == 3: #if stone
                    ore = random.choice(ores)
                    radius = random.randint(1, 3)
                    paint_ore_blob(world, x, y, ore_IDs[ore], radius)
        return world
    
    sprinkle_blobs(terrain)
    return terrain #2d array of world, now including ore tiles

def worldgen():
    terrain = terraingen()
    ore_world = ores(terrain) #adds ores to the world
    print("world created")
    # initializes the game world
    return ore_world  # returns the generated world array