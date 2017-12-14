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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    :type problem: object
    """
    "*** YOUR CODE HERE ***"
    pacStack = util.Stack()      # created stack as depth first search is LIFO
    visited = []                 # visited array
    path = util.Stack()          # this stack will contain our final path

    node = {"state":problem.getStartState(),"path":None,"parent":None}# creating dictionary which will keep location,path traversed , and parent node
    pacStack.push(node)  # pushed first node in stack

    while not pacStack.isEmpty():
        node =pacStack.pop()
        state = node["state"]
        if state in visited:            # if state is visited no action required so continuing the loop for next value
            continue

        if problem.isGoalState(state)==True:
            while node["path"] != None:        # if we have reached our goal state than going from goal to start state using parent
                path.push(node["path"])        # used stack as in end it will give us resulted path from start to goal
                node = node["parent"]
            break

        visited.append(state)       # Marking the state as visited

        for neighbours in problem.getSuccessors(state):   # now checking successors
            stat, direction, cost = neighbours
            if not stat in visited:
                nextNewNode={"state":stat,"path":direction,"parent":node}    # if successors is not in visited than added it to stack
                # in above step parent will be our previous node
                pacStack.push(nextNewNode)

    result = []
    while not path.isEmpty():
        result.append(path.pop())    # popping out value from path to gives us our final result
    return result


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    pacStack = util.Queue()      # created Queue as breath first search is FIFO
    visited = []                 # visited array
    path = util.Stack()          # this stack will contain our final path

    node = {"state":problem.getStartState(),"path":None,"parent":None}   # creating dictionary which will keep location,path traversed , and parent node
    pacStack.push(node)  # pushed first node in Queue

    while not pacStack.isEmpty():
        node =pacStack.pop()
        state = node["state"]
        if state in visited:            # if state is visited no action required so continuing the loop for next value
            continue

        if problem.isGoalState(state)==True:
            while node["path"] != None:        # if we have reached our goal state than going from goal to start state using parent
                path.push(node["path"])        # used stack as in end it will give us resulted path from start to goal
                node = node["parent"]
            break

        visited.append(state)       # Marking the state as visited

        for neighbours in problem.getSuccessors(state):   # now checking successors
            stat, direction, cost = neighbours
            if not stat in visited:
                nextNewNode={"state":stat,"path":direction,"parent":node}    # if successors is not in visited than added it to stack
                # in above step parent will be our previous node
                pacStack.push(nextNewNode)

    result = []
    while not path.isEmpty():
        result.append(path.pop())    # popping out value from path to gives us our final result
    return result



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pacStack = util.PriorityQueue()  # created priority Queue as uniform cost search is least total cost first search
    visited = []  # visited array

    path = util.Stack()  # this stack will contain our final path

    node = {"state": problem.getStartState(), "path": None,"parent": None,"cost":0}  # creating dictionary which will keep location,path traversed , and parent node
     # initally cost is 0
    pacStack.push(node,node["cost"])  # passing node with its priority(which is total cost) other wise it will be normal push

    while not pacStack.isEmpty():
        node = pacStack.pop()
        state = node["state"]
        if state in visited:  # if state is visited no action required so continuing the loop for next value
            continue

        if problem.isGoalState(state) == True:
            while node["path"] != None:          # if we have reached our goal state than going from goal to start state using parent
                path.push(node["path"])  # used stack as in end it will give us resulted path from start to goal
                node = node["parent"]
            break

        visited.append(state)  # Marking the state as visited

        for neighbours in problem.getSuccessors(state):  # now checking successors
            stat, direction, cost = neighbours
            if not stat in visited:
                currentCost=cost+node["cost"]   # added previous cost with current cost as ucs is all about total cost
                nextNewNode = {"state": stat, "path": direction,"parent": node,"cost":currentCost}  # if successors is not in visited than added it to stack
                # in above step parent will be our previous node

                pacStack.push(nextNewNode,nextNewNode["cost"])

    result = []
    while not path.isEmpty():
        result.append(path.pop())  # popping out value from path to gives us our final result
    return result


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    pacStack = util.PriorityQueue()  # created priority Queue as aStarSearch is based on (cost+heuristic) priority
    visited = []  # visited array

    path = util.Stack()  # this stack will contain our final path
    startState=problem.getStartState()
    heur= heuristic(startState, problem)  # using the heristci function provided to calculate heruistic
    node = {"state": startState, "path": None, "parent": None,"heuristic":heur, "cost": 0}  # creating dictionary which will keep location,path traversed , and parent node
    pacStack.push(node, node["cost"]+node["heuristic"])  # cost+heuristic

    while not pacStack.isEmpty():
        node = pacStack.pop()
        state = node["state"]
        if state in visited:  # if state is visited no action required so continuing the loop for next value
            continue

        if problem.isGoalState(state) == True:
            while node["path"] != None:   # if we have reached our goal state than going from goal to start state using parent
                path.push(node["path"])  # used stack as in end it will give us resulted path from start to goal
                node = node["parent"]
            break

        visited.append(state)  # Marking the state as visited

        for neighbours in problem.getSuccessors(state):  # now checking successors
            stat, direction, cost = neighbours
            if not stat in visited:
                currentCost=cost+node["cost"]   # added previous cost with current cost as ucs is all about total cost
                heurs = heuristic(stat, problem)  # calculating heuristic
                nextNewNode = {"state": stat, "path": direction,"parent": node,"heuristic":heurs,"cost":currentCost}  # if successors is not in visited than added it to stack
                pacStack.push(nextNewNode, nextNewNode["cost"]+nextNewNode["heuristic"])  # passing next node with priority as totalCost+Heuristic

    result = []
    while not path.isEmpty():
        result.append(path.pop())  # popping out value from path to gives us our final result
    return result


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
