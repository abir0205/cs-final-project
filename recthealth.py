import sys
import pygame
import galapagos
import shrubs
import finch_icon
import button
import results
import environment
import mainscreen


""" Sets up health bar at top of screen """
""" Changes in length based on event occurances """ 


class PopulationHealth:

	def __init__(self, w, h, location, r,b,g):
		self.width = w
		self.height = h
		self.health = pygame.Surface((self.width,self.height))
		self.health.fill((r,g,b))
		self.rect = self.health.get_rect()
		self.rect.x, self.rect.y = location
