import pygame
import sys


class Bird_Menu:
    def __init__(self, base_color, add_color, beak):
        pygame.init()
        self.myfont = pygame.font.SysFont("Times New Roman", 30)
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        """Load our sprites"""
        self.base =  pygame.image.load(base_color).convert_alpha()
        self.base = pygame.transform.scale(self.base, (400,400))
        self.beak = pygame.image.load(beak).convert_alpha()
        self.beak = pygame.transform.scale(self.beak, (200,200))
        self.instruction = self.myfont.render("(Press R to Return)", 1, (0,0,0))

        try:
            self.add = pygame.image.load(add_color).convert_alpha()
            self.add = pygame.transform.scale(self.add, (400,400))
        except:
            pass

    def loop(self):
        pygame.key.set_repeat(1,50)
        while True:
            self.background.fill((200, 250, 100))
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.base, (140, 100))
            self.screen.blit(self.beak, (408,41))
            self.screen.blit(self.instruction, (300, 550))

            try:
                self.screen.blit(self.add, (128,72))
            except:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_BACKSPACE:
                        sys.exit()
                    if event.key == pygame.K_r:
                        return
            pygame.display.flip()
