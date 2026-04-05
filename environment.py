# environment.py

import csv # Import built-in csv module

def write_csv():
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

