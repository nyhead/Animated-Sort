import pygame
import model
import random
from pygame.locals import *

class View:
    def __init__(self, model):
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock =  None
        self.font = None
        self.width, self.height = None, None

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

            # pygame.draw.rect(self.screen, self.RED, button_selection)
            # pygame.draw.rect(self.screen, self.GREEN, button_bubble)
            # pygame.draw.rect(self.screen, self.BLUE, button_insertion)

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
        center = (100, self.height/2)
        arr_elem = self.model.arr_elem
        # print(arr_elem)

        for i in range(len(a)):
            surf = arr_elem[i].surf
            border = arr_elem[i].border
            border_color = arr_elem[i].border_color

            text = self.font.render(str(a[i]), 1, self.BLACK)
            text_rect = text.get_rect()

            # print(a[i])
            box = pygame.rect.Rect((border, border, 50, 50))
            pygame.draw.rect(surf, border_color, box, 1)

            surf.blit(text, (20, 15))
            self.screen.blit(surf, (arr_elem[i].x, arr_elem[i].y))



    def clear_arr(self):
        arr_elem = self.model.arr_elem
        for i in range(len(arr_elem)):
            surf = arr_elem[i].surf
            # surf.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
            surf.fill(self.WHITE)
    def initialize(self):
        result = pygame.init()
        pygame.font.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Sans-Serif", 50)
        self.BLACK, self.WHITE, self.RED, self.BLUE, self.GREEN = (0,0,0), (255,255,255), (255,0,0), (0,0,255), (0,128,0)

        center = (100, self.height / 2)
        for i in range(len(self.model.a)):
            self.model.arr_elem.append(Element(center[0]+i*70, center[1]))
        # print(self.model.arr_elem)

        self.isinitialized = True


class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.border = 5

        self.surf = pygame.Surface((70,70), pygame.SRCALPHA)
        self.surf.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.surf.fill((255,255,255))
        self.border_color = ((255,255,255))

    def __repr__(self):
        return f'({self.x}, {self.y})'
