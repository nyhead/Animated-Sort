import pygame
from sorting_algorithms import *
import model
import view
from pygame.locals import *

running = True

game_model = model.Game()
graphics = view.View(game_model)

graphics.initialize()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    choice = graphics.intro()

    if choice == "BUBBLE":
        print("Bubble")
        graphics.screen.fill(graphics.BLACK)
        bubble_sort(game_model.a)
    elif choice == "SELECTION":
        graphics.screen.fill(graphics.BLACK)
        print("Selection")
        selection_sort(game_model.a)
    elif choice == "INSERTION":
        graphics.screen.fill(graphics.BLACK)
        print("Insertion")
        insertion_sort(game_model.a)

    pygame.display.update()
    graphics.clock.tick(60)

pygame.quit()