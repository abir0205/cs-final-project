#import your controller
import sys
import pygame
import galapagos
import shrubs
import finch_icon
import environment

class mainScreen:
	def __init__(self):
		pygame.init()
		self.myfont = pygame.font.SysFont("Calibri", 36)
		self.screen = pygame.display.set_mode((800, 600))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		"""Load the sprites"""
		self.galapagos = galapagos.Galapagos((0,0),'assets/Galap.jpg')
		self.screen.blit(self.galapagos.image, self.galapagos.rect)
		self.welcome = self.myfont.render("Welcome to the Galapagos!", 1, (0,0,0))
		self.welcome_2 = self.myfont.render("Good Luck on Your Explorations...", 1, (0,0,0))
		self.prompt = self.myfont.render("(Press SPACEBAR to Continue)", 1, (0,0,0))
		self.screen.blit(self.welcome, (400,5))
		self.screen.blit(self.welcome_2, (125,375))
		self.screen.blit(self.prompt, (125,400))





	"""def mainLoop(self):
		pygame.key.set_repeat(1,50)
		while True:
			self.envi = None
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if(event.key == pygame.K_9):
						self.envi = environment.Environment()
						self.envi.mainLoop2()
			pygame.display.flip()
	"""
