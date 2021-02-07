import pygame
import model
import random
from pygame.locals import *


class View:
    def __init__(self, model):
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.font = None
        self.width, self.height = None, None

    def initialize(self):
        result = pygame.init()
        pygame.font.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Sans-Serif", 50)
        self.BLACK, self.WHITE, self.RED, self.BLUE, self.GREEN = (0, 0, 0), (255, 255, 255), (255, 0, 0), (
        0, 0, 255), (0, 128, 0)

        center = (100, self.height / 2)
        for i in range(len(self.model.a)):
            self.model.arr_elem.append(Element(center[0] + i * 70, center[1]))

        self.isinitialized = True

    def intro(self):
        if not self.isinitialized: return

        running = True
        while running:
            self.screen.fill(self.WHITE)

            bubble_sort = self.font.render('Bubble Sort', 1, self.BLACK)
            selection_sort = self.font.render('Selection Sort(not implemented)', 1, self.BLACK)
            insertion_sort = self.font.render('Insertion Sort(not implemented)', 1, self.BLACK)
            mx, my = pygame.mouse.get_pos()

            button_bubble = pygame.rect.Rect(self.width // 2 - 150, self.height // 2 - 50, 250, 50)
            button_selection = pygame.rect.Rect(self.width // 2 - 150, self.height // 2, 400, 50)
            button_insertion = pygame.rect.Rect(self.width // 2 - 150, self.height // 2 + 50, 400, 50)

            self.screen.blit(bubble_sort, button_bubble)
            self.screen.blit(selection_sort, button_selection)
            self.screen.blit(insertion_sort, button_insertion)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if button_bubble.collidepoint((mx, my)):
                        return "BUBBLE"
                    if button_selection.collidepoint((mx, my)):
                        return "SELECTION"
                    if button_insertion.collidepoint((mx, my)):
                        return "INSERTION"
                return None

    def show_array(self):
        a = self.model.a
        center = (100, self.height / 2)
        arr_elem = self.model.arr_elem

        for i in range(len(a)):
            surf = arr_elem[i].surf
            border = arr_elem[i].border
            border_color = arr_elem[i].border_color

            text = self.font.render(str(a[i]), 1, self.BLACK)
            box = pygame.rect.Rect((border, border, 50, 50))
            pygame.draw.rect(surf, border_color, box, 1)

            surf.blit(text, (20, 15))
            self.screen.blit(surf, (arr_elem[i].x, arr_elem[i].y))

        self.clear_arr()
        pygame.display.update()

    def clear_arr(self):
        arr_elem = self.model.arr_elem
        # arr_elem.clear()
        center = (100, self.height / 2)
        for i in range(len(self.model.a)):

            arr_elem[i].surf.fill(self.WHITE)
            arr_elem[i].x, arr_elem[i].y = center[0] + i * 70, center[1]

    def slide_two_elements(self, elem1, elem2):
        left = -0.1
        right = 0.1

        init_elem1_x = elem1.x
        init_elem2_x = elem2.x

        a = self.model.a
        center = (100, self.height / 2)
        arr_elem = self.model.arr_elem

        for i in range(len(a)):
            if arr_elem[i] is elem1 and arr_elem[i + 1] is elem2:
                elem1.surf.fill(self.WHITE)
                elem2.surf.fill(self.WHITE)

                elem1.border_color = elem2.border_color = self.RED

                text1 = self.font.render(str(a[i + 1]), 1, self.BLACK)
                text2 = self.font.render(str(a[i]), 1, self.BLACK)

                while elem1.x < init_elem2_x and elem2.x > init_elem1_x:

                    elem1.x += right
                    elem2.x += left

                    pygame.draw.rect(elem1.surf, elem1.border_color, (elem1.border, elem1.border, 50, 50), 1)
                    pygame.draw.rect(elem2.surf, elem2.border_color, (elem2.border, elem2.border, 50, 50), 1)

                    elem1.surf.blit(text1, (20, 15))
                    elem2.surf.blit(text2, (20, 15))

                    self.screen.blit(elem1.surf, (elem1.x, elem1.y))
                    self.screen.blit(elem2.surf, (elem2.x, elem2.y))

                    pygame.display.update()
                elem1.border_color = elem2.border_color = self.WHITE

        self.clear_arr()
        pygame.display.update()

    def slide_up(self, source_index):

        arr_elem = self.model.arr_elem
        a = self.model.a
        elem = arr_elem[source_index]

        up = -0.5

        for i in range(len(a)):
            if i == source_index:
                elem.surf.fill(self.WHITE)

                elem.border_color = self.RED

                text = self.font.render(str(a[i]), 1, self.BLACK)

                limit_up = elem.y - 100
                while elem.y > limit_up:
                    elem.y += up

                    pygame.draw.rect(elem.surf, elem.border_color, (elem.border, elem.border, 50, 50), 1)

                    elem.surf.blit(text, (20, 15))

                    self.screen.blit(elem.surf, (elem.x, elem.y))

                    pygame.display.update()
                elem.border_color = self.WHITE

    def slide_right(self, source_x, dest_x):
        arr_elem = self.model.arr_elem
        a = self.model.a

        right = 0.5

        for i in range(len(a)):
            if arr_elem[i].x == source_x:
                elem = arr_elem[i]
                elem.surf.fill(self.WHITE)

                text = self.font.render(str(a[i]), 1, self.BLACK)

                #going up
                while elem.x < dest_x:
                    elem.x += right

                    pygame.draw.rect(elem.surf, elem.border_color, (elem.border, elem.border, 50, 50), 1)

                    elem.surf.blit(text, (20, 15))

                    self.screen.blit(elem.surf, (elem.x, elem.y))

                    pygame.display.update()

    def slide_in(self, temp_val, source_x, source_y, dest_x, dest_y):
        arr_elem = self.model.arr_elem
        a = self.model.a

        left = -0.5
        down = 0.5

        for i in range(len(a)):
            elem = arr_elem[i]
            if elem.x == source_x:
                elem.surf.fill(self.WHITE)
                elem.border_color = self.RED
                text = self.font.render(str(temp_val), 1, self.BLACK)

                while source_x > dest_x:
                    source_x += left

                    pygame.draw.rect(elem.surf, elem.border_color, (elem.border, elem.border, 50, 50), 1)

                    elem.surf.blit(text, (20, 15))

                    self.screen.blit(elem.surf, (source_x, source_y))

                    pygame.display.update()
                pygame.time.wait(1000)
                elem.surf.fill(self.WHITE)

                text = self.font.render(str(temp_val), 1, self.BLACK)

                while source_y < dest_y:
                    source_y += down

                    pygame.draw.rect(elem.surf, elem.border_color, (elem.border, elem.border, 50, 50), 1)

                    elem.surf.blit(text, (20, 15))

                    self.screen.blit(elem.surf, (source_x, source_y))

                    pygame.display.update()
            elem.border_color = self.WHITE

class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.border = 5

        self.surf = pygame.Surface((70, 70), pygame.SRCALPHA)
        self.surf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.surf.fill((255, 255, 255))
        self.border_color = ((255, 255, 255))

    def __repr__(self):
        return f'({self.x}, {self.y})'
