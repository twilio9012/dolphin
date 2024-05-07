g=0
def print_board(elements):
    for i in range(9):
        if i%3 == 0:
            print()
        if elements[i]==-1:
            print("_", end = " ")
        else:
            print(elements[i], end = " ")
    print()

def solvable(start):
    inv=0

    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i+1,9):
            if start[j]==-1:
                continue
            if start[i]>start[j]:
                inv+=1
    if inv%2==0:
        return True
    return False

def heuristic(start,goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j-i))//3 + (abs(j-i))%3
    return h + g

def moveleft(start,position):
    start[position],start[position-1]= start[position-1],start[position]

def moveright(start,position):
    start[position],start[position+1]= start[position+1],start[position]

def moveup(start,position):
    start[position],start[position-3]= start[position-3],start[position]

def movedown(start,position):
    start[position],start[position+3]= start[position+3],start[position]


def movetile(start,goal):
    emptyat= start.index(-1)
    row = emptyat//3
    col = emptyat%3
    t1,t2,t3,t4 = start[:],start[:],start[:],start[:]
    f1,f2,f3,f4 = 100,100,100,100

    if col -1 >=0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col+1<3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 <3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row-1>=0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2,f3,f4)

    if f1==min_heuristic:
        moveleft(start, emptyat)
    elif f2==min_heuristic:
        moveright(start, emptyat)
    elif f3==min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)
        
        
def solveEight(start,goal):
    global g
    g+=1
    movetile(start,goal)
    print_board(start)
    f = heuristic(start,goal)
    if f == g:
        print("Solved in {} moves".format(f))
        return

    solveEight(start,goal)


def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state:(Enter -1 for empty):")
    for i in range(9):
        start.append(int(input()))

    print("Enter the goal state:(Enter -1 for empty):")
    for i in range(9):
        goal.append(int(input()))

    print_board(start)

    # To check if solvable
    if solvable(start):
        solveEight(start,goal)
        print("Solved in {} moves".format(g))
    else:
        print("Not possible to solve")


if __name__ == '__main__':
    main()



# Test Cases
# 
# 1
# 2
# 3
# -1
# 4 
# 6
# 7 
# 5 
# 8 

# 1 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8
# -1


"""
This code is an implementation of the A* algorithm to solve the 8-puzzle problem, a classic problem in artificial intelligence and puzzle solving. Let's break down the code step by step:

1. **print_board(elements)**:
   - This function is used to print the current state of the puzzle board.
   - It iterates over the elements of the board and prints them in a 3x3 grid format. If an element is -1 (indicating an empty space), it prints "_".

2. **solvable(start)**:
   - This function checks if the given initial state of the puzzle is solvable.
   - It calculates the number of inversions in the initial state. An inversion occurs when a tile precedes another tile with a lower number.
   - If the total number of inversions is even, the puzzle is solvable; otherwise, it is unsolvable.

3. **heuristic(start, goal)**:
   - This function calculates the heuristic value (estimated cost) from the current state to the goal state.
   - It calculates the Manhattan distance of each tile from its goal position and sums them up. The Manhattan distance is the sum of the horizontal and vertical distances between the current position and the goal position of each tile.
   - Additionally, it increments the heuristic value (`h`) by the number of moves required to move the tile to its goal position.

4. **moveleft(start, position)**, **moveright(start, position)**, **moveup(start, position)**, **movedown(start, position)**:
   - These functions perform the movements of the empty space (represented by -1) to the left, right, up, and down, respectively.

5. **movetile(start, goal)**:
   - This function generates possible moves for the empty space and selects the move with the minimum heuristic value.
   - It creates four temporary copies of the current state and tries to move the empty space in all four directions.
   - It calculates the heuristic value for each move and selects the one with the minimum value.

6. **solveEight(start, goal)**:
   - This function recursively solves the puzzle using the A* algorithm.
   - It increments the global variable `g` representing the number of moves made.
   - It calls `movetile` to generate the next move and then recursively calls itself until the goal state is reached.

7. **main()**:
   - This function serves as the entry point of the program.
   - It prompts the user to input the initial state and the goal state of the puzzle.
   - It checks if the initial state is solvable.
   - If solvable, it calls `solveEight` to solve the puzzle and prints the solution.

8. **Execution**:
   - The code execution starts from the `main()` function.
"""
