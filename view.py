import pygame
import model
from pygame.locals import *

class View:
    def __init__(self, model):
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock =  None
        self.font = None
        self.width, self.heght = None, None
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
                return ''


    def initialize(self):
        result = pygame.init()
        pygame.font.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Sans-Serif", 40)
        self.BLACK, self.WHITE, self.RED, self.BLUE, self.GREEN = (0,0,0), (255,255,255), (255,0,0), (0,0,255), (0,128,0)
        self.isinitialized = True