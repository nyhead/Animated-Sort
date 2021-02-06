import random


class Game:
    def __init__(self):
        # self.a = [random.randint(1,8) for i in range(8)]
        self.a = [6, 5, 3, 1, 8, 7, 2, 4] # selection
        # self.a = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]  # insertion
        self.arr_elem = []
        self.FPS = 60
