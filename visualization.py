import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def visualize_search(grid, visited_order, target, title, weights=None):
    rows, cols = len(grid), len(grid[0])
    fig, ax = plt.subplots(figsize=(10, 10))

    def update(frame):
        ax.clear()
        ax.set_title(f"{title} Step {frame + 1}/{len(visited_order)}")
        ax.set_xticks([])
        ax.set_yticks([])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    color = 'black'
                elif (i, j) == (0, 0):
                    color = 'green'
                elif (i, j) == target:
                    color = 'red'
                elif (i, j) in visited_order[:frame + 1]:
                    color = 'skyblue'
                else:
                    color = 'white'

                rect = plt.Rectangle((j, rows - i - 1), 1, 1, color=color, edgecolor='gray')
                ax.add_patch(rect)
                
                # Display weights for weighted algorithms
                if weights is not None and grid[i][j] == 0:
                    weight = weights[i][j]
                    if weight != float('inf'):
                        ax.text(j + 0.5, rows - i - 0.5, str(weight), 
                                ha='center', va='center', fontsize=8)

        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)

    ani = animation.FuncAnimation(fig, update, frames=len(visited_order), interval=200, repeat=False)
    plt.show()

def visualize_path(grid, path, visited_order, target, title, weights=None):
    """
    Visualize the final path found by the algorithm along with the search process
    """
    rows, cols = len(grid), len(grid[0])
    fig, ax = plt.subplots(figsize=(10, 10))

    # Create a static image showing the final path
    ax.set_title(f"{title} Final Path")
    ax.set_xticks([])
    ax.set_yticks([])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                color = 'black'
            elif (i, j) == (0, 0):
                color = 'green'
            elif (i, j) == target:
                color = 'red'
            elif (i, j) in path:
                color = 'yellow'  # Path color
            elif (i, j) in visited_order:
                color = 'lightblue'  # Visited but not in path
            else:
                color = 'white'

            rect = plt.Rectangle((j, rows - i - 1), 1, 1, color=color, edgecolor='gray')
            ax.add_patch(rect)
            
            # Display weights for weighted algorithms
            if weights is not None and grid[i][j] == 0:
                weight = weights[i][j]
                if weight != float('inf'):
                    ax.text(j + 0.5, rows - i - 0.5, str(weight), 
                            ha='center', va='center', fontsize=8)

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    plt.show()
