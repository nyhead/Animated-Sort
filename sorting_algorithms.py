import view
import pygame


def bubble_sort(graphics, model):
    a = model.a
    n = len(a)
    arr_elem = model.arr_elem
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                graphics.slide_two_elements(arr_elem[j], arr_elem[j + 1])
                # arr_elem[j], arr_elem[j + 1] = arr_elem[j + 1], arr_elem[j]
            graphics.show_array()
            pygame.time.wait(1000)
        arr_elem[i].border_color = graphics.BLACK
        # print(a)


def selection_sort(graphics, model):
    a = model.a
    arr_elem = model.arr_elem
    n = len(a)
    for i in range(n - 1):
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
            arr_elem[j].border_color, arr_elem[min_index].border_color = prev_color_j, prev_color_min
            pygame.time.wait(1000)
        a[i], a[min_index] = a[min_index], a[i]
        arr_elem[i].border_color = graphics.GREEN
        graphics.show_array()
        pygame.time.wait(1000)


def insertion_sort(graphics, model):
    a = model.a
