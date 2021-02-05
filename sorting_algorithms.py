import view
import pygame

def bubble_sort(a, graphics, model):
    n = len(a)
    arr_elem = model.arr_elem
    graphics.show_array()
    graphics.clear_arr()
    pygame.display.update()
    pygame.time.wait(1000)
    for i in range(n - 1, 0, -1):   # n - 1 .. 1
        # arr_elem[i].border_color = graphics.BLACK
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                # arr_elem[j], arr_elem[j + 1] = arr_elem[j + 1], arr_elem[j]

                graphics.show_array()
                graphics.clear_arr()
                pygame.display.update()
                pygame.time.wait(1000)

                # print(a)

def selection_sort(a):
    pass

def insertion_sort(a):
    pass
