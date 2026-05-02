# CPE-551-Group-Project

## Project Overview

This project implements an autonomous robot navigation simulation for the AAI 551 / CPE 551 course at Stevens Institute of Technology. The system models a robot navigating a grid-based environment with static obstacles. The environment is stored in a CSV file where `0` represents open space and `1` represents an obstacle.

The program reads the map from a CSV file, stores the map using a `Map` class, creates a `Robot` object that uses the map as its environment, checks whether a path intersects with obstacles, updates robot battery usage, calculates Euclidean distance to the target, and visualizes the map and path using Matplotlib.

## Team Members

- **Kevin Pasato** - kpasato@stevens.edu - Stevens ID: 20043729
- **Danny Jutras** - djutras@stevens.edu - Stevens ID: 20013676
- **Mithil Boreddy** - mboreddy@stevens.edu - Stevens ID: 20034323

## Project Structure

```text
CPE-551-Group-Project/
├── data/
│   └── map_config.csv          # Grid map with obstacles, where 0 = empty and 1 = obstacle
├── src/
│   ├── __init__.py             # Makes src importable as a package
│   ├── agent.py                # Robot class with navigation-related logic
│   └── environment.py          # Map class with CSV loading, obstacle detection, and visualization
├── tests/
│   ├── conftest.py             # Pytest import path setup
│   ├── test_agent.py           # Pytest tests for Robot class behavior
│   └── test_environment.py     # Pytest tests for Map class exception handling
├── main.ipynb                  # Main Jupyter Notebook demo
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files/folders excluded from Git tracking
└── README.md                   # Project documentation
```
## Dependencies

Install required packages:
```bash
pip install -r requirements.txt
```

Required libraries:
- **numpy** - Grid data processing and obstacle detection
- **pytest** - Unit testing framework
- **Matplotlib** - visualizes the map and robot path

The project should be run with Python 3.12, 3.13, or 3.14

## How to Run

### Option 1: Run the Jupyter Notebook

Start Jupyter Notebook from the project folder:

```bash
jupyter notebook
```

Then open:

```text
main.ipynb
```

Run all cells in order.

### Option 2: Import the Modules Directly

The modules can also be imported into another Python file or notebook:

```python
from src.environment import Map, create_map
from src.agent import Robot

# Create the map from CSV
create_map()
env = Map("data/map_config.csv")
print(env)

# Create a robot and test basic navigation functionality
robot = Robot("R1", (0, 0), (3, 4), env)
print(robot)
print(f"Distance to target: {robot.calculate_distance()}")
```

### Option 3: Run Tests

From the project folder, run:

```bash
pytest tests/
```

Expected result:

```text
4 passed
```

## Modules

### Map Class (`src/environment.py`)

The `Map` class represents the grid-based environment. It loads a CSV file, stores the grid data with NumPy, tracks the map dimensions, and stores obstacle locations in a set.

Main features:
- Creates a sample map CSV file using `create_map()`
- Loads grid maps from `data/map_config.csv`
- Converts CSV values into a NumPy array
- Detects obstacle coordinates using NumPy iteration
- Handles `FileNotFoundError` if the map file is missing
- Handles `ValueError` if the CSV contains invalid non-numeric data
- Displays map information using `__str__`
- Visualizes the grid and robot path using Matplotlib

### Robot Class (`src/agent.py`)

The `Robot` class represents the autonomous navigation agent. It stores the robot’s current position, target position, path, battery level, and the map object it is navigating through.

Main features:
- Uses composition by storing a `Map` object as the robot’s environment
- Stores robot name, current position, target position, path, and battery level
- Calculates Euclidean distance to the target using the `math` library
- Checks whether a path intersects with any obstacles
- Updates battery level based on number of movement steps
- Displays robot status using `__str__`
- Uses `__len__` to return the number of steps in the robot’s path
### Tests (`tests/`)
The `tests` folder contains Pytest files used to check that the main parts of the project work correctly.

Current tests:
- `test_environment.py` checks missing file handling and invalid CSV data handling
- `test_agent.py` checks robot distance calculation and blocked path detection
- `conftest.py` helps Pytest import files from the `src` folder correctly
## Sample Input/Output

**Input CSV (`data/map_config.csv`):**
```text
0,0,0,1,0
0,1,0,1,0
0,1,0,0,0
0,0,0,1,0
```
**Sample Output:**
```text
Map loaded: 4x5 grid with 5 obstacles.
Robot 'R1' located at (0, 0), Target: (3, 4), Battery: 100%
Distance to target: 5.0
Path length: 8
Is path clear? False
Battery after movement: 92
```

The path example intentionally passes through an obstacle, so `is_path_clear()` returns `False`. This demonstrates that the obstacle detection logic is working.

## Requirements Fulfilled

This project fulfills the following course requirements:

### Part 1

- Two meaningful classes: `Map` and `Robot`
- Composition relationship: `Robot` stores and uses a `Map` object
- Meaningful functions/methods: `create_map`, `load_map`, `calculate_distance`, `is_path_clear`, `update_battery`, and `visualize_grid`
- Advanced libraries: NumPy and Matplotlib
- Built-in libraries: `csv` and `math`
- Exception handling: missing map file and invalid CSV data
- Pytest test cases for map error handling and robot behavior
- Data I/O using `data/map_config.csv`
- Mutable types: list and set
- Immutable types: string and tuple
- Operator overloading: `__str__` and `__len__`
- Docstrings and comments included in the main classes and functions

### Part 2

- List/set comprehension is used for obstacle detection
- Built-in modules are used, including `math` and `csv`
- Set usage is included for obstacle coordinates
- Special method `__len__` is implemented for the `Robot` class


## Main Contributions

- **Kevin Pasato**: Repository setup, data folder structure, notebook updates, project cleanup, README updates, and pytest setup support
- **Danny Jutras**: Initial source code for `environment.py` and `agent.py`, map loading logic, robot class logic, and environment tests, readme creation
- **Mithil Boreddy**: Source code and documentation contributions