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

def generateGridPoint():
    # creates the unit vectors to use to generate the noise (source: updated paper)
    perlin_vectors = np.array((1,1,0),(-1,1,0),(1,-1,0),(-1,-1,0),
                            (1,0,1),(-1,0,1),(1,0,-1),(-1,0,-1),
                            (0,1,1),(0,-1,1),(0,1,-1),(0,-1,-1),
                            (1,1,0),(-1,1,0),(0,-1,1),(0,-1,-1)) 
    # note: 4 extra vectors are added to the end of the array
    # to improve computational efficiency (as detailed in the updated paper)

    # chooses 4 random vectors from the perlin_vectors array
    # these vectors serve as the corners of the grid cell
    topleft = perlin_vectors[np.random.randint(0, 16)] 
    topright = perlin_vectors[np.random.randint(0, 16)]
    botleft = perlin_vectors[np.random.randint(0, 16)]
    botright = perlin_vectors[np.random.randint(0, 16)]

    return topleft, topright, botleft, botright

worldrows, worldcols = 2000, 1000
gridrows, gridcols = worldrows // 10, worldcols // 10
grid = np.array()
# how the freaking heck does perlin actually work bro
