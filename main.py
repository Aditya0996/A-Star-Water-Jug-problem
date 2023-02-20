import math
import heapdict

'''
To read data from file
'''
def getData():
    f = open("ques.txt", "r")
    a, b = (f.readline()[:-1].split(","), f.readline())
    temp = [eval(i) for i in a]
    final = eval(b)
    jugs = [math.inf] + temp
    return jugs, final

'''
To generate the next possible states
'''
def get_next_states(state, capacities):
    next_states = []

    # fill the pitcher with water
    for i in range(1, len(state)):
        new_state = list(state)
        if new_state[i] != capacities[i]:
            new_state[i] = capacities[i]
            next_states.append(tuple(new_state))
    # empty the pitcher to ground
    for i in range(0, len(state)):
        new_state = list(state)
        if new_state[i] > 0:
            new_state[i] = 0
            next_states.append(tuple(new_state))
    # pour water from one pitcher to another
    for i in range(1, len(state)):
        for j in range(1, len(state)):
            if i != j and state[i] > 0:
                new_state = list(state)
                transfer = min(state[i], capacities[j] - state[j])
                new_state[i] -= transfer
                new_state[j] += transfer
                next_states.append(tuple(new_state))
    # empty the pitcher into the "infinite" pitcher
    for i in range(1, len(state)):
        if state[i] > 0:
            new_state = list(state)
            new_state[0] = state[0] + state[i]
            new_state[i] = 0
            next_states.append(tuple(new_state))

    return next_states

'''
To check heuristics of states
'''
def heu(cost, currentState, final):
    temp = []
    if(final<1000):
        bfsProbability = 5
    else:
        bfsProbability = 2
    total = final - currentState[0]
    jugs = currentState[1:]
    for state in jugs:
        temp.append(abs(state - total))
    return (min(temp)/bfsProbability)+cost


'''
Search for the shortest path
'''
def search(jugs, final):
    initial_state = tuple([0 for _ in range(len(jugs))])
    goal_state = tuple([final if i == 0 else 0 for i in range(len(jugs))])
    open_states = heapdict.heapdict()
    open_states[(0, initial_state, ())] = 0
    closed_states = []
    while open_states:
        # print("heuristics", open_states.peekitem()[1])
        # Choose the state with the lowest estimated cost from the open states list and mark it as the current state
        current_cost, current_state, pathTuple = open_states.popitem()[0]
        path = list(pathTuple)
        # print("current cost- ", current_cost, "path- ", path)
        path.append(current_state)
        closed_states.append(current_state)

        # If the current state is the goal state, then return the path and cost to the goal
        if current_state[0] == goal_state[0]:
            return current_cost, path

        # Generate all possible next states from the current state by filling, pouring, or emptying the jugs
        nextStates = get_next_states(current_state, jugs)

        for states in nextStates:
            if states not in closed_states and states[0] <= final:
                heuristic = heu(current_cost, states, final)
                open_states[(current_cost + 1, states, tuple(path))] = heuristic

    return -1,path


jugs, final = getData()
cost, path = search(jugs, final)
print("Cost- ", cost)
# print("path- ", path)
