import random

TILESIZE = 64

def worldmapgen():
    randnum = random.randint(1,100);
    if randnum >= 41:
        return " " # grass tile
    if randnum <= 40 and randnum >= 20:
        return "T" # tree tile
    if randnum <= 19:
        return "o" # rock

# for now, x represents a tree, blank represents grass
world_map = [[worldmapgen() for x in range(31)] for x in range(31)]

for i,v in enumerate(world_map):
    print(v)