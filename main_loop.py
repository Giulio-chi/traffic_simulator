import pygame
import random

from classes import *
from functions import *
from pygame_actions import *
from costants import *


pygame.init()
surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Traffic simulation')

# icon = pygame.image.load('main_python\\Pygame\\Sudoku\\icon.jpg')
# pygame.display.set_icon(icon)

cells = [[Cell('building', i, j) for j in range(NUM_OF_CELLS[0])] for i in range(NUM_OF_CELLS[1])]
create_random_streets(cells, 0.4)


running = True
while running:

    mouse = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cell_width = DISPLAY_WIDTH // NUM_OF_CELLS[0]
            cell_height = DISPLAY_HEIGHT // NUM_OF_CELLS[1]

            grid_x = mouse[0] // cell_width
            grid_y = mouse[1] // cell_height

            for _ in cells:
                for cell in _:
                    if cell.x == grid_x and cell.y == grid_y:
                        if cell.type == 'building':
                            cell.type = 'street'
                            cell.color = (155, 155, 155)
                        
                        elif cell.type == 'street':
                            cell.type = 'building'
                            cell.color = (145, 78, 245)

                        break

    surface.fill((255, 255, 255))
    draw_cells(surface, cells)

    pygame.display.update()

pygame.quit()