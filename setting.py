import random

TILESIZE = 64

def worldmapgen():
    randnum = random.randint(1,100);
    if randnum >= 41:
        return " " # grass tile
    if randnum <= 40 and randnum >= 20:
        return "T" # tree tile
    if randnum <= 19:
        pass#return "o" # rock

# for now, x represents a tree, blank represents grass
# each element is a tile in the game
# each tile has a size of 64
# this can be put into coordinates; the topleft tile would be (0,0), the one to the right would be (0,64)
world_map = [[worldmapgen() for x in range(100)] for x in range(100)]

#for i,v in enumerate(world_map):
#    print(v)