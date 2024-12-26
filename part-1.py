import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from collections import deque

def find_start_end(maze):
    start, end = None, None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 2:  # Start point
                start = (i, j)
            elif cell == 3:  # End point
                end = (i, j)
    return start, end

def is_valid_move(maze, x, y, visited):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] in [1, 3] and (x, y) not in visited

def bfs_explore_until_goal(maze):
    start, end = find_start_end(maze)
    if not start or not end:
        return [], []  # Return empty if start or end is not found

    # Directions for movement: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue for BFS, starting with the start point and the path taken to reach it
    queue = deque([(start, [start])])  # Store the cell and the path to it
    
    # Set to track visited cells
    visited = set()
    visited.add(start)
    
    reachable_cells = []  # To store reachable cells
    shortest_path = []    # To store the shortest path if found

    while queue:
        (x, y), path = queue.popleft()
        reachable_cells.append((x, y))
        
        # If we reached the end, store the path and break the loop
        if (x, y) == end:
            shortest_path = path
            break
        
        # Explore all directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, new_x, new_y, visited):
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))  # Append new path
    
    return reachable_cells, shortest_path

def visualize_paths(maze, reachable_cells, shortest_path):
    # Create a color map for visualization
    cmap = colors.ListedColormap(['black', 'white', 'red', 'blue', 'green'])  # Blue for the paths
    bounds = [0, 1, 2, 3, 4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    maze_array = np.array(maze)  # Convert maze to numpy array for easier manipulation

    # Draw the maze with start (2) and end (3)
    ax.imshow(maze_array, cmap=cmap, norm=norm)

    # Draw all reachable cells in red
    for (x, y) in reachable_cells:
        ax.scatter(y, x, color='blue', s=100)  # y and x are reversed in scatter
        plt.pause(0.01)  # Short pause to show the exploration
    
    # After exploring, draw the shortest path in blue
    for (x, y) in shortest_path:
        ax.scatter(y, x, color='red', s=100)  # y and x are reversed in scatter

    plt.show()

# Example maze input
maze = [
    [2, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Explore reachable cells and find the shortest path
reachable_cells, shortest_path = bfs_explore_until_goal(maze)

# Visualize reachable cells in red and the shortest path in blue
visualize_paths(maze, reachable_cells, shortest_path)

# Print the shortest path
print("Shortest path:", shortest_path)
