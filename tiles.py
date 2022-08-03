import pygame

# this class will aslo handle sprites
# sprites are seperated into two groups: visible sprites (those that are drawn onto screen), obstacle sprites (sprites that player and mobs collide with)

class level:
    def __init__(self):
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
