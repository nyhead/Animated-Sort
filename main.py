from sorting_algorithms import *
import model
import view
from pygame.locals import *

running = True

data_model = model.Data()
graphics = view.View(data_model)

graphics.initialize()
choice = ''

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    choice = graphics.intro()
    graphics.screen.fill(graphics.WHITE)

    print(choice)
    graphics.show_array()
    pygame.time.wait(1000)
    if choice == "BUBBLE":
        bubble_sort(graphics, data_model)
    elif choice == "SELECTION":
        selection_sort(graphics, data_model)
    elif choice == "INSERTION":
        insertion_sort(graphics, data_model)

    data_model.generate_unsorted_array()

    graphics.screen.fill(graphics.WHITE)
    graphics.clear_arr(CLEAR_COLOR=True)

    pygame.display.update()
    graphics.clock.tick(data_model.FPS)

    choice = ''

pygame.quit()
