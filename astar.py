import heapq
from visualization import visualize_search, visualize_path

def heuristic(a, b):
    """
    Manhattan distance heuristic for A* algorithm
    Args:
        a: Tuple (row, col) representing the current position
        b: Tuple (row, col) representing the target position
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_with_steps(grid, target, weights=None):
    """
    Implementation of A* algorithm with visualization.
    Args:
        grid: 2D array where 0 represents open path and 1 represents obstacle
        target: Tuple (row, col) representing the target position
        weights: 2D array of weights for each cell, if None, all cells have weight 1
    """
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    
    # If no weights are provided, use uniform weights (1) for all open cells
    if weights is None:
        weights = [[1 if grid[i][j] == 0 else float('inf') for j in range(cols)] for i in range(rows)]
    
    # g_score: Cost from start to current node
    g_score = {start: 0}
    # f_score: Estimated total cost from start to goal through current node
    f_score = {start: heuristic(start, target)}
    # Priority queue for A* algorithm
    open_set = [(f_score[start], 0, start)]  # (f_score, tiebreaker, node)
    # Previous node dictionary for path reconstruction
    came_from = {}
    # Set to track visited nodes
    closed_set = set()
    # List to track the order of cells visited for visualization
    visited_order = []
    
    # Counter for tiebreaking equal f_scores
    counter = 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    while open_set:
        _, _, current = heapq.heappop(open_set)
        
        if current in closed_set:
            continue
            
        closed_set.add(current)
        visited_order.append(current)
        
        # If we reached the target, break
        if current == target:
            break
            
        x, y = current
        
        # Check all neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the neighbor is valid and not an obstacle
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                
                # If we've already evaluated this neighbor, skip
                if neighbor in closed_set:
                    continue
                    
                # Calculate tentative g_score
                tentative_g_score = g_score[current] + weights[nx][ny]
                
                # If this path is better than any previous one
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Record the best path
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, target)
                    
                    # Add to the open set if not already there
                    heapq.heappush(open_set, (f_score[neighbor], counter, neighbor))
                    counter += 1
    
    # Reconstruct path if target was found
    path = []
    if target in came_from:
        current = target
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
    
    # Visualize the search process
    visualize_search(grid, visited_order, target, title="A* Search", weights=weights)
    
    # Visualize the final path if found
    if path:
        visualize_path(grid, path, visited_order, target, title="A* Search", weights=weights)
    
    # Return the path length to target (if found)
    return g_score.get(target, float('inf'))