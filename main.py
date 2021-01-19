#import your controller
import sys
import pygame
import shrubs
import finch_icon
import environment
import mainscreen
import button
import results
import controller

def main():
	pygame.init()
	main_window = controller.Controller()
	main_window.mainLoop()
	#Create an instance on your controller object
main()
