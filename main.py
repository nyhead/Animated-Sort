import pygame
from sorting_algorithms import *
import model
import view
from pygame.locals import *

running = True

game_model = model.Game()
graphics = view.View(game_model)

graphics.initialize()

choice = graphics.intro()
while running:
    graphics.screen.fill(graphics.WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if choice != None:
        print(choice)
        graphics.show_array()
        pygame.time.wait(1000)
        if choice == "BUBBLE":
            bubble_sort(graphics, game_model)
        elif choice == "SELECTION":
            selection_sort(graphics, game_model)
        elif choice == "INSERTION":
            insertion_sort(graphics, game_model)
        choice = ''
    else:
        choice = graphics.intro()

    pygame.display.update()
    graphics.clock.tick(game_model.FPS)

pygame.quit()
