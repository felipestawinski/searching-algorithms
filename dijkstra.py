import heapq
from visualization import visualize_search, visualize_path

def dijkstra_with_steps(grid, target, weights=None):
    """
    Implementation of Dijkstra's algorithm with visualization.
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
    
    # Distance dictionary
    distances = {start: 0}
    # Previous node dictionary for path reconstruction
    previous = {}
    # Priority queue for Dijkstra's algorithm
    pq = [(0, start)]
    # Set to track visited nodes
    visited = set()
    # List to track the order of cells visited for visualization
    visited_order = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # If we've already processed this node, skip it
        if current in visited:
            continue
        
        # Mark as visited
        visited.add(current)
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
                
                # Calculate new distance to neighbor
                new_dist = current_dist + weights[nx][ny]
                
                # If this path is better than any previous one
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
    
    # Reconstruct path if target was found
    path = []
    if target in previous:
        current = target
        while current != start:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()
    
    # Visualize the search process
    visualize_search(grid, visited_order, target, title="Dijkstra", weights=weights)
    
    # Visualize the final path if found
    if path:
        visualize_path(grid, path, visited_order, target, title="Dijkstra", weights=weights)
    
    # Return the path length to target (if found)
    return distances.get(target, float('inf'))