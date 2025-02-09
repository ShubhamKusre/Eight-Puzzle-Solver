import heapq
import numpy as np

def manhattan_distance(matrix, goal):
    matrix = np.array(matrix)  # Convert to NumPy array for efficient indexing
    goal = np.array(goal)
    
    distance = 0
    for num in range(1, 9):  # Loop through tile values 1 to 8 (excluding blank)
        x1, y1 = np.argwhere(matrix == num)[0]  # Get position of tile in current state
        x2, y2 = np.argwhere(goal == num)[0]    # Get position of tile in goal state
        distance += abs(x1 - x2) + abs(y1 - y2)  # Compute Manhattan distance

    return distance


#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#IDEA TO IMPLEMENT SEARCH ALGORITHMS WITH HEAPQ (MIN HEAP) AND TUPLES FROM GEEKSFORGEEKS (https://www.geeksforgeeks.org/uniform-cost-search-ucs-in-ai/)#
#REST OF THE CODE FOLLOWS SIMILAR ALGORITHM TO GENERAL ALGORITHM TAUGHT IN LECTURES AND SLIDES#
#ALL OTHER SOURCES LISTED IN THE REPORT
#----------------------------------------------------------------------------------------------------------------------------------------------------------#


def a_star_with_manhattan_distance(start, goal):
    if start.checkGoalState(goal):  # Check if the initial state is already the goal
        return start

    queue = []  # Initialize a priority queue (min-heap)
    heapq.heappush(queue, (start.cost, start))  # Push the start node with its cost into the queue
    seen = []  # List to store visited states
    expanded_nodes = 0  # Counter to track the number of expanded nodes
    max_queue_size = 1  # Track the maximum queue size during execution

    while queue:  # Continue while there are nodes in the queue
        cost, current = heapq.heappop(queue)  # Extract the node with the lowest cost
        expanded_nodes += 1  # Increment the number of expanded nodes

        if current.checkGoalState(goal):  # If the goal state is reached, return the node
            current.max_queue_size = max_queue_size  # Store the max queue size in the final node
            return current  # Return the final node as the solution

        current_state = current.getMatrix().tolist()  # Convert the current node's matrix to a list format
        seen.append(current_state)  # Mark the current state as visited by adding it to the seen list

        for child in current.expandNodes():  # Generate child nodes by expanding the current node
            child_state = child.getMatrix().tolist()  # Convert the child node's matrix to a list format
            if child_state not in seen:  # Only explore child nodes that haven't been visited
                child.cost = manhattan_distance(child.getMatrix(), goal) + child.depth  # Calculate cost (heuristic + depth)
                child.expanded_nodes = expanded_nodes  # Update expanded node count for tracking
                heapq.heappush(queue, (child.cost, child))  # Push child node into the priority queue

        max_queue_size = max(max_queue_size, len(queue))  # Update the maximum queue size encountered

    return False  # Return False if no solution is found
