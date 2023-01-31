from copy import deepcopy
import numpy as np
import time

# takes the input of current states and evaluvates the best path to goal state
def bestsolution(state):
    bestsol = np.array([], int).reshape(-1, 9)
    count = len(state) - 1
    while count != -1:
        bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
        count = (state[count]['parent'])
    return bestsol.reshape(-1, 3, 3)

       
# this function checks for the uniqueness of the iteration(it) state, weather it has been previously traversed or not.
def all(checkarray):
    set=[]
    for it in set:
        for checkarray in it:
            return 1
        else:
            return 0


# calculate Manhattan distance cost between each digit of puzzle(start state) and the goal state
def manhattan(puzzle, goal, size=3):
    a = abs(puzzle // size - goal // size)
    b = abs(puzzle % size - goal % size)
    mhcost = a + b
    return sum(mhcost[1:])




# will calcuates the number of misplaced tiles in the current state as compared to the goal state
def misplaced_tiles(puzzle,goal):
    mscost = np.sum(puzzle != goal) - 1
    return mscost if mscost > 0 else 0
       


#3[on_true] if [expression] else [on_false] 


# will indentify the coordinates of each of goal or initial state values
def coordinates(puzzle):
    pos = np.array(range(9))
    for p, q in enumerate(puzzle):
        pos[q] = p
    return pos



# start of 8 puzzle evaluvation, using Manhattan heuristics 
def evaluvate(puzzle, goal, n):
    steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('position', list),('head', int)])

    dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
    
     # initializing the parent, gn and hn, where hn is manhattan distance function call 
    costg = coordinates(goal)
    parent = -1
    gn = 0
    if n==1:
        hn = manhattan(coordinates(puzzle), costg)
    else:
        hn = linear_conflicts_manhattan(coordinates(puzzle), costg)
    state = np.array([(puzzle, parent, gn, hn)], dtstate)

# We make use of priority queues with position as keys and fn as value.
    dtpriority = [('position', int),('fn', int)]
    priority = np.array( [(0, hn)], dtpriority)



    while 1:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])     
        position, fn = priority[0]                                                 
        priority = np.delete(priority, 0, 0)  
        # sort priority queue using merge sort,the first element is picked for exploring remove from queue what we are exploring                   
        puzzle, parent, gn, hn = state[position]
        puzzle = np.array(puzzle)
        # Identify the blank square in input 
        blank = int(np.where(puzzle == 0)[0])       
        gn = gn + 1                              
        c = 1
        start_time = time.time()
        for s in steps:
            c = c + 1
            if blank not in s['position']:
                # generate new state as copy of current
                openstates = deepcopy(puzzle)                   
                openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]             
                # The all function is called, if the node has been previously explored or not
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():    
                    end_time = time.time()
                    if (( end_time - start_time ) > 2):
                        print(" The 8 puzzle is unsolvable ! \n")
                        exit 
                    # calls the manhattan function to calcuate the cost 
                    if n==1:
                        hn = manhattan(coordinates(puzzle), costg)
                    else:
                        hn = linear_conflicts_manhattan(coordinates(puzzle), costg)   
                     # generate and add new state in the list                    
                    q = np.array([(openstates, position, gn, hn)], dtstate)         
                    state = np.append(state, q, 0)
                    # f(n) is the sum of cost to reach node and the cost to rech fromt he node to the goal state
                    fn = gn + hn                                        
            
                    q = np.array([(len(state) - 1, fn)], dtpriority)    
                    priority = np.append(priority, q, 0)
                      # Checking if the node in openstates are matching the goal state.  
                    if np.array_equal(openstates, goal):                              
                        print(' The 8 puzzle is solvable ! \n')
                        return state, len(priority)
        
                        
    return state, len(priority)


def linear_conflicts_manhattan(candidate, solved, size=3):
    def count_conflicts(candidate_row, solved_row, size, ans=0):
        counts = [0 for x in range(size)]
        for i, tile_1 in enumerate(candidate_row):
            if tile_1 in solved_row and tile_1 != 0:
                solved_i = solved_row.index(tile_1)
                for j, tile_2 in enumerate(candidate_row):
                    if tile_2 in solved_row and tile_2 != 0 and i != j:
                        solved_j = solved_row.index(tile_2)
                        if solved_i > solved_j and i < j:
                            counts[i] += 1
                        if solved_i < solved_j and i > j:
                            counts[i] += 1
        if max(counts) == 0:
            return ans * 2
        else:
            i = counts.index(max(counts))
            candidate_row[i] = -1
            ans += 1
            return count_conflicts(candidate_row, solved_row, size, ans)

    res = manhattan(candidate, solved, size)
    candidate_rows = [[] for y in range(size)]
    candidate_columns = [[] for x in range(size)]
    solved_rows = [[] for y in range(size)]
    solved_columns = [[] for x in range(size)]
    for y in range(size):
        for x in range(size):
            idx = (y * size) + x
            candidate_rows[y].append(candidate[idx])
            candidate_columns[x].append(candidate[idx])
            solved_rows[y].append(solved[idx])
            solved_columns[x].append(solved[idx])
    for i in range(size):
        res += count_conflicts(candidate_rows[i], solved_rows[i], size)
    for i in range(size):
        res += count_conflicts(candidate_columns[i], solved_columns[i], size)
    return res

# ----------  Program start -----------------



 # User input for initial state 
puzzle = []
print(" Input vals from 0-8 for start state ")
for i in range(0,9):
    x = int(input("enter vals :"))
    puzzle.append(x)

 # User input of goal state       
goal = []
print(" Input vals from 0-8 for goal state ")
for i in range(0,9):
    x = int(input("Enter vals :"))
    goal.append(x)

n = int(input("1. Manhattan distance \n2. Linear Conflict and Manhattan distance\n"))


state, visited = evaluvate(puzzle, goal, n) 
bestpath = bestsolution(state)
print(str(bestpath).replace('[', ' ').replace(']', ''))
totalmoves = len(bestpath) - 1
print('Steps to reach goal:',totalmoves)
visit = len(state) - visited
print('Total nodes visited: ',visit, "\n")
print('Total generated:', len(state))


    