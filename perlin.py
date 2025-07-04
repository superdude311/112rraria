# generates the perlin noise map for the given size
# based on https://en.wikipedia.org/wiki/Perlin_noise
# and original papers from Ken Perlin:
# https://dl.acm.org/doi/pdf/10.1145/325165.325247
    # henceforth referred to as the "original paper"
# https://mrl.cs.nyu.edu/~perlin/paper445.pdf 
    # henceforth referred to as the "updated paper"

# created by Matthew Kibarian (AndrewID: mkibaria) for 112rraria

import numpy as np
from cmu_graphics import *

def generate_grid_point():
    # creates the unit vectors to use to generate the noise (source: updated paper)
    perlin_vectors = np.array((1,1,0),(-1,1,0),(1,-1,0),(-1,-1,0),
                            (1,0,1),(-1,0,1),(1,0,-1),(-1,0,-1),
                            (0,1,1),(0,-1,1),(0,1,-1),(0,-1,-1),
                            (1,1,0),(-1,1,0),(0,-1,1),(0,-1,-1)) 
    # note: 4 extra vectors are added to the end of the array
    # to improve computational efficiency (as detailed in the updated paper)

    # randomly select one of the vectors to use for the grid point
    vector = perlin_vectors[np.random.randint(0, 16)] 
    return vector

scale = 10  # scale of the grid, can be adjusted for different resolutions
worldrows, worldcols = 2000, 1000
gridrows, gridcols = worldrows // scale, worldcols // scale
vectorgrid = np.empty((gridrows, gridcols), dtype=np.uint8)
worldgrid = np.empty((worldrows, worldcols), dtype=np.uint8)

for i in range(gridrows):
    for j in range(gridcols):
        vectorgrid[i][j] = generate_grid_point()
        # generates grid of random vectors

def smoothing_function(n):
    # smoothing function for the perlin noise
    # based on the new paper's smoothing function
    return 6 * n**5 - 15 * n**4 + 10 * n**3

def dist(x1, y1, x2, y2):
    # calculates the distance between two points
    d = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    a = np.arctan2(y2 - y1, x2 - x1)
    return d, a # returns a tuple of (distance, angle)

def create_gradient():
    for i in range(worldrows):
        for j in range(worldcols):
            # gets the 4 corner grid vectors for current world tile
            # 3-tuple of (x, y, z) coordinates, only x and y are used
            topleft = vectorgrid(np.floor(i / scale), np.floor(j / scale))
            topright = vectorgrid(np.floor(i / scale), np.ceil(j / scale))
            botleft = vectorgrid(np.ceil(i / scale), np.floor(j / scale))
            botright = vectorgrid(np.ceil(i / scale), np.ceil(j / scale))

            # calculates the magnitude of each vector
            m_topleft = np.sqrt(topleft[0]**2 + topleft[1]**2)
            m_topright = np.sqrt(topright[0]**2 + topright[1]**2)
            m_botleft = np.sqrt(botleft[0]**2 + botleft[1]**2)
            m_botright = np.sqrt(botright[0]**2 + botright[1][1]**2)

            # calculates the distance (magnitude and angle) from the current world tile to each corner
            dv_topleft = dist(i, j, topleft[0] * scale, topleft[1] * scale)
            dv_topright = dist(i, j, topright[0] * scale, topright[1] * scale)
            dv_botleft = dist(i, j, botleft[0] * scale, botleft[1] * scale)
            dv_botright = dist(i, j, botright[0] * scale, botright[1] * scale)

            # calculates the dot product of the distance and the vector
            dot_topleft = dv_topleft[0] * m_topleft * np.cos(dv_topleft[1])
            dot_topright = dv_topright[0] * m_topright * np.cos(dv_topright[1])
            dot_botleft = dv_botleft[0] * m_botleft * np.cos(dv_botleft[1])
            dot_botright = dv_botright[0] * m_botright * np.cos(dv_botright[1])

            # interpolates the values using the smoothing function
            def interpolate(a, b, x):
                return b * smoothing_function(x) + a * (1 - smoothing_function(x))
            
            i_top = interpolate(dot_topleft, dot_topright, None)
            i_bot = interpolate(dot_botleft, dot_botright, None) #fill none with the correct x value

            # sets the world grid value to the interpolated value
            worldgrid[i][j] = interpolate(i_top, i_bot, None)
    return worldgrid

# how the freaking heck does perlin actually work bro