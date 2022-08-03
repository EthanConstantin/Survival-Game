import pygame
from setting import *



class Tile(pygame.sprite.Sprite):
    # pos for position of the tile, group for the type of sprite (e.g obstacle or visible)
    def __init__(self,pos,groups):
        super().__init__(groups); # initialises getting the inheritance from sprite.Sprite
        self.image = pygame.image.load("assets/tree.png").convert_alpha() #apprently using this for every image load improves performance
        self.rect = self.image.get_rect(topleft = pos)

class level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface();
        # grouping the sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map();
    
    def create_map(self):
        for row_i,row in enumerate(world_map):
            for col_i, col in enumerate(row):
                x = col_i * TILESIZE
                y = row_i *TILESIZE
                if col == 'T':
                    Tile((x,y),[self.visible_sprites])


    def run(self):
        self.visible_sprites.draw(self.display_surface)


