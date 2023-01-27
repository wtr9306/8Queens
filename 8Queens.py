import random

# Function to check if the current state is a goal state (no queens are in conflict)
def is_goal_state(state):
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j]:
                return False
            if abs(i-j) == abs(state[i]-state[j]):
                return False
    return True

# Function to generate all possible neighbor states by moving each column's queen through the rows of its column
def generate_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i] != j:
                new_state = state.copy()
                new_state[i] = j
                neighbors.append(new_state)
    return neighbors

# Heuristic function to evaluate the current state
def heuristic(state):
    h = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j]:
                h += 1
            if abs(i-j) == abs(state[i]-state[j]):
                h += 1
    return h

# Function to output the state in a grid style using 0s (empty) and 1s (queen)
def print_state(state):
    for i in range(len(state)):
        row = ['0'] * len(state)
        row[state[i]] = '1'
        print(row)

# Main function to solve the 8-Queens problem using Hill-Climbing with random restarts
def solve_8_queens():
    # Initialize variables to keep track of restarts and state changes
    restarts = 0
    state_changes = 0
    # Generate a random starting state
    current_state = [random.randint(0, 7) for _ in range(8)]
    while not is_goal_state(current_state):
        # Check if current state is a goal state
        if is_goal_state(current_state):
            print("Solution found:")
            print_state(current_state)
            print("Restarts:", restarts)
            print("State changes:", state_changes)
            return
        # Generate all possible neighbor states
        neighbors = generate_neighbors(current_state)
        # Evaluate the heuristic of each neighbor state
        best_neighbor = None
        best_neighbor_heuristic = float('inf')
        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < best_neighbor_heuristic:
                best_neighbor = neighbor
                best_neighbor_heuristic = h
        # Check if a better state was found
        if best_neighbor_heuristic < heuristic(current_state):
            print("Generating neighbor state:")
            print_state(best_neighbor)
            print("Heuristic:", best_neighbor_heuristic)
            print("Neighbors with lower heuristics: 1")
            current_state = best_neighbor
