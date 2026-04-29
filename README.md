# Timetable Optimiser

## Description
This work implements a multi objective evolutionary algorithm to solve a university timetabling problem. The optimiser generates candidate timetables and iteratively improves them using genetic operators such as crossover and mutation. The optimisation focuses on two conflicting objectives: minimising clashes between modules that share students, and reducing the number of teaching days required by staff. A Pareto based selection mechanism is used to maintain a set of non-dominated solutions, allowing the algorithm to produce multiple trade-off timetables rather than a single optimal solution.
## Setup
1. Install Python (3.11+ recommended)
2. Install required dependency:
   ```
   pip install matplotlib
   ```

## Run
To execute the optimiser:
```
python src/main.py
```

To run experiments and generate results:
```
python src/experiments.py
```
