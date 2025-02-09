import numpy
import copy

class puzzle:
    def __init__(self, customMatrix, cost=0):
        self.matrix = customMatrix  # Store the current matrix state
        self.parent = None  # Keep track of the parent node
        self.depth = 0  # Depth level of the node in the search tree
        self.cost = cost  # Cost used for priority queue sorting in UCS
        self.expanded_nodes = 0  # Number of nodes expanded so far
        self.max_queue_size = 0  # Track the maximum size of the queue

    def printMatrix(self):
        for row in self.matrix:  # Print each row of the matrix
            print(row)


#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#IDEA TO IMPLEMENT EXPAND NODES FUNCTION FROM GEEKSFORGEEKS (#https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/)#
#----------------------------------------------------------------------------------------------------------------------------------------------------------#

    #Generate all possible child nodes by moving the blank space.
    def expandNodes(self):
        x, y = next((i, j) for i in range(len(self.matrix)) for j in range(len(self.matrix[i])) if self.matrix[i][j] == 0)  # Find position of blank space (0)

        def swap(x1, y1, x2, y2):
            temp = copy.deepcopy(self.matrix)  # Create a deep copy of the matrix to avoid modifying the original
            temp[x1][y1], temp[x2][y2] = temp[x2][y2], temp[x1][y1]  # Swap values to generate a new state
            return temp
        
        child_nodes = []  # List to store possible child nodes
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible moves: down, up, right, left

        for dx, dy in moves:
            nx, ny = x + dx, y + dy  # Compute new coordinates
            if 0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]):  # Check if move is within bounds
                newChild = puzzle(swap(x, y, nx, ny), cost=self.cost + 1)  # Create new puzzle state with updated cost
                newChild.parent = self  # Set current node as parent
                newChild.depth = self.depth + 1  # Increase depth
                child_nodes.append(newChild)  # Add child node to the list
        
        return child_nodes  # Return list of all possible child nodes


    #Check if the current state matches the goal state.
    def checkGoalState(self, goal):
        return numpy.array_equal(self.matrix, goal)

    #Return the current matrix state.
    def getMatrix(self):
        return self.matrix


    #Define comparison method for priority queue sorting based on cost.
    def __lt__(self, other):
        return self.cost < other.cost  # Nodes with lower cost have higher priority
