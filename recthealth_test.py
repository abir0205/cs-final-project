import pygame
import sys
import recthealth

def main():
	health = recthealth.PopulationHealth(25, 25, (25,25), 0,0,0)
	"""This gives us location coords"""
	print(health.rect.x)
	print(health.rect.y)
	"""This gives us width and height"""
	print(health.width)
	print(health.height)
main()
