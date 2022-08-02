import pygame

class player:
    def __init__(self,img):
        self.img = img;
        self.x = 0
        self.y = 0
        self.pos = [self.x,self.y]

    def movementhandler(self,keys):
        if keys[pygame.K_LEFT]:
            self.pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            self.pos[0] += 5
        if keys[pygame.K_UP]:
            self.pos[1] -= 5
        if keys[pygame.K_DOWN]:
            self.pos[1] += 5

class mob:
    def __init__(self,img):
        self.img = img
        self.pos = [100,100]
    
        
    





