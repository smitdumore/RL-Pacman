## Project 2 

### Files to edit :
1. multiAgents.py

### Q1. Reflex Agent
Build an evaluation function that scores actions

Testing the code
```
python3 pacman.py -p ReflexAgent -l testClassic
python3 pacman.py --frameTime 0 -p ReflexAgent -k 1
python3 pacman.py --frameTime 0 -p ReflexAgent -k 2
```

### Q2. Minimax Agent

Testing the code
```
python3 autograder.py -q q2
python3 pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python3 pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
``` 

### Q3. Alpha-Beta Pruning

Testing the code
```
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
python autograder.py -q q3
``` 

### Q4. Expectimax

Testing the code
```
python3 autograder.py -q q4
python3 pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
python3 pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
```

## Project 3 

### Files to edit :
1. valueIterationAgents.py
2. qlearningAgents.py
3. analysis.py

### Q1. Value Iteration

Testing the code
```
python3 gridworld.py -a value -i 100 -k 10
python3 gridworld.py -a value -i 5
```

### Q2. Policies

Testing the code
```
python3 autograder.py -q q2
```

### Q3. Q-learning

Testing the code
```
python3 gridworld.py -a q -k 5 -m
python3 autograder.py -q q3
```