import pygame
from setting import *
from player import player


class Tile(pygame.sprite.Sprite):
    # pos for position of the tile, group for the type of sprite (e.g obstacle or visible)
    def __init__(self,pos,groups):
        super().__init__(groups); # initialises getting the inheritance from sprite.Sprite
        self.image = pygame.image.load("assets/tree.png").convert_alpha() #apprently using this for every image load improves performance
        self.rect = self.image.get_rect(bottomleft = pos)

class level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface();
        # grouping the sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map();
    
    def create_map(self):
        # looping through each element in the world map
        for row_i,row in enumerate(world_map):
            for col_i, col in enumerate(row):
                # calculating world pos 
                x = col_i * TILESIZE
                y = row_i *TILESIZE
                if x == 0 and y == 0:
                    # (0,0) - pos of the map | [visi_sprites] - placing player into this group | self.obs_sprite - giving player this property
                    self.player = player((0,0),[self.visible_sprites],self.obstacle_sprites)
                if col == 'T':
                    # this puts a sprite on elements 'T' and putting it into both the groups
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])




    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()

