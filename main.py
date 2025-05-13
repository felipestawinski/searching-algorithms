from bfs import bfs_with_steps
from dfs import dfs_with_steps
from dijkstra import dijkstra_with_steps
from astar import astar_with_steps
import numpy as np

def main():
    grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

    target = (9, 9)
    
    # Create a weights grid for Dijkstra and A* (example with random weights)
    rows, cols = len(grid), len(grid[0])
    # Create weights in range 1-5 for open cells
    np.random.seed(42)  # For reproducibility
    weights = [[np.random.randint(1, 6) if grid[i][j] == 0 else float('inf') 
                for j in range(cols)] for i in range(rows)]

    print("Running BFS...")
    bfs_with_steps(grid, target)
    
    print("Running DFS...")
    dfs_with_steps(grid, target)
    
    print("Running Dijkstra's algorithm...")
    dijkstra_with_steps(grid, target, weights)
    
    print("Running A* algorithm...")
    astar_with_steps(grid, target, weights)
    
    return

if __name__ == "__main__":
    main()