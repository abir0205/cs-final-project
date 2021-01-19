import pygame
import sys
import recthealth
import bird_menu
import button
import controller


class End_Results:
	def __init__(self):
		pygame.init()
		self.myfont = pygame.font.SysFont("Times New Roman", 20)
		self.screen = pygame.display.set_mode((800, 600))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.crest = pygame.image.load('assets/results_crest.jpg').convert_alpha()
		self.crest = pygame.transform.scale(self.crest, (800,600))

	def end_result_loop(self, endresult, score, base, add, beak):
		pygame.key.set_repeat(1,50)
		while True:
			self.background.fill((200, 250, 100))
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.crest,(0,0))
			self.result = self.myfont.render(endresult, 1, (0,0,0))
			self.screen.blit(self.result, (250,300))
			self.result = self.myfont.render(score, 1, (0,0,0))
			self.screen.blit(self.result, (300,250))
			self.result_return = self.myfont.render("(Press Backspace to Exit)", 1, (0,0,0))
			self.screen.blit(self.result_return, (300,325))
			self.result_return = self.myfont.render("(Press E to view Final Evolution)", 1, (0,0,0))
			self.screen.blit(self.result_return, (300,350))
			self.result_return = self.myfont.render("(Press 1 to Play Again)", 1, (0,0,0))
			self.screen.blit(self.result_return, (300,510))


			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						self.controller = controller.Controller()
						self.controller.mainLoop()
					elif(event.key == pygame.K_BACKSPACE):
						sys.exit()
					elif(event.key == pygame.K_e):
						self.bird_menu = bird_menu.Bird_Menu(base, add, beak)
						self.bird_menu.loop()
			pygame.display.flip()
