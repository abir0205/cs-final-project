import pygame
import sys
import random

class River(pygame.sprite.Sprite):

	def __init__(self, location, img_file):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).convert_alpha()
		self.image = pygame.transform.scale(self.image, (372,160))
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = location

