# 8 Puzzle Solver


## Introduction

This is an implementation of the 8 puzzle problem, solved using the A* search algorithm. The code uses two heuristics: Manhattan Distance and Linear Conflicts, to evaluate the best path to the goal state. The goal state is represented as the array [1, 2, 3, 4, 5, 6, 7, 8, 0]. The puzzle is considered solvable if a solution exists, and unsolvable otherwise.

## File Description

+ ### bestsolution(state): 

    This function takes the input of the current states and evaluates the best path to the goal state. It returns the best solution, which is an array of the states.

+ ### all(checkarray): 
    
    This function checks for the uniqueness of the current iteration state, whether it has been previously traversed or not.
 
+ ### manhattan(puzzle, goal, size=3): 

    This function calculates the Manhattan Distance cost between each digit of the puzzle and the goal state.

+ ### misplaced_tiles(puzzle,goal): 

    This function calculates the number of misplaced tiles in the current state as compared to the goal state.

+ ### coordinates(puzzle): 

    This function identifies the coordinates of each of the goal or initial state values.

+ ### evaluvate(puzzle, goal, n): 
    This is the start of the 8 puzzle evaluation, using either Manhattan Distance or Linear Conflicts as the heuristics. It makes use of priority queues, with position as keys and f(n) as value, to sort the elements.

## Usage

  + Import the necessary libraries (from copy import deepcopy, import numpy as np, import time).

  + Define the input puzzle and the goal state.

  + Call the evaluvate function, passing the input puzzle, goal state, and the heuristics (1 for Manhattan Distance, 2 for Linear Conflicts).

  + The function will return the best solution.

## Note

The code will exit if the solution is unsolvable, which is determined if the time taken to solve the puzzle is more than 2 seconds.
