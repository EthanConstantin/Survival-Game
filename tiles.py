import pygame
from setting import *
from player import player
from camera import Ycamerasort
from debug import debug

class Tile(pygame.sprite.Sprite):
    # pos for position of the tile, group for the type of sprite (e.g obstacle or visible)
    def __init__(self,pos,groups):
        super().__init__(groups); # initialises getting the inheritance from sprite.Sprite
        self.image = pygame.image.load("assets/tree.png").convert_alpha() #apprently using this for every image load improves performance
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30,-30)
        self.hitbox.y += 10


class level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface();
        # grouping the sprites
        self.visible_sprites = Ycamerasort()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map();
    
    def create_map(self):
        self.player = player((3168,3168),[self.visible_sprites],self.obstacle_sprites)
        # looping through each element in the world map
        for row_i,row in enumerate(world_map):
            for col_i, col in enumerate(row):
                # calculating world pos 
                x = col_i * TILESIZE
                y = row_i *TILESIZE
                if col == 'T':
                    # this puts a sprite on elements 'T' and putting it into both the groups
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites])



    def run(self):
        self.visible_sprites.customDraw(self.player)
        self.visible_sprites.update()
        #debug(str(self.player.rect.x),str(self.player.rect.y))


