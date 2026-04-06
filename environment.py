# environment.py
import numpy as np # Import numpy library
import csv # Import built-in csv module

def create_map():
    """
    Create the csv file with map information writing to 'map_config.csv'. 0 is for empty space and 1 is for obstacles.
    """
    data = [[0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0]]
    # Write the data to a csv file in the current working directory
    with open('./map_config.csv', "w") as fo:
        writer = csv.writer(fo)
        writer.writerows(data)

class Map:
    """
    A representation of the environment. Contains attributes such as grid data, dimensions, and obstacle data.
    """
    def __init__(self, file_path):
        """
        Initialize the workspace based on the provided file.
        """
        self.file_path = file_path
        self.grid_data = None # Will be populated w/ numpy
        self.dimensions =  (0, 0) # Immutable tuple
        self.obstacles = set() # Mutable set

        # Load the map on initiation
        self.load_map()

    def load_map(self):
        """
        Read the csv file to populate the grid data, dimensions, and obstacle data.
        """
        # Requirement 5: Meaningful data I/O - reading a file
        raw_data = []
        with open(self.file_path, "r") as fo:
            reader = csv.reader(fo)
            for row in reader:
                # Convert the string digits to integers using list comprehension
                raw_data.append([int(cell) for cell in row])
        # Requirement 3 (1/2): Use advanced Python library numpy for data processing
        self.grid_data = np.array(raw_data)

        # Requirement 7 (1/4): Populate the dimensions (given by .shape in numpy) as an immutable tuple
        self.dimensions = self.grid_data.shape

        # Find the obstacle coordinates
        # Use numpy's .nditer to iterate the grid data array and access indicies w/ multi_index
        it = np.nditer(self.grid_data, flags=['multi_index'])
        # Requirement 7 (2/4): Use list comprehension to get the obstacle coordinates of indicies with a value of 1 (an obstacle)
        self.obstacles = {it.multi_index for x in it if x == 1}

    def __str__(self):
        """
        Overload print() to print useful map information.
        """
        return f"Map loaded: {self.dimensions[0]}x{self.dimensions[1]} grid with {len(self.obstacles)} obstacles."
print(Map('map_config.csv'))

