# test_agent.py
from src.environment import Map, create_map
from src.agent import Robot
def test_robot_distance_calculation():
    """
    Testing that the robot correctly calculates the euclidean distance to the target
    """
    create_map()
    test_map =Map("data/map_config.csv")
    robot = Robot("R1", (0,0), (3, 4), test_map)
    assert robot.calculate_distance() == 5.0
def test_robot_detects_blocked_path():
    """
    test that the robot detects a path that passes through an obstacle to avoid collision
    """
    create_map()
    test_map =Map("data/map_config.csv")
    robot=Robot("R1",(0,0), (3, 4), test_map)
    robot.path=[(0, 0), (0,1), (0, 2), (1, 2),(2,2), (3, 2),(3, 3), (3, 4)]
    assert robot.is_path_clear() == False
def test_robot_path_steps_generator():
    """
    This tests that the robot path_steps generator returns path coordinates one at a time.
    """
    create_map()
    test_map = Map("data/map_config.csv")
    robot = Robot("R1", (0, 0), (3, 4), test_map)
    robot.path =[(0, 0), (0, 1), (0, 2)]
    assert list(robot.path_steps())==[(0,0),(0, 1), (0,2)]
