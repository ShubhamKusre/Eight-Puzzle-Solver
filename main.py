import numpy
import time
# from puzzle import puzzle
# from uniform_cost import uniform_cost_search
# from a_star_misplaced import a_star_with_misplaced_tiles
# from a_star_manhattan import a_star_with_manhattan_distance

# Utility function moved into main.py
def printMatrix(matrix):
    for m in matrix:
        print(m)
    print()

def get_puzzle_choice():
    print("\nYou select to use the default puzzle. \nType '1' for Depth 0  \nType '2' for Depth 2 \nType '3' for Depth 4 \nType '4' for Depth 8 \nType '5' for Depth 16 \nType '6' for Depth 20 \nType '7' for Depth 24. \n**Error input will automatically use Depth 16.\n")
    choicePuz = int(input())
    puzzles = [puzzle0, puzzle2, puzzle4, puzzle8, puzzle16, puzzle20, puzzle24]
    return puzzles[choicePuz - 1] if 1 <= choicePuz <= 7 else puzzle16

def create_custom_puzzle():
    print("\nYou select to create your own puzzle. Please enter your puzzle, use a zero to represent the blank. Enter each row, use space between numbers. Example: 1 2 3")
    print("please enter the first row")
    firstRow = list(map(int, input().split()))
    print("please enter the second row")
    secondRow = list(map(int, input().split()))
    print("please enter the third row")
    thirdRow = list(map(int, input().split()))
    return numpy.array([firstRow, secondRow, thirdRow])

def select_algorithm(start, goal):
    print("\nEnter your choice of algorithm: \nType '1' for Uniform Cost Search \nType '2' for A* with the Misplaced Tile heuristic \nType '3' for A* with the Manhattan distance heuristic.")
    choice = int(input())
    print()
    
    algorithms = {
        1: ("Uniform Cost Search", uniform_cost_search),
        2: ("A* with the Misplaced Tile heuristic", a_star_with_misplaced_tiles),
        3: ("A* with the Manhattan distance heuristic", a_star_with_manhattan_distance)
    }
    
    if choice in algorithms:
        print(f"You select to use {algorithms[choice][0]}")
        startTime = time.time()
        result = algorithms[choice][1](start, goal)
        endTime = time.time()
        display_results(result, endTime - startTime)
    

def display_results(result, time_taken):
    nodeExpand = result.expanded_nodes
    depth = result.depth
    max_queue_size = result.max_queue_size
    
    path = []
    while result.parent:
        path.append((result.getMatrix(), result.depth, result.expanded_nodes))
        result = result.parent
    path.append((result.getMatrix(), result.depth, result.expanded_nodes))
    path.reverse()
    
    for p in path:
        print(f"The best state to expand with a g(n): {p[1]} is:")
        printMatrix(p[0])
    
    print("Goal State! \n")
    print(f"Solution path: {depth}\nNumber of nodes expanded: {nodeExpand}\nMax queue size: {max_queue_size}")
    print(f"Algorithm finished! Taking {time_taken} seconds \n \n")

def main():
    global puzzle0, puzzle2, puzzle4, puzzle8, puzzle16, puzzle20, puzzle24, goal
    
    goal = numpy.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])

    puzzle0 = numpy.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])

    puzzle2 = numpy.array([
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ])

    puzzle4 = numpy.array([
        [1, 2, 3],
        [5, 0, 6],
        [4, 7, 8]
    ])

    puzzle8 = numpy.array([
        [1, 3, 6],
        [5, 0, 2],
        [4, 7, 8]
    ])

    puzzle16 = numpy.array([
        [1, 6, 7],
        [5, 0, 3],
        [4, 8, 2]
    ])

    puzzle20 = numpy.array([
        [7, 1, 2],
        [4, 8, 5],
        [6, 3, 0]
    ])

    puzzle24 = numpy.array([
        [0, 7, 2],
        [4, 6, 1],
        [3, 5, 8]
    ])
    
    print("Welcome to my 8-Puzzle Solver: \nType '1' to use a default puzzle  \nType '2' to create your own.")
    choice = int(input())
    
    if choice == 1:
        print("You select to use the default puzzle.")
        puzzleChoice = get_puzzle_choice()
    elif choice == 2:
        puzzleChoice = create_custom_puzzle()
    else:
        print("Invalid choice, using default Depth 16 puzzle.")
        puzzleChoice = puzzle16
    
    printMatrix(puzzleChoice)
    start = puzzle(puzzleChoice)
    select_algorithm(start, goal)
    
if __name__ == "__main__":
    main()
