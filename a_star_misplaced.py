import heapq  # Import the heap queue algorithm (priority queue)


### Calculate the number of misplaced tiles compared to the goal state. ###
def misplaced_tiles(matrix, goal):
    count = 0  # Initialize the misplaced tile counter
    for i in range(len(matrix)):  # Iterate through each row of the matrix
        for j in range(len(matrix[i])):  # Iterate through each column of the matrix
            if matrix[i][j] != goal[i][j] and matrix[i][j] != 0:  # Ignore the empty tile (0) and count misplaced tiles
                count += 1  # Increment misplaced tile count
    return count  # Return total number of misplaced tiles



#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#IDEA TO IMPLEMENT SEARCH ALGORITHMS WITH HEAPQ (MIN HEAP) AND TUPLES FROM GEEKSFORGEEKS (https://www.geeksforgeeks.org/uniform-cost-search-ucs-in-ai/)#
#REST OF THE CODE FOLLOWS SIMILAR ALGORITHM TO GENERAL ALGORITHM TAUGHT IN LECTURES AND SLIDES#
#ALL OTHER SOURCES LISTED IN THE REPORT
#----------------------------------------------------------------------------------------------------------------------------------------------------------#


### Perform A* search using the Misplaced Tiles heuristic ###
def a_star_with_misplaced_tiles(start, goal):
    if start.checkGoalState(goal):  # Check if the initial state is already the goal
        return start  # Return the start state as the solution

    searchQueue = []  # Initialize a priority queue (min-heap) to store nodes to be explored
    heapq.heappush(searchQueue, (start.cost, start))  # Push the start node with its cost into the queue
    visitedStates = []  # List to store visited states
    expanded_nodes = 0  # Counter to track the number of expanded nodes
    max_queue_size = 1  # Track the maximum queue size during execution

    while searchQueue:  # Continue while there are nodes to explore
        cost, current = heapq.heappop(searchQueue)  # Extract the node with the lowest cost from the queue
        expanded_nodes += 1  # Increment the number of expanded nodes

        if current.checkGoalState(goal):  # If the goal state is reached, return the node
            current.max_queue_size = max_queue_size  # Store the max queue size in the final node
            return current  # Return the final node as the solution

        current_state = current.getMatrix().tolist()  # Convert the current node's matrix to a list format
        visitedStates.append(current_state)  # Mark the current state as visited by adding it to the seen list

        for child in current.expandNodes():  # Generate child nodes by expanding the current node
            child_state = child.getMatrix().tolist()  # Convert the child node's matrix to a list format
            if child_state not in visitedStates:  # Only explore child nodes that haven't been visited
                child.cost = misplaced_tiles(child.getMatrix(), goal) + child.depth  # Calculate cost (heuristic + depth)
                child.expanded_nodes = expanded_nodes  # Update expanded node count for tracking
                heapq.heappush(searchQueue, (child.cost, child))  # Push child node into the priority queue

        max_queue_size = max(max_queue_size, len(searchQueue))  # Update the maximum queue size encountered

    return False  # Return False if no solution is found
