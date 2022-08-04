import pygame
import random
from debug import debug

class player(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacle_sprites):
        super().__init__(group)
        self.image = pygame.image.load("assets/player.png").convert_alpha();
        self.rect = self.image.get_rect(topleft = pos)
        self.obstacleSprites = obstacle_sprites
        self.direction = pygame.math.Vector2()
        self.speed = 5; 

    def movementhandler(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def collision(self,direction):
        # checking for vertical and horizontal collisions
        if direction == 'horizontal':
            # loops through obs sprites because those are the ones that can collide
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: 
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: #moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: #moving up
                        self.rect.top = sprite.rect.bottom

    def move(self,speed):
      self.rect.y += self.direction.y * speed
      self.collision('vertical')
      self.rect.x += self.direction.x *speed
      self.collision('horizontal')
    def update(self):
        self.movementhandler()
        self.move(self.speed)
        # displays player coords
        debug(self.rect.x,self.rect.y)