# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        
        #print("Printing Scores")
        #print(legalMoves)
        #print(scores)

        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]

        #print("Printing best indices")
        #print(bestIndices)

        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]
        #return legalMoves[0]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        "Q1"

        # Get pacman's current position
        currentPosition = currentGameState.getPacmanPosition()

        # Initialise score to zero
        score = 0

        # If next action leads to winning
        # Then high score
        if successorGameState.isWin():
            return 99999

        # If next action causes ghost and pacman to intersect
        # Then low score
        for state in newGhostStates:
            if state.getPosition() == currentPosition and state.scaredTimer == 0:
                return -99999

        # Stopping is bad because we could always be moving towards food
        if action == 'Stop':
            score -= 100

        ### Food ###
        AllFoodDistance = [util.manhattanDistance(newPos, food) for food in newFood]
        nearestFood = min(AllFoodDistance)
        # Nearest Food should have highest score
        score += int(1/nearestFood)
        # Minimise leftover food
        score -= newFood.count()
        
        ### Ghosts ###

        # current ghost states
        AllCurrentGhostDistances = [util.manhattanDistance(newPos, ghost.getPosition()) 
        for ghost in currentGameState.getGhostStates()]
        nearestCurrentGhost = min(AllCurrentGhostDistances)

        # new ghost states
        AllNewGhostDistances = [util.manhattanDistance(newPos, ghost.getPosition()) \
        for ghost in newGhostStates]
        nearestNewGhost = min(AllNewGhostDistances)

        # If action leads to ghosts getting closer
        # Then bad score 
        # If action leads to ghost going far
        # Then high score
        if nearestNewGhost < nearestCurrentGhost:
            score -= 100
        else:
            score += 200

        return successorGameState.getScore() + score

### END OF REFLEX AGENT ###

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        "Q2"

        # Pacman's turn
        # Try to maximise score
        def maxValue(state, agentIndex, depth):
            # 0 idx is the pacman
            agentIndex = 0
            legalActions = state.getLegalActions(agentIndex)

            # Base case for recurison termination
            # If empty legal actions or depth reached then call evaluation function
            if not legalActions  or depth == self.depth:
                return self.evaluationFunction(state)

            # Get max
            # Recursive call to next depth and next ghost
            maximumValue =  max(minValue(state.generateSuccessor(agentIndex, action),
            agentIndex + 1, depth + 1) for action in legalActions)

            return maximumValue

        # Ghost's turn
        # Try to minimise Pacman's score
        def minValue(state, agentIndex, depth):
            # Get number of ghosts + Pacman
            agentCount = gameState.getNumAgents()
            # get legal actions for ghosts if agentIndex != 0
            legalActions = state.getLegalActions(agentIndex)

            # Recursion base case
            if not legalActions:
                return self.evaluationFunction(state)

            # pacman is the last to move after all ghost movement
            # Recursive calls
            if agentIndex == agentCount - 1:
                # Pacman's turn
                minimumValue =  min(maxValue(state.generateSuccessor(agentIndex, action), \
                agentIndex,  depth) for action in legalActions)
            else:
                # All ghost's turn
                minimumValue = min(minValue(state.generateSuccessor(agentIndex, action), \
                agentIndex + 1, depth) for action in legalActions)

            return minimumValue

        # Driver code for Minimax
        # Pacman's turn first
        # Get legal actions for Pacman(0) 
        actions = gameState.getLegalActions(0)

        allActions = {}

        # Run Minimax from each action in actions
        # And store the outcome in allActions
        for action in actions:
            # Pacman played 'action' from actions
            # Now Ghost plays minValue with (newState, ghost index, depth=1)
            allActions[action] = minValue(gameState.generateSuccessor(0, action), 1, 1)
        
        # return best outcome action set
        return max(allActions, key=allActions.get)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        "Q3"

        def maxValue(state, agentIndex, depth, alpha, beta):
            
            agentIndex = 0
            legalActions = state.getLegalActions(agentIndex)
            
            if not legalActions  or depth == self.depth:
                return self.evaluationFunction(state)

            max_answer = -99999
            currAlpha = alpha

            for action in legalActions:
                max_answer = max( max_answer, minValue(state.generateSuccessor(agentIndex, action), 
                agentIndex + 1, depth + 1, currAlpha, beta) )
                
                if max_answer > beta:
                    return max_answer
                
                currAlpha = max(currAlpha, max_answer)
            
            return max_answer

        def minValue(state, agentIndex, depth, alpha, beta):
            
            agentCount = gameState.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)
            
            if not legalActions:
                return self.evaluationFunction(state)

            min_answer = 99999
            currBeta = beta

            # pacman is the last to move after all ghost movement
            # Recursive calls
            if agentIndex == agentCount - 1:
                # Pacman's turn
                for action in legalActions:
                    min_answer = min( min_answer, maxValue(state.generateSuccessor(agentIndex, action), 
                    agentIndex, depth, alpha, currBeta) )
                
                    if min_answer < alpha:
                        return min_answer
                
                currBeta = min(currBeta, min_answer)
                
            else:
                # All ghost's turn
                for action in legalActions:
                    min_answer =  min(min_answer, minValue(state.generateSuccessor(agentIndex, action), 
                    agentIndex + 1, depth, alpha, currBeta))
                    if min_answer < alpha:
                        return min_answer
                    currBeta = min(currBeta, min_answer)

            return min_answer

        # Driver code 
        actions = gameState.getLegalActions(0)

        alpha = -99999
        beta = 99999

        allActions = {}

        for action in actions:
            # Pacman played 'action' from actions
            # Now Ghost plays minValue with (newState, ghost index, depth=1)
            value = minValue(gameState.generateSuccessor(0, action), 1, 1, alpha, beta)
            allActions[action] = value

            #update alpha
            if value > beta:
                return action
            alpha = max(value, alpha)

        # return best outcome action set
        return max(allActions, key=allActions.get)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        "Q4"

        # Ghost's turn (chance node)
        def expValue(state, agentIndex, depth):
            # Information about the agent count and the legal actions for the index
            agentCount = gameState.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)

            # Recursion base case
            if not legalActions:
                return self.evaluationFunction(state)

        
            expectedValue = 0
            # Equal probability for each action
            probability = 1.0 / len(legalActions) 

            # pacman is the last to move after all ghost movement
            for action in legalActions:
                if agentIndex == agentCount - 1:
                    # Pacman's turn
                    currentExpValue =  maxValue(state.generateSuccessor(agentIndex, action), 
                    agentIndex,  depth)
                else:
                    # Ghost's turn
                    currentExpValue = expValue(state.generateSuccessor(agentIndex, action), 
                    agentIndex + 1, depth)

                expectedValue += currentExpValue * probability

            return expectedValue

        def maxValue(state, agentIndex, depth):
            
            agentIndex = 0
            legalActions = state.getLegalActions(agentIndex)

            # Recursion base case
            if not legalActions  or depth == self.depth:
                return self.evaluationFunction(state)

            maximumValue =  max(expValue(state.generateSuccessor(agentIndex, action), 
            agentIndex + 1, depth + 1) for action in legalActions)

            return maximumValue

        # Driver code
        actions = gameState.getLegalActions(0)
        

        allActions = {}
        for action in actions:

            allActions[action] = expValue(gameState.generateSuccessor(0, action), 1, 1)

        return max(allActions, key=allActions.get)
        

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
