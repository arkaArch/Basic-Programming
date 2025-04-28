"""
A filled-in square will be “alive” and an empty square will be “dead.” 
If a living square has two or three living neighbors, it continues to live on the next step.
If a dead square has exactly three living neighbors, it comes alive on the next step.
"""

# Here we take '#' as a living cell and ' ' as a dead cell.
import random, time, copy
WIDTH = 60
HEIGHT = 20     # Capital, since they're constant

# Create an empty list of list. We append another list 'row' later.
cells = []               # Think it as a column
for i in range(HEIGHT):
    row = [] # Create a new row
    for j in range(WIDTH):
        if random.randint(0, 1) == 1:
            row.append('#')      # Add a living cell 
        else:
            row.append(' ')      # Add a dead cell
    # Append the column in the cell
    cells.append(row)

# Main program loop
while True:
    print('\n\n\n\n')   # Separate each step with new lines
    current_cell = copy.deepcopy(cells)
    # We use deepcopy when we want to copy the elements of lists inside a list

    # Print current_cell on the screen
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(current_cell[i][j], end='')
        print()

    # Calculate the next step
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # % WIDTH ensures left_coordinate is always between 0 and (WIDTH - 1)
            left_coordinate = (j - 1) % WIDTH
            right_coordinate = (j + 1) % WIDTH
            above_coordinate = (i - 1) % HEIGHT
            below_coordinate = (i + 1) % HEIGHT

            # Count number of living neighbors:
            num_neighbors = 0
            # Top-left neighbors is alive:
            if current_cell[above_coordinate][left_coordinate] == '#':
                num_neighbors += 1
            # Top neighbors is alive
            if current_cell[above_coordinate][j] == '#':
                num_neighbors += 1
            # Top-right neighbors is alive
            if current_cell[above_coordinate][right_coordinate] == '#':
                num_neighbors += 1
            # Left neighbors is alive
            if current_cell[i][left_coordinate] == '#':
                num_neighbors += 1
            # Right neighbors is alive
            if current_cell[i][right_coordinate] == '#':
                num_neighbors += 1
            # Bottom left neighbors is alive
            if current_cell[below_coordinate][left_coordinate] == '#':
                num_neighbors += 1
            # Bottom neighbors is alive
            if current_cell[below_coordinate][j] == '#':
                num_neighbors += 1
            # Bottom right neighbors is alive
            if current_cell[below_coordinate][right_coordinate] == '#':
                num_neighbors += 1

            # Set cell based on conway's game of life:
            # A living neighbors has two or three living neighbors it continues to live:
            if current_cell[i][j] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                cells[i][j] = '#'
            # A dead cell has exactly three living neighbors, it comes alive:
            elif current_cell[i][j] == ' ' and num_neighbors == 3:
                cells[i][j] = '#'
            # Everything else dies or stay dead:
            else:
                cells[i][j] = ' '

    # Add a 1 second pause for every step
    time.sleep(1)
