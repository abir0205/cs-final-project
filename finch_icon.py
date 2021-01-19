import pygame
import sys

class Finch2(pygame.sprite.Sprite):

	def __init__(self, location, img_file):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).convert_alpha()
		self.image = pygame.transform.scale(self.image, (82,82))
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = location
		self.speed = 14

	def y_coord(self):
		return self.rect.y
	def x_coord(self):
		return self.rect.x

	def move_up(self):
		self.rect.y -= self.speed
	def move_down(self):
		self.rect.y += self.speed
	def move_left(self):
		self.rect.x -= self.speed
	def move_right(self):
		self.rect.x += self.speed
