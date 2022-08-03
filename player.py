import pygame
import random

class player(pygame.sprite.Sprite):
    def __init__(self,pos,group,img):
        super().__init__(group)
        self.img = img;
        self.rect = self.img.get_rect(topleft = pos)

    def movementhandler(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            self.pos[0] += 5
        if keys[pygame.K_UP]:
            self.pos[1] -= 5
        if keys[pygame.K_DOWN]:
            self.pos[1] += 5

class mob:
        pass
    
        
    





