# CPE-551-Group-Project

## Project Overview

This project implements an autonomous robot navigation system for the AAI 551 (CPE-551) course at Stevens Institute of Technology. The system simulates a robot navigating a grid-based map with obstacles, reading environment data from CSV files and computing paths using Euclidean distance.

## Team Members

- **Kpasato** - Project setup, data folder structure
- **Danny Jutras** - Source code (agent.py, environment.py), test implementation
- **Mithil Reddy Boreddy** - Contributions to source code and documentation

## Project Structure

```
CPE-551-Group-Project/
├── data/
│   └── map_config.csv      # Grid map with obstacles (0=empty, 1=obstacle)
├── src/
│   ├── agent.py            # Robot class with navigation logic
│   └── environment.py      # Map class with CSV loading and obstacle detection
├── tests/
│   └── test_environment.py # Pytest tests for Map class exception handling
├── main.ipynb              # Jupyter notebook demo
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Dependencies

Install required packages:
```bash
pip install -r requirements.txt
```

Required libraries:
- **numpy** - Grid data processing and obstacle detection
- **pytest** - Unit testing framework

## How to Run

### Option 1: Run the Jupyter Notebook
```bash
jupyter notebook main.ipynb
```
Then run all cells in the notebook.

### Option 2: Run from Python
```bash
python main.ipynb
```
Or import the modules directly:
```python
from src.environment import Map, create_map
from src.agent import Robot

# Create the map from CSV
create_map()
env = Map('data/map_config.csv')
print(env)

# Create a robot and navigate
robot = Robot('R1', (0, 0), (3, 4), env)
print(robot)
print(f"Distance to target: {robot.calculate_distance()}")
```

### Option 3: Run Tests
```bash
pytest tests/
```

## Modules

### Map Class (`src/environment.py`)
- Loads grid maps from CSV files
- Detects obstacle coordinates using NumPy
- Handles FileNotFoundError and ValueError exceptions gracefully

### Robot Class (`src/agent.py`)
- Represents an autonomous navigation agent
- Tracks position, target, path, and battery
- Calculates Euclidean distance to target using the math library
- Implements `__str__`, `__len__` operator overloads

## Sample Input/Output

**Input CSV (data/map_config.csv):**
```
0,0,0,1,0
0,1,0,1,0
0,1,0,0,0
0,0,0,1,0
```

**Sample Output:**
```
Map loaded: 4x5 grid with 5 obstacles.
Robot 'R1' located at (0, 0), Target: (3, 4), Battery: 100%
Distance to target: 5.0
```

## Requirements Fulfilled

This project fulfills the following course requirements:
- **Part 1**: Two meaningful classes (Robot, Map), two meaningful functions (calculate_distance, load_map), two advanced Python libraries (NumPy, pytest), exception handling, data I/O, mutable/immutable types, operator overloading, comments/docstrings
- **Part 2**: List comprehension, built-in libraries (math, csv), comprehension expressions
