# AI Project: Water Jug Problem

## Problem Statement
This project tackles the classic water jug problem, providing a practical application to deepen our understanding of search algorithms, particularly the A* algorithm. The objective is to determine the minimum number of steps required to measure a specific amount of water using jugs of different capacities.

## Input and Output
The input is provided via a text file with the following structure:
1. **First Line**: A variable number of integers, comma-separated, representing the capacities of the jugs.
2. **Second Line**: A single integer representing the target amount of water to be measured.

The output is either the minimum cost (number of steps) to reach the goal state or -1 if it's not possible to measure the exact amount.

## Algorithm Overview

### Step-by-Step Process
1. **Read Data**: Read and parse the data from the input file, storing the jug capacities and target amount.
2. **Initialize Infinite Jug**: Introduce an infinite jug at the 0th position in the list of jugs to simulate an unlimited water source.
3. **Initialize Lists**: Create an open list for discovered but unexplored states and a closed list for visited states.
4. **Start State**: Add the initial state (all jugs empty) to the open list.
5. **Generate Next States**: For each state, generate all possible next states by either filling, emptying, or pouring between jugs, and calculate the heuristic for each.
6. **Select State**: Choose the state with the lowest heuristic (A* value) and check if it matches the target amount of water.
7. **Goal Check**: If the chosen state matches the goal, return the cost. Otherwise, continue with the next state.
8. **Update Lists**: Move the current state to the closed list.
9. **Terminate**: If the open list is exhausted without finding the goal, return -1.

### Heuristic/A* Algorithm
1. **Remaining Water Calculation**: Determine the remaining amount of water needed to reach the target and store it as "Total".
2. **BFS Probability Adjustment**: Adjust the BFS Probability based on the target value; higher target values result in a lower BFS Probability and vice versa.
3. **State Evaluation**: For each jug, calculate the difference between the "Total" and the current state, storing these values in a list.
4. **Heuristic Determination**: Identify the minimum value in the list and divide it by the BFS Probability to obtain the heuristic for the state.
5. **A* Value Computation**: Add the current node’s cost to the heuristic to compute the A* value for the state.

## Project Impact
This project demonstrates the practical application of search algorithms in problem-solving, showcasing the efficiency of the A* algorithm in navigating through possible states to reach a desired outcome. It emphasizes the importance of heuristics in optimizing search processes and provides a concrete example for potential applications in fields requiring precise measurements and resource management.

## Instructions to Execute Project
- Download the heapdict Library using- pip install heapdict
