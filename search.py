# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()
        

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""

    stack = util.Stack()
    visitedNotes = []
    startState = problem.getStartState()
    startNode = (startState, [])
    
    stack.push(startNode)
    
    while not stack.isEmpty():
        currentState, actions = stack.pop()
        
        if currentState not in visitedNotes:
            visitedNotes.append(currentState)
            if problem.isGoalState(currentState):
                return actions
            else:
                successors = problem.getSuccessors(currentState)
                for successor, action, stepCost in successors:
                    newAction = actions + [action]
                    newNode = (successor, newAction)
                    stack.push(newNode)

    return actions  
    
def breadthFirstSearch(problem):
    queue = util.Queue()
    visitedNotes = []
    startState = problem.getStartState()
    startNode = (startState, [])
    
    queue.push(startNode)
    
    while not queue.isEmpty():
        currentState, actions = queue.pop()
        
        if currentState not in visitedNotes:
            visitedNotes.append(currentState)
            if problem.isGoalState(currentState):
                return actions
            else:
                successors = problem.getSuccessors(currentState)
                for successor, action, stepCost in successors:
                    newAction = actions + [action]
                    newNode = (successor, newAction)
                    queue.push(newNode)

    return actions  

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    visitedNotes = {}
    startState = problem.getStartState()
    startNode = (startState, [], 0) #state,action,cost
    
    pq.push(startNode,0)
    
    while not pq.isEmpty():
        currentState, actions, currentCost = pq.pop()
        
        if currentState not in visitedNotes or currentCost<visitedNotes[currentState]:
            visitedNotes[currentState]=currentCost
            if problem.isGoalState(currentState):
                return actions
            else:
                successors = problem.getSuccessors(currentState)
                for successor, action, stepCost in successors:
                    newAction = actions + [action]
                    newCost=currentCost+stepCost
                    newNode = (successor, newAction, newCost)                  
                    pq.push(newNode,newCost)

    return actions  

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    
    pq = util.PriorityQueue()

    visitedNodes = [] #holds (state, cost)

    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)

    pq.push(startNode, 0)

    while not pq.isEmpty():

        #begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = pq.pop()
        #put popped node into explored list
        currentNode = (currentState, currentCost)
        visitedNodes.append((currentState, currentCost))

        if problem.isGoalState(currentState):
            return actions

        else:
            #list of (successor, action, stepCost)
            successors = problem.getSuccessors(currentState)

            #examine each successor
            for successor, action, stepCost in successors:
                newAction = actions + [action]
                newCost = problem.getCostOfActions(newAction)
                newNode = (successor, action, stepCost)

                #check if this successor has been explored
                checkVisited = False
                for visited in visitedNodes:
                    #examine each explored node tuple
                    visitedState, visitedCost = visited

                    if (successor == visitedState) and (newCost >= visitedCost):
                        checkVisited= True

                #if this successor not explored, put on frontier and explored list
                if not checkVisited:
                    pq.push(newNode, newCost + heuristic(successor, problem))
                    visitedNodes.append((successor, newCost))

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
