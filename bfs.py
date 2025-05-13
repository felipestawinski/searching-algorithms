from collections import deque
from visualization import visualize_search, visualize_path

def bfs_with_steps(grid, target):
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    visited = set()
    queue = deque([start])
    visited_order = []
    # Previous node dictionary for path reconstruction
    previous = {}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        visited_order.append((x, y))

        if (x, y) == target:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if (nx, ny) not in previous:
                    previous[(nx, ny)] = (x, y)
                queue.append((nx, ny))

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
    visualize_search(grid, visited_order, target, title="BFS")
    
    # Visualize the final path if found
    if path:
        visualize_path(grid, path, visited_order, target, title="BFS")
