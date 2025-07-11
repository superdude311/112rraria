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
import math
from worldsetup import *

def generate_grid_point():
    # creates the unit vectors to use to generate the noise (source: updated paper)
    perlin_vectors = np.array([[1,1,0],[-1,1,0],[1,-1,0],[-1,-1,0],
                            [1,0,1],[-1,0,1],[1,0,-1],[-1,0,-1],
                            [0,1,1],[0,-1,1],[0,1,-1],[0,-1,-1],
                            [1,1,0],[-1,1,0],[0,-1,1],[0,-1,-1]]) 
    # note: 4 extra vectors are added to the end of the array
    # to improve computational efficiency (as detailed in the updated paper)

    # randomly select one of the vectors to use for the grid point
    vector = perlin_vectors[np.random.randint(0, 16)] 
    return vector

def smoothing_function(n):
    # smoothing function for the perlin noise
    # based on the new paper's smoothing function
    return ((6 * n**5 - 15) * (n**4 + 1) * n**3)

def dist_comp(x1, y1, x2, y2): #returns distance in component vector form (x, y)
    x = x2 - x1
    y = y2 - y1
    return x, y 

def create_gradient():

    scale = 10  # scale of the grid, can be adjusted for different resolutions
    gridrows, gridcols = worldrows // scale, worldcols // scale
    vectorgrid = np.empty((gridrows, gridcols, 3), dtype=np.uint8)
    worldgrid = np.empty((worldrows, worldcols), dtype=np.uint8)

    for i in range(gridrows):
        for j in range(gridcols):
            vectorgrid[i, j] = generate_grid_point()
            # generates grid of random vectors

    for i in range(worldrows):
        for j in range(worldcols):
            # this calculates the perlin noise grid square by square
            # while this is somewhat similar to 112craft (which in turn is pretty much the algorithm described in the paper), 
            # the implementation differs as this is a finite world game, so I could build this to a finite sized array

            print('\n')
            # gets the 4 corner grid vectors for current world tile
            # 3-tuple of (x, y, z) coordinates, only x and y are used
            topleft = vectorgrid[math.floor(i / scale) - 1, math.floor(j / scale) - 1]
            topright = vectorgrid[math.floor(i / scale) - 1, math.ceil(j / scale) - 1]
            botleft = vectorgrid[math.ceil(i / scale) - 1, math.floor(j / scale) - 1]
            botright = vectorgrid[math.ceil(i / scale) - 1, math.ceil(j / scale) - 1]
            print(f"topleft: {topleft}, topright: {topright}, botleft: {botleft}, botright: {botright}")

            # # calculates the magnitude of each vector
            # m_topleft = np.sqrt(topleft[0]**2 + topleft[1]**2)
            # m_topright = np.sqrt(topright[0]**2 + topright[1]**2)
            # m_botleft = np.sqrt(botleft[0]**2 + botleft[1]**2)
            # m_botright = np.sqrt(botright[0]**2 + botright[1]**2)
            # print(f"m_topleft: {m_topleft}, m_topright: {m_topright}, m_botleft: {m_botleft}, m_botright: {m_botright}")

            # calculates the distance (magnitude and angle) from the current world tile to each corner
            dv_topleft = dist_comp(i, j, topleft[0] * scale, topleft[1] * scale)
            dv_topright = dist_comp(i, j, topright[0] * scale, topright[1] * scale)
            dv_botleft = dist_comp(i, j, botleft[0] * scale, botleft[1] * scale)
            dv_botright = dist_comp(i, j, botright[0] * scale, botright[1] * scale)
            print(f"dv_topleft: {dv_topleft}, dv_topright: {dv_topright}, dv_botleft: {dv_botleft}, dv_botright: {dv_botright}")

            # calculates the dot product of the distance and the vector
            dot_topleft = dv_topleft[0] * topleft[0] + dv_topleft[1] * topleft[1]
            dot_topright = dv_topright[0] * topright[0] + dv_topright[1] * topright[1]
            dot_botleft = dv_botleft[0] * botleft[0] + dv_botleft[1] * botleft[1]
            dot_botright = dv_botright[0] * botright[0] + dv_botright[1] * botright[1]
            print(f"dot_topleft: {dot_topleft}, dot_topright: {dot_topright}, dot_botleft: {dot_botleft}, dot_botright: {dot_botright}")

            # interpolates the values using the smoothing function
            def interpolate(a, b, x):
                return b * smoothing_function(x) + a * (1 - smoothing_function(x))
            
            print(i / scale - i // scale)

            x_interp_val = i / scale - i // scale
            if x_interp_val == 0.0:
                x_interp_val += random()
            
            i_top = interpolate(dot_topleft, dot_topright, x_interp_val)
            i_bot = interpolate(dot_botleft, dot_botright, x_interp_val) #fill none with the correct x value
            # sets the world grid value to the interpolated value

            y_interp_val = j / scale - j // scale
            if y_interp_val == 0.0:
                y_interp_val += random()

            worldgrid[i][j] = interpolate(i_top, i_bot, y_interp_val)
            print(f"i_top: {i_top}, i_bot: {i_bot}, interp: {worldgrid[i][j]}")

    print(worldgrid)
    return worldgrid

def main():
    create_gradient()

main()
# how the freaking heck does perlin actually work bro