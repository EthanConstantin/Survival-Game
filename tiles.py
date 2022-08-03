import pygame
from setting import world_map
# this class will aslo handle sprites
# sprites are seperated into two groups: visible sprites (those that are drawn onto screen), obstacle sprites (sprites that player and mobs collide with)

class level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface();
        # grouping the sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map();
    
    def create_map(self):
        for row in world_map:
            print(row)

    def run():
        pass
