# pathfinding.py

from collections import deque

def get_neighbors(position, environment):
    """
    Return valid neighboring grid positions that are in bounds and not obstacles.
    """
    row, col = position
    max_rows, max_cols = environment.dimensions
    possible_moves = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)]
    all_positions = {
        (r, c)
        for r in range(max_rows)
        for c in range(max_cols)}
    available_positions = all_positions - environment.obstacles
    neighbors = [
        move for move in possible_moves
        if move in available_positions]
    return neighbors
def find_path(environment, start_pos, target_pos):
    """
    Find a collision-free path from the start position to the target position using breadth-first search.
    Returns a list of coordinate tuples. Returns an empty list if no path is found.
    """
    start_pos = tuple(start_pos)
    target_pos = tuple(target_pos)
    if start_pos in environment.obstacles or target_pos in environment.obstacles:
        return []
    queue = deque()
    queue.append((start_pos, [start_pos]))
    visited = set()
    visited.add(start_pos)
    while queue:
        current_pos, path = queue.popleft()
        if current_pos == target_pos:
            return path
        for neighbor in get_neighbors(current_pos, environment):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []


