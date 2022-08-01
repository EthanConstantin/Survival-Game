import pygame
import os
import random
from screeninfo import get_monitors


FPS = 165
WIDTH = [i.width for i in get_monitors()]
WIDTH = WIDTH[-1]
HEIGHT = [i.height for i in get_monitors()]
HEIGHT = HEIGHT[-1]
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Game")

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space_background.jpg")), (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(SPACE, (0, 0))

    pygame.display.update()


def main():
    second = 0  # Time

    while True:
        pygame.time.Clock().tick(FPS)  # Caps framerate
        second += 1 / FPS  # Keeps track of time
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        draw_window()

if __name__ == "__main__":
    main()