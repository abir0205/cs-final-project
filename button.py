import pygame
import sys
import galapagos
import shrubs
import finch_icon
import environment
import mainscreen
import results
import bird_menu


class Button:

	def __init__(self, w, h, location, text, text_location, color):
		"""Creates the rectangle for the button and fills it with initial color, and sets its location"""
		self.myfont = pygame.font.SysFont("Times New Roman", 18)
		self.scroll = pygame.image.load('assets/scroll.jpg').convert_alpha()
		self.scroll = pygame.transform.scale(self.scroll, (400,200))
		self.width = w
		self.height = h
		self.text = text
		self.text_location = text_location
		self.button = pygame.Surface((self.width,self.height))
		self.color = color
		self.button.fill(self.color)
		self.prompt = self.myfont.render(self.text, 1, (0,0,0))
		self.button.blit(self.scroll,(0,0))
		self.button.blit(self.prompt, (self.text_location))
		self.rect = self.button.get_rect()
		self.rect.x, self.rect.y = location		

	def hover(self):
		mouse = pygame.mouse.get_pos()
		if int(self.rect.x)+self.width > mouse[0] > int(self.rect.x) and int(self.rect.y)+self.height > mouse[1] > int(self.rect.y):
			self.button.blit(self.scroll,(0,0))
			self.button.fill((15,255,200))
			self.prompt = self.myfont.render(self.text, 1, (0,0,0))
			self.button.blit(self.prompt, (self.text_location))
			return True	
		else:
			self.button.fill(self.color)
			self.button.blit(self.scroll,(0,0))
			self.prompt = self.myfont.render(self.text, 1, (0,0,0))
			self.button.blit(self.prompt, (self.text_location))
			return False
	def clicked(self):
		if (self.hover()):
			mouse = pygame.mouse.get_pos()
			self.click = pygame.mouse.get_pressed()
			return self.click[0] == 1
		return False
