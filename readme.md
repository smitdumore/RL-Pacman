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

### Q4. Epsilon Greedy

Testing the code
```
python3 gridworld.py -a q -k 100 --noise 0.0 -e 0.1
python3 gridworld.py -a q -k 100 --noise 0.0 -e 0.9
python3 autograder.py -q q4
python3 crawler.py
```

### Q5. Q-Learning and Pacman

Testing the code
```
python3 pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
python3 autograder.py -q q5
```

### Q6. Approximate Q-Learning

Testing the code
```
python3 pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid
python3 pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
python3 pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic
python3 autograder.py -q q6
```

## Project 4 

### Files to edit : 
1. bustersAgents.py 
2. inference.py
3. factorOperations.py

### Q1. Bayes Net Structure

Testing the code
```
python3 autograder.py -q q1
```

### Q2. Join Factors

Testing the code
```
python3 autograder.py -q q2
```

### Q3. Eliminate

Testing the code
```
python3 autograder.py -q q3
```

### Q4. Variable Elimination

Testing the code
```
python3 autograder.py -q q4
```

### Q5a. Discrete Distribution Class

Testing the code
```
python3 -m doctest -v inference.py
```

### Q5b. Observation Probability

Testing the code
```
python3 autograder.py -q q5
```

### Q6. Exact Inference Observation

Testing the code
```
python3 autograder.py -q q6
```

### Q7. Exact Inference with Time Elapse

Testing the code
```
python3 autograder.py -q q7
```

### Q8. Exact Inference Full Test

Testing the code
```
python3 autograder.py -q q8
```

### Q9. Approximate Inference Initialization and Beliefs

Testing the code
```
python3 autograder.py -q q9
```

### Q10. Approximate Inference Observation

Testing the code
```
python3 autograder.py -q q10
```

### Q11. Approximate Inference with Time Elapse

Testing the code
```
python3 autograder.py -q q11
```

## Project 5 

### Files to edit : 
1. models.py

### Q1. Perceptron

Testing the code
```
python3 autograder.py -q q1
```




