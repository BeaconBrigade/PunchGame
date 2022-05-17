# Handle Game

import pygame
from display import initGui, destGui

print("Game logic works")

# Array to store io events
ioevents = []
trackEvents = True

from handleio import checkInputs, ledOutput

def gameLoop() :
	""" The main game loop! """
	pygame.init()
	destGui()
	
	screen = pygame.display.set_mode((800, 450))
	pygame.display.set_caption("Punch Game!")
	background = pygame.image.load("resource/mortal.png")
	
	running = True

	# Main game loop
	while running :
		checkInputs()
		screen.fill("white")
		screen.blit(background, (0, 0))

		for event in pygame.event.get() :
			print("hi")

		pygame.display.update()

	# Close game loop
	initGui()
	trackEvents = False
