# agent.py

import math 

# P1, R1 (2/2): Meaningful class
class Robot:
    """
    Represents an autonomous agent that navigates a map. Demonstrates a composition relationship
    as the Map object is used as the robot's environment.
    """
    def __init__(self, name, start_pos, target_pos, environment):
        """
        Initialize the robot with a name, start and end coordinates, and a map of its environment.
        """
        self.name = str(name) # Immutable string
        self.current_pos = tuple(start_pos) # Immutable tuple
        self.target_pos = tuple(target_pos) # Immutable tuple
        self.map = environment # Establish composition relationship
        self.path = [] # Mutable list
        self.battery = 100
        
    def calculate_distance(self):
        """
        Calculates Euclidean distance to target using the math library.
        """
        # P1, R2 (1/2): Meaningful function
        # P2, R3: Math library (built-in library)

        # Need to calculate distance here and return it rounded to 2 or 3 decimal places

    # P1, R8 (2/2): Implement __len__ as the additional operator overload
    def __len__(self):
        """
        Overload len() operator to return the number of steps in the current path.
        """
        return len(self.path)
    
    def __str__(self):
        """
        Overload print() operator to provide a status summary for the robot.
        """
        return f"Robot '{self.name}' located at {self.current_pos}, Target: {self.target_pos}, Battery: {self.battery}%"