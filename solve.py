def uniform_cost_search(start, goal):
    if start.checkGoalState(goal):
        return start
    
    queue = []
    queue.append(start)
    seen = []
    expendCnt = 0
    maxQueue = len(queue)
    
    while True:
        if len(queue) == 0:
            return False
        
        current = queue.pop(0)
        expendCnt += 1
        
        if current.checkGoalState(goal):
            current.maxQueue = maxQueue   
            return current
        
        seen.append(current.getMatrix().tolist())
        child = current.getChild()
        
        for c in child:
            if c.getMatrix().tolist() not in seen:
                c.expended = expendCnt
                queue.append(c)
        
        if len(queue) > maxQueue:
            maxQueue = len(queue)