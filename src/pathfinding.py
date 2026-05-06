# pathfinding.py

from collections import deque
def get_neighbors(position, environment):
    """
    Return valid neighboring grid positions that are in bounds and not obstacles.
    """
    row, col = position
    max_rows, max_cols = environment.dimensions
    possible_moves = [
        (row - 1, col),#the possible moves are limited to up, down, left, and right
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)]
    all_positions = {
        (r, c)#building a set of every coordinate that exists inside the map boundaries
        for r in range(max_rows)
        for c in range(max_cols)}
    available_positions = all_positions - environment.obstacles #removes the obstacle coordinates so the robot only considers open spaces.
    neighbors =[#keeps only moves that are inside the grid and not blocked by obstacles
        move for move in possible_moves
        if move in available_positions]
    return neighbors
def find_path(environment, start_pos, target_pos):
    """
    Find a collision-free path from the start position to the target position using breadth-first search.
    Returns a list of coordinate tuples. Returns an empty list if no path is found.
    """
    start_pos = tuple(start_pos)
    target_pos = tuple(target_pos)# if either endpoint is blocked then there is no valid path
    if start_pos in environment.obstacles or target_pos in environment.obstacles:
        return []
    queue = deque()#queue stores each position along with the path taken to reach it
    queue.append((start_pos, [start_pos]))
    visited = set()
    visited.add(start_pos)
    while queue:
        current_pos, path = queue.popleft()#once the target is reached, it returns the full path
        if current_pos == target_pos:
            return path
        for neighbor in get_neighbors(current_pos, environment):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []#returns empty since if the queue is empty and the target was not found, no path exists


