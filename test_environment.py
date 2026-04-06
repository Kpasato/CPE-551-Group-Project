# test_environment.py

import pytest
import os
from environment import Map

# P1, R4 (3/4): Pytest FileNotFoundError
def test_file_not_found_handling():
    """
    Test 1: Verifies that passing a non-existent file path to the Map class does not crash the program
    and initializes empty grid data instead.
    """
    # Attempt to load a non-existent file
    test_map = Map("non_existent_file.csv")

    # Ensure the try-except handling in environment.py is working by verifying empty grid data
    assert test_map.grid_data.size == 0
    assert len(test_map.obstacles) == 0

# P1, R4 (4/4): Pytest ValueError
def test_invalid_data_handling():
    """
    Test 2: Verifies that a CSV with non-numeric data is handled gracefully, initializing empty grid data to avoid crashing.
    """
    # Create a non-numeric/corrupt CSV file
    corrupt_file = "corrupt_map.csv"
    with open(corrupt_file, "w") as fo:
        fo.write("1,0,A\n0,1,0") # The 'A' should trigger a ValueError as it cannot be converted to int

    # Attempt to load the corrupt file
    test_map = Map(corrupt_file)

    # Verify empty grid data
    assert test_map.grid_data.size == 0
    assert len(test_map.obstacles) == 0

    # Remove the file after the test
    if os.path.exists(corrupt_file):
        os.remove(corrupt_file)
