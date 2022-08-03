import pygame

pygame.font.init()
def debug(*args):
    display_surface = pygame.display.get_surface()
    font = pygame.font.SysFont('Comic Sans MS',30)
    text_surface = font.render(str(args),False,(0,0,0))
    display_surface.blit(text_surface,(0,0))
