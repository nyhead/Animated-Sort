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
        if event.type == KEYDOWN:
            game_model.FPS = 0
            # print('show array')
    if choice != None:
        # graphics.screen.fill(graphics.WHITE)
        # graphics.show_array()
        # [graphics.clock.tick(i) for i in range(3)]
        if choice == "BUBBLE":
            # print("Bubble")
            # graphics.screen.fill(graphics.BLACK)
            bubble_sort(game_model.a, graphics, game_model)
            choice = ''
            # print(game_model.a)
        elif choice == "SELECTION":
            # graphics.screen.fill(graphics.BLACK)
            # print("Selection")
            selection_sort(game_model.a)
        elif choice == "INSERTION":
            # graphics.screen.fill(graphics.BLACK)
            # print("Insertion")
            insertion_sort(game_model.a)
    else:
        choice = graphics.intro()

    pygame.display.update()
    graphics.clock.tick(game_model.FPS)

pygame.quit()