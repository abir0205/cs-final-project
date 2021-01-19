import pygame
import sys
import recthealth
import bird_menu
import button
import environment


class Results:
	def __init__(self, filename):
		pygame.init()
		self.myfont = pygame.font.SysFont("Droid Serif", 40)
		self.screen = pygame.display.set_mode((800, 600))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.crest = pygame.image.load('assets/results_crest_2.jpeg').convert_alpha()
		self.crest = pygame.transform.scale(self.crest, (800,600))
		fileref = open(filename, 'r')
		self.line1 = fileref.readline()
		self.line2 = fileref.readline()
		self.line3 = fileref.readline()


	def result_loop(self):
		pygame.key.set_repeat(1,50)
		while True:
			self.background.fill((200, 250, 100))
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.crest,(0,0))
			self.read1 = self.myfont.render(self.line1, 1, (0,0,0))
			self.read2 = self.myfont.render(self.line2, 1, (0,0,0))
			self.read3 = self.myfont.render(self.line3, 1, (0,0,0))

			self.screen.blit(self.read1, (260,200))
			self.screen.blit(self.read2, (260,250))
			self.screen.blit(self.read3, (260,300))
			self.result_return = self.myfont.render("Press R to continue", 1, (0,0,0))
			self.screen.blit(self.result_return, (260,450))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.type == pygame.K_BACKSPACE:
						sys.exit()
					if event.key == pygame.K_r:
						return
			pygame.display.flip()
