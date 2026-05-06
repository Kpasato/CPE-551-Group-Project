from src.environment import Map, create_map
from src.pathfinding import find_path
def test_find_path_returns_valid_start_and_target():
    """
    test that find_path returns a path starting at the start position and end at the target position.
    """
    create_map()
    test_map = Map("data/map_config.csv")
    path = find_path(test_map, (0, 0), (3, 4))  #generate a path through the sample map
    assert path[0] ==(0, 0)
    assert path[-1] == (3, 4)#the returned path should begin and end at the requested coordinates
def test_find_path_avoids_obstacles():
    """
    testing that find_path returns a path that does not pass through obstacle coordinates.
    """
    create_map()
    test_map = Map("data/map_config.csv")
    path = find_path(test_map, (0, 0),(3, 4)) #generate a path and check every coordinate against the maps obstacle set
    for position in path:
        assert position not in test_map.obstacles
