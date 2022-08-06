import pygame
import random
from debug import debug

class player(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacle_sprites):
        super().__init__(group)
        self.image = pygame.image.load("assets/player.png").convert_alpha();
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-20)
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
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: 
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacleSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def move(self,speed):
      self.hitbox.y += self.direction.y * speed
      self.collision('vertical')
      self.hitbox.x += self.direction.x *speed
      self.collision('horizontal')
      self.rect.center = self.hitbox.center
      
    def update(self):
        self.movementhandler()
        self.move(self.speed)