import pygame
from costants import *

def draw_cells(surface, cells):
    dimensions = (DISPLAY_WIDTH // NUM_OF_CELLS[0], DISPLAY_HEIGHT // NUM_OF_CELLS[1])
    for _ in cells:
        for cell in _:
            pygame.draw.rect(surface, cell.color, (cell.x * dimensions[0], cell.y * dimensions[1], dimensions[0], dimensions[1]))