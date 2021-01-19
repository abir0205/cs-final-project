import sys
import pygame
import shrubs
import finch_icon
import environment
import mainscreen
import button
import results
import controller

class Controller:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		"""Load the sprites"""



	def mainLoop(self):
		pygame.key.set_repeat(1,50)
		while True:
			self.envi = None
			self.mainscreen = mainscreen.mainScreen()
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if(event.key == pygame.K_SPACE):
						self.envi = environment.Environment()
						self.envi.mainLoop2()
			pygame.display.flip()

