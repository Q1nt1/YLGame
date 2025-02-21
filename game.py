import pygame
import sys
from const import *


class Game:
    def __init__(self):
        pass

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  # Белый
                else:
                    color = (163, 113, 67)  # Темный

                rect = (SQUARESIZE * row, SQUARESIZE * col, SQUARESIZE, SQUARESIZE)

                pygame.draw.rect(surface, color, rect)
