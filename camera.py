import pygame

class Ycamerasort(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,200);
        self.half_width = self.surface.get_size()[0] // 2
        self.half_height = self.surface.get_size()[1] // 2
    def customDraw(self,player):

        # player cam offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # magic to render which sprite should be on top
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): 
            offset_pos = sprite.rect.topleft - self.offset
            self.surface.blit(sprite.image, offset_pos)