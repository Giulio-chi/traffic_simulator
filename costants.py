DISPLAY_WIDTH = 684
DISPLAY_HEIGHT = 684

NUM_OF_CELLS = (57, 57)
# [1, 2, 3, 4, 6, 9, 12, 18, 19, 36, 38, 57, 76, 114, 171, 228, 342, 684]

def print_factors_count(stop):
    """
    Prints each number from 1 to `stop` and the number of factors it has.
    
    Parameters:
    stop (int): The maximum number to evaluate (inclusive).
    """
    if stop < 1:
        print("Stop number must be 1 or greater.")
        return
    
    for num in range(1, stop + 1):
        # Calculate factors by checking divisibility
        factors = [i for i in range(1, num + 1) if num % i == 0]
        # Print the number and its factor count
        print(f"{num}: {len(factors)} factors...            {factors}")
    
if __name__ == '__main__':
    print_factors_count(700)