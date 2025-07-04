#test file for 112rraria
#tests drawing world array to screen

import numpy as np
from cmu_graphics import *


rows, cols = 10, 20
testarray  = np.random.randint(0, 256, size=(rows, cols), dtype=np.uint8)
print(testarray)
for i in range(rows):
    for j in range(cols):
        drawRect(rows, cols, 1, fill = rgb(testarray[i,j]))


#draw black and white array to screen with x,y being testarray[y][x]