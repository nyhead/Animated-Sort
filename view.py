import sys

import pygame
import random
from pygame.locals import *


class View:
    def __init__(self, model):
        self.model = model
        self.arr_elem = []
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.font = None
        self.width, self.height = None, None
        self.BLACK = self.WHITE = self.RED = self.BLUE = self.GREEN = None

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
            self.arr_elem.append(Element(center[0] + i * 70, center[1]))

        self.isinitialized = True

    def intro(self):
        if not self.isinitialized: return

        running = True
        while running:
            self.screen.fill(self.WHITE)

            bubble_sort = self.font.render('Bubble Sort', 1, self.BLACK)
            selection_sort = self.font.render('Selection Sort', 1, self.BLACK)
            insertion_sort = self.font.render('Insertion Sort', 1, self.BLACK)
            mx, my = pygame.mouse.get_pos()

            button_bubble = pygame.rect.Rect(self.width // 2 - 150, self.height // 2 - 50, 250, 50)
            button_selection = pygame.rect.Rect(self.width // 2 - 150, self.height // 2, 400, 50)
            button_insertion = pygame.rect.Rect(self.width // 2 - 150, self.height // 2 + 50, 400, 50)

            self.screen.blit(bubble_sort, button_bubble)
            self.screen.blit(selection_sort, button_selection)
            self.screen.blit(insertion_sort, button_insertion)

            pygame.display.update()

            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if button_bubble.collidepoint((mx, my)):
                    return "BUBBLE"
                if button_selection.collidepoint((mx, my)):
                    return "SELECTION"
                if button_insertion.collidepoint((mx, my)):
                    return "INSERTION"

    def initiate_event_loop(self):
        pygame.time.set_timer(USEREVENT, 1000)
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == USEREVENT:
                break

    def show_array(self, ignore_list = []):
        a = self.model.a
        center = (100, self.height / 2)
        arr_elem = self.arr_elem

        for i in range(len(a)):
            if arr_elem[i] in  ignore_list: continue

            border = arr_elem[i].border
            border_color = arr_elem[i].border_color

            text = self.font.render(str(a[i]), 1, self.BLACK)
            box = pygame.rect.Rect((arr_elem[i].x, arr_elem[i].y, 50, 50))
            pygame.draw.rect(self.screen, arr_elem[i].border_color, box, 1)

            text_rec = text.get_rect(center=box.center)

            self.screen.blit(text, text_rec)
        pygame.display.update()

        # self.clear_arr()

    def clear_arr(self, CLEAR_COLOR = False):
        arr_elem = self.arr_elem
        # arr_elem.clear()
        center = (100, self.height / 2)
        for i in range(len(self.model.a)):
            # arr_elem[i].surf.fill(self.WHITE)
            if CLEAR_COLOR: arr_elem[i].border_color = self.WHITE
            arr_elem[i].x, arr_elem[i].y = center[0] + i * 70, center[1]

    def slide_two_elements(self, elem1, elem2):
        left = -0.1
        right = 0.1

        init_elem1_x = elem1.x
        init_elem2_x = elem2.x

        a = self.model.a
        center = (100, self.height / 2)
        arr_elem = self.arr_elem

        for i in range(len(a)-1):
            if arr_elem[i] is elem1:
                elem1.border_color = elem2.border_color = self.RED

                text1 = self.font.render(str(a[i]), 1, self.BLACK)
                text2 = self.font.render(str(a[i+1]), 1, self.BLACK)

                while elem1.x < init_elem2_x and elem2.x > init_elem1_x:
                    self.screen.fill(self.WHITE)
                    self.show_array()

                    elem1.x += right
                    elem2.x += left

                    box1 = pygame.rect.Rect((elem1.x, elem1.y, 50, 50))
                    text_rect1 = text1.get_rect(center=box1.center)
                    box2 = pygame.rect.Rect((elem2.x, elem2.y, 50, 50))
                    text_rect2 = text2.get_rect(center=box2.center)


                    pygame.draw.rect(self.screen, elem1.border_color, box1, 1)
                    pygame.draw.rect(self.screen, elem2.border_color, box2, 1)

                    self.screen.blit(text1, text_rect1)
                    self.screen.blit(text2, text_rect2)

                    # pygame.display.update()
                    # self.show_array()
                elem1.border_color = elem2.border_color = self.WHITE
            # else:
            #     border = arr_elem[i].border
            #     border_color = arr_elem[i].border_color
            #
            #     text = self.font.render(str(a[i]), 1, self.BLACK)
            #     box = pygame.rect.Rect((arr_elem[i].x, arr_elem[i].y, 50, 50))
            #     pygame.draw.rect(self.screen, self.BLACK, box, 1)
            #
            #     text_rec = text.get_rect(center=box.center)
            #
            #     self.screen.blit(text, text_rec)
            #     pygame.display.update()
            #     self.screen.fill(self.WHITE)

        # self.clear_arr()
        pygame.display.update()

    def slide_up(self, source_index):

        arr_elem = self.arr_elem
        a = self.model.a
        elem = arr_elem[source_index]

        up = -0.5

        for i in range(len(a)):
            if i == source_index:
                elem.border_color = self.RED

                text = self.font.render(str(a[i]), 1, self.BLACK)

                limit_up = elem.y - 100
                while elem.y > limit_up:
                    self.screen.fill(self.WHITE)
                    self.show_array()

                    elem.y += up

                    box = pygame.rect.Rect((elem.x, elem.y, 50, 50))
                    pygame.draw.rect(self.screen, elem.border_color, box, 1)

                    text_rec = text.get_rect(center=box.center)

                    self.screen.blit(text, text_rec)

                    # pygame.display.update()

                elem.border_color = self.WHITE

    def slide_right(self, j, t):
        arr_elem = self.arr_elem
        a = self.model.a

        right = 0.5

        prev_x = prev_y = None
        elem = arr_elem[j]
        dest = arr_elem[j+1].x
        while j >= 0 and a[j] > t:
            prev_x = elem.x
            prev_y = elem.y
            text = self.font.render(str(a[j]), 1, self.BLACK)

            while elem.x < dest:
                self.screen.fill(self.WHITE)
                self.show_array()

                elem.x += right

                box = pygame.rect.Rect((elem.x, elem.y, 50, 50))
                pygame.draw.rect(self.screen, elem.border_color, box, 1)

                text_rec = text.get_rect(center=box.center)

                self.screen.blit(text, text_rec)
            self.initiate_event_loop()
            j -= 1
            elem = arr_elem[j]
            dest = prev_x
        return prev_x, prev_y

        # for i in range(len(a)):
        #     if arr_elem[i].x == source_x:
        #         elem = arr_elem[i]
        #
        #         text = self.font.render(str(a[i]), 1, self.BLACK)
        #
        #         while elem.x < dest_x:
        #             self.screen.fill(self.WHITE)
        #             self.show_array()
        #
        #             elem.x += right
        #
        #             box = pygame.rect.Rect((elem.x, elem.y, 50, 50))
        #             pygame.draw.rect(self.screen, elem.border_color, box, 1)
        #
        #             text_rec = text.get_rect(center=box.center)
        #
        #             self.screen.blit(text, text_rec)


    def slide_in(self, temp_val, source_x, source_y, dest_x, dest_y):
        arr_elem = self.arr_elem
        a = self.model.a

        left = -0.5
        down = 0.5

        for i in range(len(a)):
            elem = arr_elem[i]
            if elem.x == source_x and elem.y == source_y:
                elem.border_color = self.RED
                text = self.font.render(str(a[i]), 1, self.BLACK)

                while elem.x > dest_x:
                    elem.x += left

                    box = pygame.rect.Rect((elem.x, elem.y, 50, 50))
                    pygame.draw.rect(self.screen, elem.border_color, box, 1)

                    text_rec = text.get_rect(center=box.center)

                    self.screen.blit(text, text_rec)

                    pygame.display.update()
                    self.screen.fill(self.WHITE)
                    self.show_array()

                self.initiate_event_loop()

                text = self.font.render(str(temp_val), 1, self.BLACK)

                while elem.y < dest_y:
                    elem.y += down

                    box = pygame.rect.Rect((elem.x, elem.y, 50, 50))
                    pygame.draw.rect(self.screen, elem.border_color, box, 1)

                    text_rec = text.get_rect(center=box.center)

                    self.screen.blit(text, text_rec)

                    pygame.display.update()
                    self.screen.fill(self.WHITE)
                    self.show_array()
                self.initiate_event_loop()
            elem.border_color = self.WHITE


class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.border = 5

        # self.surf = pygame.Surface((70, 70), pygame.SRCALPHA)
        #
        # self.surf.fill((255, 255, 255))
        self.border_color = ((255, 255, 255))

    def __repr__(self):
        return f'({self.x}, {self.y})'
