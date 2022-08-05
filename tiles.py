import pygame
from setting import *
from player import player
from camera import Ycamerasort


class Tile(pygame.sprite.Sprite):
    # pos for position of the tile, group for the type of sprite (e.g obstacle or visible)
    def __init__(self,pos,groups):
        super().__init__(groups); # initialises getting the inheritance from sprite.Sprite
        self.image = pygame.image.load("assets/tree.png").convert_alpha() #apprently using this for every image load improves performance
        self.rect = self.image.get_rect(center = pos)

class Tile2(pygame.sprite.Sprite):
    # pos for position of the tile, group for the type of sprite (e.g obstacle or visible)
    def __init__(self,pos,groups):
        super().__init__(groups); # initialises getting the inheritance from sprite.Sprite
        self.image = pygame.transform.scale(pygame.image.load("assets/treehitbox.png").convert_alpha(), (2,18) )#apprently using this for every image load improves performance
        self.rect = self.image.get_rect(center = pos)
        self.rect.y += 15

class level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface();
        # grouping the sprites
        self.visible_sprites = Ycamerasort()
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
                    Tile((x,y),[self.visible_sprites])
                    Tile2((x,y),[self.obstacle_sprites])



    def run(self):
        self.visible_sprites.customDraw(self.player)
        self.visible_sprites.update()


