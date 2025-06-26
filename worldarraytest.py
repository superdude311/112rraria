#test file for 112rraria
#tests drawing world array to screen

import numpy as np
# cmu graphics library here 

rows, cols = 10, 20
testarray  = np.random.randint(0, 256, size=(rows, cols), dtype=np.uint8)
print(testarray)

#draw black and white array to screen with x,y being testarray[y][x]