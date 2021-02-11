import pygame
from pygame.locals import *

def bubble_sort(graphics, model):
    a = model.a
    n = len(a)
    arr_elem = graphics.arr_elem
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                graphics.slide_two_elements(arr_elem[j], arr_elem[j+1])
                a[j], a[j + 1] = a[j + 1], a[j]
                # arr_elem[j], arr_elem[j + 1] = arr_elem[j + 1], arr_elem[j]
            # graphics.show_array()
            graphics.clear_arr()
            graphics.initiate_event_loop()
        arr_elem[i].border_color = graphics.BLACK
    # graphics.screen.fill(graphics.WHITE)
    # graphics.show_array()
    graphics.initiate_event_loop()

def selection_sort(graphics, model):
    a = model.a
    arr_elem = graphics.arr_elem
    n = len(a)
    for i in range(n):
        min_index = i
        min_val = a[i]
        for j in range(i + 1, n):
            prev_color_j = arr_elem[j].border_color
            prev_color_min = arr_elem[min_index].border_color
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
            if prev_color_j != graphics.GREEN: arr_elem[j].border_color = graphics.BLUE
            if prev_color_min != graphics.GREEN: arr_elem[min_index].border_color = graphics.RED

            graphics.show_array()
            graphics.screen.fill(graphics.WHITE)
            arr_elem[j].border_color, arr_elem[min_index].border_color = prev_color_j, prev_color_min
            graphics.initiate_event_loop()

        a[i], a[min_index] = a[min_index], a[i]
        arr_elem[i].border_color = graphics.GREEN
        graphics.show_array()
        graphics.screen.fill(graphics.WHITE)
        graphics.initiate_event_loop()
    graphics.show_array()
    graphics.initiate_event_loop()


def insertion_sort(graphics, model):
    a = model.a
    arr_elem = graphics.arr_elem
    n = len(a)

    for i in range(n):
        graphics.initiate_event_loop()
        t = a[i]
        j = i - 1
        init = (arr_elem[j].x, arr_elem[j].y)
        if t < a[j]:
            graphics.slide_up(i)
            returned = graphics.slide_right(j, t)
            graphics.slide_in(t, arr_elem[i].x, arr_elem[i].y, returned[0], returned[1])
        graphics.clear_arr()
        # variable_j = graphics.slide_right(j, t)
        # if t < a[j]:
        #     print()
        #     # arr_elem[j+1].x, arr_elem[j+1].y = init[0], init[1]
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]
            # graphics.slide_right(arr_elem[j].x, arr_elem[j+1].x)
            # arr_elem[j+1] = arr_elem[j]

            graphics.initiate_event_loop()
            j -= 1
        a[j + 1] = t

        # if t < a[i]:
        #     print()
        #     # arr_elem[j+1].x, arr_elem[j+1].y = init[0], init[1]
        #     graphics.slide_in(t, arr_elem[i].x, arr_elem[i].y, init[0], init[1])
        #     graphics.initiate_event_loop()
        graphics.initiate_event_loop()