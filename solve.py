def uniform_cost_search(start_state, goal_state):
    if start_state.checkGoalState(goal_state):
        return start_state

    search_queue = []
    search_queue.append(start_state)
    visited_states = []
    expandedCount = 0
    max_frontier_size = len(search_queue)

    while True:
        if len(search_queue) == 0:
            return "failure"

        current_node = search_queue.pop(0)
        expandedCount += 1

        if current_node.checkGoalState(goal_state):
            current_node.maxQueue = max_frontier_size
            return current_node

        visited_states.append(current_node.getMatrix().tolist())
        expanded_nodes = current_node.getChild()

        for next_node in expanded_nodes:
            if next_node.getMatrix().tolist() not in visited_states:
                next_node.expended = expandedCount
                search_queue.append(next_node)

        if len(search_queue) > max_frontier_size:
            max_frontier_size = len(search_queue)
