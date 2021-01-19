import pygame
import sys


class Instruction:
    def __init__(self):
        pygame.init()
        self.myfont = pygame.font.SysFont("Times New Roman", 24)
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.returns = self.myfont.render("(Press R to Return)", 1, (0,0,0))
        self.instruct1 = self.myfont.render("Welcome to the Evolution Game!", 1, (0,0,0))
        self.instruct2 = self.myfont.render("Here, you will play as a finch surviving on the Galapagos islands.", 1, (0,0,0))
        self.instruct3 = self.myfont.render("In the game you will search for food sources by moving the finch around", 1, (0,0,0))
        self.instruct4 = self.myfont.render("the environment and choosing food options in those sources.", 1, (0,0,0))
        self.instruct5 = self.myfont.render("The point of the game is to bare-bones simulate evolution.", 1, (0,0,0))
        self.instruct7 = self.myfont.render("Obtain a Population Health of 100 to fully evolve.", 1, (0,0,0))
        self.instruct8 = self.myfont.render("A Population Health of zero means you went extinct! Choose wisely... ", 1, (0,0,0))
        self.instruct9 = self.myfont.render("Click on the options with your mouse to select them", 1, (0,0,0))

        self.instruct6 = self.myfont.render("(Press R to return)", 1, (0,0,0))


	

    def word_screen(self):
        pygame.key.set_repeat(1,50)
        while True:
            self.background.fill((255, 255, 255))
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.instruct1,(25,25))
            self.screen.blit(self.instruct2, (25, 75))
            self.screen.blit(self.instruct3, (25,125))
            self.screen.blit(self.instruct4, (25, 175))
            self.screen.blit(self.instruct5, (25, 225))
            self.screen.blit(self.instruct7, (25, 250))
            self.screen.blit(self.instruct8, (25, 275))
            self.screen.blit(self.instruct9, (25, 300))
            self.screen.blit(self.instruct6, (100, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_BACKSPACE:
                        sys.exit()
                    if event.key == pygame.K_r:
                        return
            pygame.display.flip()
