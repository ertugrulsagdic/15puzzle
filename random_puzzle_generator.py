from puzzle15 import *
import random

def generate_random_instance_of_puzzle(goal_puzzle, depth):
    # expanded = []
    # frontier = [Node(None, goal_puzzle, [puzzle])]
    check = []

    current_puzzle = goal_puzzle
    
    for i in range(depth):
        actions = current_puzzle.get_possible_actions()
        random_action = random.choice(actions)
        if random_action[0].puzzle in check:
            i -= 1
        else:
            current_puzzle = random_action[0]
            check.append(random_action[0].puzzle)
        
    return current_puzzle


goal_puzzle = Puzzle15(puzzle=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])

print(generate_random_instance_of_puzzle(goal_puzzle, 2).render())
        

