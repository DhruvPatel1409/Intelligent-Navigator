from PIL import Image
import tkinter as tk  
from collections import Counter

from PIL import Image

def image_to_maze_with_start_end(image_file, cell_size):
    """
    Convert an image of a maze into a 2D list, recognizing walls, paths, start, end, coffee shop, pits, and warnings.
    """
    img = Image.open(image_file).convert("RGB")
    width, height = img.size
    maze = []

    for y in range(0, height, cell_size):
        row = []
        for x in range(0, width, cell_size):
            pixel = img.getpixel((x, y))
            if pixel == (0, 0, 0):  
                row.append(0)
            elif pixel == (255, 255, 255):  
                row.append(1)
            elif pixel == (255, 0, 0):  
                row.append(2)
            elif pixel == (0, 255, 0):  
                row.append(3)
            elif pixel == (255, 255, 0):  
                row.append(4)
            elif pixel == (128, 128, 128):
                row.append(5)
            elif pixel == (255, 182, 193):
                row.append(6)
            else:  
                row.append(-1)  
        maze.append(row)
    return maze



def display_feature_counts(matrix):
    """
    Display the counts of each feature in the matrix for debugging.

    Args:
        matrix: 2D list representing the maze.
    """
    flat_list = [item for sublist in matrix for item in sublist]
    feature_counts = Counter(flat_list)

    print("Feature Counts:")
    for feature, count in sorted(feature_counts.items()):
        print(f"Feature {feature}: {count} cells")


def display_matrix(matrix):
    """
    Display the 2D matrix in a GUI window using tkinter.

    Args:
        matrix: 2D list where each value represents a different feature.
    """
    root = tk.Tk()
    root.title("Maze Matrix")

    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            label = tk.Label(root, text=str(value), font=('Arial', 18), padx=10, pady=5)
            label.grid(row=row_idx, column=col_idx)

    root.mainloop()

def find_start_end_middle(maze):
    """Locate the start (2) and end (3) points in the maze."""
    start, end, coffee, pit,warning = None, None, None, None 
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 2:
                start = (r,c)
            elif maze[r][c] == 3:
                end = (r, c)
            elif maze[r][c] == 4:
                coffee == (r, c)
            elif maze[r][c] == 5:
                pit == (r, c)
            elif maze[r][c] == -1:
                Warning == (r, c)
    return start, end , coffee, pit , warning


image_file = "C:/Users/ADMIN/Desktop/python jupyter/AI/shortest path/big_maze.png" 
cell_size = 10

parsed_maze = image_to_maze_with_start_end(image_file, cell_size)

display_feature_counts(parsed_maze)

display_matrix(parsed_maze)

print("\nParsed Maze:")
for row in parsed_maze:
    print(row)


    