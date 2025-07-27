# setup world type variables to be used across many files
# variables such as world size will be held here

scale = 25 #scale for perlin noise grid, scale is how many samples per grid square
scale1d = 15

# note: terraria defines much larger world sizes, which I may add in the future
# https://terraria.fandom.com/wiki/World_size
worldrows, worldcols = 300, 300 # it appears that in some cases worldcols is used for rows, and vice versa
# I would just recommend using square worlds. theres no reason not to, and theres no chance of crashing due to this bug
# yes, at some point I'll fix it 

vectorgridrows, vectorgridcols = worldrows, worldcols

tilesize = 25 # square
gamestate = 'worldgen' #game state can be 'title', 'worldgen', 'game'