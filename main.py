import pygame
import os
import random
from screeninfo import get_monitors
from tiles import level


#FPS = 165
#WIDTH = [i.width for i in get_monitors()][-1]
#HEIGHT = [i.height for i in get_monitors()][-1]
#WIN = pygame.display.set_mode((1280, 720))
#pygame.display.set_caption("Survival Game")
clock = pygame.time.Clock()
# using OOP to make it easier to manage
class Game():
    def __init__(self) -> None:
        self.FPS = 60;
        self.WIDTH  = [i.width for i in get_monitors()][-1]
        self.HEIGHT = [i.height for i in get_monitors()][-1]
        self.WIN = pygame.display.set_mode((1280,720)) # test resolution will be changed later
        pygame.display.set_caption("Survival Game")
        self.Level = level()

    def run(self):
        
        while True:
         self.WIN.fill((255,255,255))
         #self.WIN.blit(pygame.transform.scale(pygame.image.load("assets/grass.png").convert_alpha(),(self.WIDTH,self.HEIGHT)), (0,0))  
         clock.tick(self.FPS)  # Caps framerate
         self.Level.run()
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0; #returning 0 means success
            if event.type == pygame.QUIT:
                raise SystemExit
         pygame.display.flip() # you can pass rectangles into this method to only update specified regions // stuff in rectangles are updated 


if __name__ == "__main__":
    game = Game()
    game.run()
