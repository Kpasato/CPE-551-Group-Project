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

                dx = self.target_pos[0] - self.current_pos[0]
        dy = self.target_pos[1] - self.current_pos[1]
        return round(math.sqrt(dx**2 + dy**2), 2)

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

    def is_path_clear(self):
                if not self.path:
                                return True
                            for pos in self.path:
                                            if pos in self.map.obstacles:
                                                                return False
                                                        return True

    def update_battery(self, steps):
                for _ in range(steps):
                                if self.battery > 0:
                                                    self.battery -= 1
                                                else:
                break
