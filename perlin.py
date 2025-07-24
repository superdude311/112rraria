# generates the perlin noise map for the given size
# found via https://www.cs.cmu.edu/~112/notes/student-tp-guides/Terrain.pdf
# as this source said, this was "very hard" to implement
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


def smoothing_function(n):
    # smoothing function for the perlin noise
    # based on the new paper's smoothing function
    return ((6 * n**5) - (15 * n**4) + (10 * n**3))

# interpolates the values using the smoothing function
def interpolate(a, b, x):
    return b * smoothing_function(x) + a * (1 - smoothing_function(x))

def dist_comp(x1, y1, x2, y2): #returns distance in component vector form (x, y)
    x = x2 - x1
    y = y2 - y1
    return x, y 

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

def generate_1d_slopes():
    # similar to generate_grid_point, but generatees 1d slopes instead of 2d vectors
    slope = np.empty(worldcols)
    for i in range(worldcols):
        slope[i] = np.random.uniform(-1, 1)
    return slope

def create_1d_gradient_point(i, slope):
    # gets the slopes + distancecs to the left and right of the sampled point
    left_slope = slope[math.floor(i)]
    right_slope = slope[math.floor(i) + 1]
    left_dist = i - math.floor(i)
    right_dist = i - (math.floor(i) + 1)
    dot_left = left_slope * left_dist
    dot_right = right_slope * right_dist
    noise_point = interpolate(dot_left, dot_right, left_dist)
    return noise_point

# generates a 1D gradient noise array
def sample_1d_gradient(scale1d):
    slope = generate_1d_slopes() # generates the slope vectors
    gradient = np.empty(worldrows)
    for i in range(worldrows):
        x = i / scale1d
        raw = create_1d_gradient_point(x, slope)
        gradient[i] = np.interp(raw, (-1, 1), (worldrows - 35, worldrows - 5))
        # normalizes to a height variation of -35 to -5 from the top of the world
    return gradient

def generate_vectorgrid():
    gridrows, gridcols = vectorgridrows + 1, vectorgridcols + 1
    # +1 because the grid is defined by the corners of the squares, not the squares
    vectorgrid = np.empty((gridrows, gridcols, 3))

    for i in range(gridrows):
        for j in range(gridcols):
            vectorgrid[i][j] = generate_grid_point()
            # generates grid of random vectors
    return vectorgrid

def create_2d_gradient_point(i, j, vectorgrid): #returns a "density" value of the noise at the given point
    # this calculates the perlin noise grid square by square
    # while this is somewhat similar to 112craft (which in turn is pretty much the algorithm described in the paper), 
    # the implementation differs as this is a finite world game, so I could build this to a finite sized array
    # instead of an infinite world like in 112craft, which required chunking (I think, I didn't look too closely at the code)

    # gets the 4 corner grid vectors for current world tile
    # 3-tuple of (x, y, z) coordinates, only x and y are used
    topleft = vectorgrid[math.floor(i), math.floor(j)]
    topright = vectorgrid[math.floor(i) + 1, math.floor(j)]
    botleft = vectorgrid[math.floor(i), math.floor(j) + 1]
    botright = vectorgrid[math.floor(i) + 1, math.floor(j) + 1]

    # calculates the distance (x, y) from each perlin grid corner to the current world point
    dv_topleft = dist_comp(math.floor(i), math.floor(j), i, j)
    dv_topright = dist_comp(math.floor(i) + 1, math.floor(j), i, j)
    dv_botleft = dist_comp(math.floor(i), math.floor(j) + 1, i, j)
    dv_botright = dist_comp(math.floor(i) + 1, math.floor(j) + 1, i, j)

    # calculates the dot product of the distance and the vector
    dot_topleft = dv_topleft[0] * topleft[0] + dv_topleft[1] * topleft[1]
    dot_topright = dv_topright[0] * topright[0] + dv_topright[1] * topright[1]
    dot_botleft = dv_botleft[0] * botleft[0] + dv_botleft[1] * botleft[1]
    dot_botright = dv_botright[0] * botright[0] + dv_botright[1] * botright[1]

    x_interp_val = abs(i - math.floor(i))
    i_top = interpolate(dot_topleft, dot_topright, x_interp_val)
    i_bot = interpolate(dot_botleft, dot_botright, x_interp_val)

    # sets the world grid value to the interpolated value
    y_interp_val = abs(j - math.floor(j))
    gradient_point = interpolate(i_top, i_bot, y_interp_val)
    return gradient_point

def sample_2d_gradient(scale):
    vectorgrid = generate_vectorgrid()
    worldgrid = np.empty((worldrows, worldcols))
    for i in range(worldrows):
        for j in range(worldcols):
            # sample the gradient at the given scale
            x = i / scale
            y = j / scale
            raw = create_2d_gradient_point(x, y, vectorgrid)
            worldgrid[i][j] = np.interp(raw, (-1, 1), (0, 255))
            # normalizes the values to 0-255 for drawing
    return worldgrid

# how the freaking heck does perlin actually work bro