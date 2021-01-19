import pygame

class Galapagos(pygame.sprite.Sprite):

	def __init__(self, location, img_file):
		pygame.init()
		self.image = pygame.image.load(img_file).convert_alpha()
		self.image = pygame.transform.scale(self.image, (800, 600))
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
