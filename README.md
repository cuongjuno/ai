# ai
#   câu1: DFS - 10 steps
    #trạng thái tìm kiếm, tạo 1 stack dùng để lưu giữ thông tin của các trạng thái state và các           #action 
    border = util.Stack()
    #node này lưu giữ các nơi đã đi qua
    visitedNodes = []
    #khởi tạo 
    startState = problem.getStartState()
    startNode = (startState, [])
   
    stack.push(startNode)
    while not border.isEmpty():
   
        #bắt đầu bằng việc gán trạng thái hiện tại và các action bằng cách pop từ stack
        currentState, actions = border.pop()
        
        if currentState not in visitedNodes: 
            #nếu chưa xuất hiện trong mảng đã được khám phá thì cho vào mảng đã được khám phá
            visitedNodes.append(currentState)

            if problem.isGoalState(currentState):
                return actions
            else:
                # lấy node và action kế tiếp
                successors = problem.getSuccessors(currentState)
                # đẩy node tiếp theo vào frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    border.push(newNode)

    return actions






#   câu 2: tương tự nhưng thay stack bằng hàng đợi queue
#   câu 3: tương tự nhưng thay queue bằng hàng đợi ưu tiên prioity queue
    frontier = util.PriorityQueue()
   
    visitedNodes = {} 
    
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    
    frontier.push(startNode, 0)
    
    while not frontier.isEmpty():
        #begin exploring first (lowest-cost) node on frontier
        currentState, actions, currentCost = frontier.pop()
       
        if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
            #put popped node's state into explored list
            exploredNodes[currentState] = currentCost

            if problem.isGoalState(currentState):
                return actions
            else:
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.update(newNode, newCost)

    return actions
