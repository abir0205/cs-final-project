import pygame
import sys
import random
import finch_icon
import shrubs
import button
import option
import mainscreen
import recthealth
import results
import tree
import ground
import bird_menu
import river
import gameover
import instruction

class Environment(pygame.sprite.Sprite):

	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.myfont = pygame.font.SysFont("Droid Sarif", 24)
		self.screen = pygame.display.set_mode((800, 600))
		"""Setting up our screens"""
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.mainscreen = mainscreen.mainScreen()
		self.scenery = pygame.image.load('assets/scene.png').convert_alpha()
		self.scenery = pygame.transform.scale(self.scenery, (800,600))



		"""Load our sprites: Finch_icon, shrubs, tree, ground, river"""

		self.shrubs = shrubs.Shrubs((257,309),'assets/shrubs.png')
		self.shrubs.used = False
		self.tree = tree.Tree((624,0), 'assets/tree.png')
		self.tree.used = False
		self.ground = ground.Ground((571, 359), 'assets/ground.png')
		self.ground.used = False
		self.river = river.River((0, 444), 'assets/river1.png')
		self.river.used = False
		self.base = 'assets/Bases/base.png'
		self.add = ''
		self.beak = 'assets/beak.png'
		self.game_end = False
		self.finch = finch_icon.Finch2((60,200),'assets/finch.png')


		"""This is the initial health bar"""
		self.x = 30


		self.source = pygame.sprite.Group()
		"""Self.source is the group of sprites that the finch can collide with to search for different sources of food. Under here is shrubs, trees, rivers, ground"""
		self.source.add(self.shrubs)
		self.tree_source = pygame.sprite.Group()
		self.tree_source.add(self.tree)
		self.ground_source = pygame.sprite.Group()
		self.ground_source.add(self.ground)
		self.river_source = pygame.sprite.Group()
		self.river_source.add(self.river)
		"""Grouping all sprites for usability purposes"""
		self.all_sprites = pygame.sprite.Group()
		self.all_sprites.add(self.finch,self.shrubs,self.tree,self.ground, self.river)

		"""Setting up all of our buttons. The .used function is to turn the buttons on or off for the food options."""

		self.finchdisplay1 = button.Button(400,200,(100,0), "Tasty Insects Near the Roots", (40, 75), (0,0,250))
		self.finchdisplay1.used = False
		self.finchdisplay2 = button.Button(400,200,(100,200), "Leaves on the Top Look Delicious", (40, 75), (0,0,250))
		self.finchdisplay2.used = False
		self.finchdisplay3 = button.Button(400,200,(100,400), "Eat the Juicy Small Red Berries", (40, 75), (0,0,250))
		self.finchdisplay3.used = False
		self.finchdisplay4 = button.Button(400,200,(100,0), "Eat the Small Leaves on Branches", (40, 75), (0,0,250))
		self.finchdisplay4.used = False
		self.finchdisplay5 = button.Button(400,200,(100,200), "Eat the Seeds Hanging off the Trees", (40, 75), (0,0,250))
		self.finchdisplay5.used = False
		self.finchdisplay6 = button.Button(400,200,(100,400), "Eat the Insects in the Bark", (40, 75), (0,0,250))
		self.finchdisplay6.used = False
		self.finchdisplay7 = button.Button(400,200,(100,0), "You see a Small Fish by the Surface...", (40, 75), (0,0,250))
		self.finchdisplay7.used = False
		self.finchdisplay8 = button.Button(400,200,(100,200), "Go for the Insects and Grubs near the bank", (40, 75), (0,0,250))
		self.finchdisplay8.used = False
		self.finchdisplay9 = button.Button(400,200,(100,400), "Bushes with Yellow Berries grow nearby", (40, 75), (0,0,250))
		self.finchdisplay9.used = False
		self.finchdisplay10 = button.Button(400,200,(100,0), "There are Insects and Grubs in some Red Clay", (40, 75), (0,0,250))
		self.finchdisplay10.used = False
		self.finchdisplay11 = button.Button(400,200,(100,200), "There are Seeds Lying Around", (40, 75), (0,0,250))
		self.finchdisplay11.used = False
		self.finchdisplay12 = button.Button(400,200,(100,400), "Use Mud to make Ground Nests", (40, 75), (0,0,250))
		self.finchdisplay12.used = False



	def mainLoop2(self):
		attack = random.randrange(1,6)
		"""This is our attack variable, a random variable that occurs throughout the game resulting in health loss"""

		pygame.key.set_repeat(1,50)
		while True:
			"""Setting up our environment screen"""
			self.background.fill((200, 250, 100))
			self.screen.blit(self.background, (0, 0))
			self.screen.blit(self.scenery, (0, 0))
			self.all_sprites.draw(self.screen)
			self.pop_Health = recthealth.PopulationHealth(self.x,50,(25,25),0,0,100)
			self.screen.blit(self.pop_Health.health, (25,20))
			""" ^ Health Bar on screen """

			self.pop_health_txt = self.myfont.render("Current Population Health: " + str(self.x), 1, (255,255,255))
			self.health_instruction = self.myfont.render("Full Evolution: 100    Extinction: 0", 1, (255,255,255))
			self.bird_instruction = self.myfont.render("Use the Directional Keys to Move Bird", 1, (255,255,255))
			self.menu_instruction = self.myfont.render("Press E to View Current Bird Evolution", 1, (255,255,255))
			self.blurb_instruction = self.myfont.render("Press I to View Game Description", 1, (255,255,255))
			self.screen.blit(self.health_instruction, (25, 75))
			self.screen.blit(self.pop_health_txt, (25, 100))
			self.screen.blit(self.bird_instruction, (25, 125))
			self.screen.blit(self.menu_instruction, (25, 150))
			self.screen.blit(self.blurb_instruction, (25, 175))
			""" ^ Health Bar and Instruction Text on screen """


			if (self.x <= 0 and not self.game_end):
				self.x == 0
				print("Done extinct now")
				self.lost = gameover.End_Results()
				self.lost.end_result_loop("Sorry fren, You Been Exctincted", "Population Health = " + str(self.x), self.base, self.add, self.beak)
				self.game_end = True
			if (self.x >= 100 and not self.game_end):
				print("Fuck yeah bean")
				self.won = gameover.End_Results()
				self.won.end_result_loop("Congratulations! You Evolved", "Population Health = " + str(self.x), self.base, self.add, self.beak)
				self.game_end = True

				"""This makes it so that if population health = 100, the Game is Over and it prompts the game over screen. Same goes for health = 0 but for the extinction screen"""




			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				"""This is for finch movement, called upon in the finch_icon class"""
				if event.type == pygame.KEYDOWN:
					if(event.key == pygame.K_UP):
						self.finch.move_up()
					elif(event.key == pygame.K_DOWN):
						self.finch.move_down()
					elif(event.key == pygame.K_LEFT):
						self.finch.move_left()
					elif(event.key == pygame.K_RIGHT):
						self.finch.move_right()
					elif(event.key == pygame.K_e):
						self.bird_menu = bird_menu.Bird_Menu(self.base, self.add, self.beak)
						self.bird_menu.loop()
					elif(event.key == pygame.K_i):
						self.instruct = instruction.Instruction()
						self.instruct.word_screen()
					elif(event.key == pygame.K_BACKSPACE):
						sys.exit()



			"""These are the main functions of the game. I'll go through just the shrub collision to demonstrate what each action does."""
			shrub_source = pygame.sprite.spritecollide(self.finch, self.source, False)
			"""This detects the collision. The .used function is used to kill the sprite upon choosing an option."""
			if(shrub_source and not self.shrubs.used):
				"""Upon colliding, the buttons pop up on the screen, and the .hover options show that the mouse is hovering over the button."""
				self.screen.blit(self.finchdisplay1.button, (200,0))
				self.screen.blit(self.finchdisplay2.button, (200,200))
				self.screen.blit(self.finchdisplay3.button, (200,400))
				self.finchdisplay1.hover()
				self.finchdisplay2.hover()
				self.finchdisplay3.hover()
				"""If the button is clicked, three options can happen. First, the .used function for the button runs through to see if a previous evolution decision keeps the finch from being able to choose this option. If so, it loads a json file that dictates the evolution does not allow this option. Second, we check if the attack variable occurs. Third, our main result occurs, and upon doing so nulls other options from being able to be chosen based on the evolution decision and takes you to a screen telling you what occurs. This repeats for each button."""
				if self.finchdisplay1.clicked():
					if self.finchdisplay1.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 30
						self.shrubs.used = True
						self.results = results.Results('jsons/storm.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/narrow beak.png'
						self.finchdisplay5.used = True
						self.finchdisplay9.used = True
						self.finchdisplay11.used = True
						self.shrubs.used = True
						self.results = results.Results('jsons/narrow.json')
						self.results.result_loop()
				if self.finchdisplay2.clicked():
					if self.finchdisplay2.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					else:
						self.x += 15
						self.add = 'assets/Wings/greenwing.png'
						self.shrubs.used = True
						self.results = results.Results('jsons/leaves.json')
						self.results.result_loop()

				if self.finchdisplay3.clicked():
					if self.finchdisplay3.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.shrubs.used = True
						self.results = results.Results('jsons/poison.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/big beak.png'
						self.add = 'assets/Wings/wing1.png'
						self.shrubs.used = True
						self.finchdisplay6.used = True
						self.finchdisplay7.used = True
						self.finchdisplay8.used = True
						self.finchdisplay10.used = True
						self.results = results.Results('jsons/berries.json')
						self.results.result_loop()


			tree_source = pygame.sprite.spritecollide(self.finch, self.tree_source, False)
			if(tree_source and not self.tree.used):
				self.screen.blit(self.finchdisplay4.button, (200,0))
				self.screen.blit(self.finchdisplay5.button, (200,200))
				self.screen.blit(self.finchdisplay6.button, (200,400))
				self.finchdisplay4.hover()
				self.finchdisplay5.hover()
				self.finchdisplay6.hover()
				if self.finchdisplay4.clicked():
					if self.finchdisplay4.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.tree.used = True
						self.results = results.Results('jsons/predator.json')
						self.results.result_loop()
					else:
						self.x += 15
						self.add = 'assets/Wings/greenwing.png'
						self.tree.used = True
						self.results = results.Results('jsons/leaves.json')
						self.results.result_loop()
				if self.finchdisplay5.clicked():
					if self.finchdisplay5.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 30
						self.tree.used = True
						self.results = results.Results('jsons/storm.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/big beak.png'
						self.base = 'assets/Bases/brownbase.png'
						self.finchdisplay1.used = True
						self.finchdisplay7.used = True
						self.finchdisplay8.used = True
						self.finchdisplay10.used = True
						self.tree.used = True
						self.results = results.Results('jsons/bigbeak.json')
						self.results.result_loop()
				if self.finchdisplay6.clicked():
					if self.finchdisplay6.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.tree.used = True
						self.results = results.Results('jsons/predator.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/narrow beak.png'
						self.base = 'assets/Bases/brownbase.png'
						self.finchdisplay3.used = True
						self.finchdisplay5.used = True
						self.finchdisplay9.used = True
						self.finchdisplay11.used = True
						self.tree.used = True
						self.results = results.Results('jsons/narrow.json')
						self.results.result_loop()


			ground_source = pygame.sprite.spritecollide(self.finch, self.ground_source, False)
			if(ground_source and not self.ground.used):
				self.screen.blit(self.finchdisplay7.button, (200,0))
				self.screen.blit(self.finchdisplay8.button, (200,200))
				self.screen.blit(self.finchdisplay9.button, (200,400))
				if self.finchdisplay7.clicked():
					if self.finchdisplay7.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.ground.used = True
						self.results = results.Results('jsons/predator.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/narrow beak.png'
						self.base = 'assets/Bases/redbase.png'
						self.finchdisplay3.used = True
						self.finchdisplay5.used = True
						self.finchdisplay11.used = True
						self.ground.used = True
						self.results = results.Results('jsons/narrow.json')
						self.results.result_loop()
				if self.finchdisplay8.clicked():
					if self.finchdisplay8.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.ground.used = True
						self.results = results.Results('jsons/predator.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/big beak.png'
						self.finchdisplay3.used = True
						self.finchdisplay5.used = True
						self.finchdisplay11.used = True
						self.ground.used = True
						self.results = results.Results('jsons/bigbeak.json')
						self.results.result_loop()
				if self.finchdisplay9.clicked():
					if self.finchdisplay9.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.ground.used = True
						self.results = results.Results('jsons/predator.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.base = 'assets/Bases/brownbase.png'
						self.finchdisplay1.used = True
						self.finchdisplay6.used = True
						self.finchdisplay10.used = True
						self.ground.used = True
						self.results = results.Results('jsons/ground.json')
						self.results.result_loop()


			river_source = pygame.sprite.spritecollide(self.finch, self.river_source, False)
			if(river_source and not self.river.used):
				self.screen.blit(self.finchdisplay10.button, (200,0))
				self.screen.blit(self.finchdisplay11.button, (200,200))
				self.screen.blit(self.finchdisplay12.button, (200,400))
				if self.finchdisplay10.clicked():
					if self.finchdisplay10.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 30
						self.river.used = True
						self.results = results.Results('jsons/storm.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/narrow beak.png'
						self.finchdisplay3.used = True
						self.finchdisplay5.used = True
						self.finchdisplay9.used = True
						self.river.used = True
						self.results = results.Results('jsons/narrow.json')
						self.results.result_loop()
				if self.finchdisplay11.clicked():
					if self.finchdisplay11.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.river.used = True
						self.results = results.Results('jsons/predator.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.beak = 'assets/big beak.png'
						self.add = 'assets/Wings/bluewing.png'
						self.finchdisplay1.used = True
						self.finchdisplay7.used = True
						self.finchdisplay8.used = True
						self.finchdisplay6.used = True
						self.river.used = True
						self.results = results.Results('jsons/bigbeak.json')
						self.results.result_loop()
				if self.finchdisplay12.clicked():
					if self.finchdisplay12.used:
						self.results = results.Results('jsons/nope.json')
						self.results.result_loop()
					elif attack == 1:
						self.x -= 15
						self.river.used = True
						self.results = results.Results('jsons/poison.json')
						self.results.result_loop()
					else:
						self.x += 30
						self.base = 'assets/Bases/yellowbase.png'
						self.river.used = True
						self.results = results.Results('jsons/berries.json')
						self.results.result_loop()




			if (self.shrubs.used == True and self.tree.used == True and self.ground.used == True and self.river.used == True):
				self.lost = gameover.End_Results()
				self.lost.end_result_loop("All Options Extinguished. Game Over!", "Population Health = " + str(self.x), self.base, self.add, self.beak)
				self.game_end = True

				"""If all Sprite Options are Extinguished, the game ends. Otherwise you would just move around with nothing to do/interact with"""

			pygame.display.flip()
