import pygame
import os
import random
from screeninfo import get_monitors
from main import player

FPS = 165
WIDTH = [i.width for i in get_monitors()][-1]
HEIGHT = [i.height for i in get_monitors()][-1]
WIN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Survival Game")



player = player(pygame.image.load("assets/player.png"))

def main():
    second = 0  # Time

    while True:
        keys = pygame.key.get_pressed()
        pygame.time.Clock().tick(FPS)  # Caps framerate
        second += 1 / FPS  # Keeps track of time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        WIN.fill((255,255,255))
        WIN.blit(player.img,player.pos)
        player.movementhandler(keys)

        pygame.display.update()

if __name__ == "__main__":
    main()
