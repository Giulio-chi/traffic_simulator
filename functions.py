import random
from costants import *
from classes import *

def create_random_streets(cells, density):
    base_weights = {'down': 0.25, 'up': 0.25, 'left': 0.25, 'right': 0.25}
    current_streak_move = None
    current_streak_count = 0 
    starting_position = [random.randint(0, NUM_OF_CELLS[1] - 1), 0]

    position = starting_position
    num_of_streets = 0
    street_density = 0
    while street_density < density:
        # print(position)
        street_density = num_of_streets / (NUM_OF_CELLS[0] * NUM_OF_CELLS[1])
        
        retries = 0
        max_retries = 10

        while retries < max_retries:
            adjusted_weights = {}
            total_weight = 0

            for direction, base_weight in base_weights.items():
                if direction == current_streak_move:
                    adjusted_weight = base_weight / (1 + current_streak_count)

                else:
                    adjusted_weight = base_weight * 0.001

                adjusted_weights[direction] = adjusted_weight
                total_weight += adjusted_weight

            for direction in adjusted_weights:
                adjusted_weights[direction] /= total_weight

            movement = random.choices(list(adjusted_weights.keys()), list(adjusted_weights.values()))[0]

            if movement == current_streak_move:
                current_streak_count += 1

            else:
                current_streak_move = movement
                current_streak_count = 1

            new_x, new_y = position[0], position[1]

            if movement == 'down' and position[0] < NUM_OF_CELLS[0] - 1:
                new_x = position[0] + 1
            elif movement == 'up' and position[0] > 0:
                new_x = position[0] - 1
            elif movement == 'right' and position[1] < NUM_OF_CELLS[1] - 1:
                new_y = position[1] + 1
            elif movement == 'left' and position[1] > 0:
                new_y = position[1] - 1

            if new_x >= 0 and new_x < NUM_OF_CELLS[0] and new_y >= 0 and new_y < NUM_OF_CELLS[1]:

                street_neighbors = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = new_x + dx, new_y + dy
                    if 0 <= nx < NUM_OF_CELLS[0] and 0 <= ny < NUM_OF_CELLS[1]:
                        if cells[nx][ny].type == 'street':
                            street_neighbors += 1


            if cells[new_x][new_y].type != 'street' and street_neighbors <= 1:
                position = [new_x, new_y]
                cells[new_x][new_y].type = 'street'
                cells[new_x][new_y].color = (155, 155, 155)
                num_of_streets += 1
                break

            retries += 1

        if retries == max_retries:
            position = [random.randint(0, NUM_OF_CELLS[1] - 1), random.randint(0, NUM_OF_CELLS[0] - 1)]


        

if __name__ == '__main__':
    cells = [[Cell('building', i, j) for j in range(NUM_OF_CELLS[1])] for i in range(NUM_OF_CELLS[0])]
    create_random_streets(cells, 0.75)
    print(cells)
