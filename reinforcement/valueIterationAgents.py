# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        """
          Run the value iteration algorithm. Note that in standard
          value iteration, V_k+1(...) depends on V_k(...)'s.
        """
        "*** YOUR CODE HERE ***"
        
        for iteration in range(self.iterations):
            table_of_values = util.Counter()

            # Visiting all boxes in the grid
            for state in self.mdp.getStates():
                
                if self.mdp.isTerminal(state):
                    table_of_values[state] = 0
                else:
                    maxVal = -99999

                    # get all successor actions from current state
                    actions = self.mdp.getPossibleActions(state)

                    # find value for all successor actions
                    for action in actions:
                        
                        T = self.mdp.getTransitionStatesAndProbs(state, action)
                        value = 0

                        for State_and_Prob in T:
                            # State_and_Prob[1] -> returns the transition probability from s to s' by taking action 
                            # State_and_Prob[0] -> returns the state s'
                            # self.values[State_and_Prob[0]] -> recursive call to get value of s'

                            value += State_and_Prob[1] * (self.mdp.getReward(state, action, State_and_Prob[1]) 
                                                                        + self.discount * self.values[State_and_Prob[0]])

                        # update max value for current state
                        maxVal = max(value, maxVal)

                    if maxVal != -99999:
                        table_of_values[state] = maxVal

            self.values = table_of_values


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        # NOTE : action and state is passed is as a parameter
        # So this funciton will return a value of a specific aciton taken from state 's'
        # which is nothing but the Q value of the state
        
        qValue = 0

        for State_and_Prob in self.mdp.getTransitionStatesAndProbs(state, action):

            qValue += State_and_Prob[1] * (self.mdp.getReward(state, action, State_and_Prob[1]) 
                                                    + self.discount * self.values[State_and_Prob[0]])

        return qValue

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        
        # This is policy extraction 
        
        # We cannot take any action from terminal state
        if self.mdp.isTerminal(state):
            return None

         
        actions = self.mdp.getPossibleActions(state)
        
        allActions = {}
        for action in actions:
            allActions[action] = self.computeQValueFromValues(state, action)

        # We calculated the Q values from the state passed as parameter
        # Now we return the action that gav rise to the max value
        # argmax
        return max(allActions, key=allActions.get)

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
