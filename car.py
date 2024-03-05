import pygame
from settings import *

class Car(pygame.sprite.Sprite):

    def __init__(self, x, y, filename,left_key,right_key):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = CAR_WIDTH
        self.speedx = CAR_SPEEDX
        self.left_key = left_key
        self.right_key = right_key

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.left_key]:
           self.rect.x -= self.speedx
        elif keys[self.right_key]:
            self.rect.x += self.speedx

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SC_WIDTH - CAR_WIDTH:
            self.rect.x = SC_WIDTH - CAR_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

