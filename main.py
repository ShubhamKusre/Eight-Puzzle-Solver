import numpy
import time
from puzzle import puzzle
from uniform_cost import uniform_cost_search
from a_star_misplaced import a_star_with_misplaced_tiles
from a_star_manhattan import a_star_with_manhattan_distance
from a_star_misplaced import misplaced_tiles
from a_star_manhattan import manhattan_distance

# Function to print a given matrix (puzzle state)
def printMatrix(matrix):
    for m in matrix:
        print(m)
    print()

# Function to let the user select a predefined puzzle depth
def get_puzzle_choice():
    print("\nSelect a default puzzle depth:")
    print("1: Depth 0\n2: Depth 2\n3: Depth 4\n4: Depth 8\n5: Depth 16\n6: Depth 20\n7: Depth 24")
    choicePuz = int(input())
    puzzles = [puzzle0, puzzle2, puzzle4, puzzle8, puzzle16, puzzle20, puzzle24]
    return puzzles[choicePuz - 1] if 1 <= choicePuz <= 7 else puzzle16  # Default to Depth 16

# Function to allow the user to create a custom puzzle
def create_custom_puzzle():
    print("\nCreate your own puzzle (use 0 to represent the blank space). Enter rows one by one:")
    firstRow = list(map(int, input().split()))
    secondRow = list(map(int, input().split()))
    thirdRow = list(map(int, input().split()))
    return numpy.array([firstRow, secondRow, thirdRow])

# Function to select and run a search algorithm
def select_algorithm(start, goal):
    print("\nSelect an algorithm:")
    print("1: Uniform Cost Search\n2: A* with Misplaced Tile heuristic\n3: A* with Manhattan Distance heuristic")
    choice = int(input())
    
    algorithms = {
        1: ("Uniform Cost Search", uniform_cost_search),
        2: ("A* with Misplaced Tile heuristic", a_star_with_misplaced_tiles),
        3: ("A* with Manhattan Distance heuristic", a_star_with_manhattan_distance)
    }
    
    if choice in algorithms:
        print(f"Using {algorithms[choice][0]}")
        startTime = time.time()
        result = algorithms[choice][1](start, goal)
        endTime = time.time()
        display_results(result, endTime - startTime, choice, goal)

# Function to display the results including path, depth, and nodes expanded
def display_results(result, time_taken, choice, goal):
    nodeExpand = result.expanded_nodes  # Track number of expanded nodes
    depth = result.depth  # Solution depth
    max_queue_size = result.max_queue_size  # Maximum queue size encountered
    
    path = []  # Store solution path
    while result.parent:
        state = result.getMatrix()
        g_n = result.depth  # Cost so far
        h_n = misplaced_tiles(state, goal) if choice == 2 else manhattan_distance(state, goal) if choice == 3 else 0  # Compute heuristic if applicable
        path.append((state, g_n, h_n))
        result = result.parent
    path.append((result.getMatrix(), 0, 0))
    path.reverse()
    
    for p in path:
        print(f"The best state to expand with g(n) = {p[1]} and h(n) = {p[2]} is:")
        printMatrix(p[0])
    
    print("Goal State Reached!\n")
    print(f"Solution depth: {depth}\nNodes expanded: {nodeExpand}\nMax queue size: {max_queue_size}")
    print(f"Execution time: {time_taken} seconds\n\n")

# Main function to initialize the puzzle and handle user interaction
def main():
    global puzzle0, puzzle2, puzzle4, puzzle8, puzzle16, puzzle20, puzzle24, goal
    
    # Define goal state and default puzzle configurations at different depths
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
    
    print("Welcome to the 8-Puzzle Solver:")
    print("1: Use a default puzzle\n2: Create your own puzzle")
    choice = int(input())
    
    if choice == 1:
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
