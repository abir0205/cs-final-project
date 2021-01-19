import pygame
import sys

class Option:
		
	def __init__(self, location, text):
		pygame.init()
		pygame.font.init()
		self.myfont = pygame.font.SysFont("Times New Roman", 24)
		self.option = pygame.Surface((300,150))
		self.option.fill((100,200,150))
		self.rect = self.option.get_rect()
		self.prompt = self.myfont.render(str(text), 1, (255,255,255))
		self.option.blit(self.prompt, (location))
