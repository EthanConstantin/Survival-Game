import pygame
import os
import random
from screeninfo import get_monitors
from player import player,mob

#FPS = 165
#WIDTH = [i.width for i in get_monitors()][-1]
#HEIGHT = [i.height for i in get_monitors()][-1]
#WIN = pygame.display.set_mode((1280, 720))
#pygame.display.set_caption("Survival Game")

# using OOP to make it easier to manage
class Game():
    def __init__(self) -> None:
        self.FPS = 165;
        self.WIDTH = WIDTH = [i.width for i in get_monitors()][-1]
        self.HEIGHT = [i.height for i in get_monitors()][-1]
        self.WIN = pygame.display.set_mode((1280, 720)) # test resolution will be changed later
        pygame.display.set_caption("Survival Game")
        self.player = player(pygame.image.load("assets/player.png"))

    def run(self):

        while True:
         keys = pygame.key.get_pressed()
         pygame.time.Clock().tick(self.FPS)  # Caps framerate
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            self.WIN.fill((255,255,255))
            self.WIN.blit(self.player.img,self.player.pos)
            self.player.movementhandler(keys)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
