from puzzle15 import *
from node import *
import math

def heuristic_misplaced(puzzle):
    total_number_of_misplaced = 0
    for x in range(0, puzzle.number_of_rows):
        for y in range(0, puzzle.number_of_columns):
            if(puzzle.puzzle[x][y] != puzzle.goal_state[x][y]):
                total_number_of_misplaced += 1
    
    return total_number_of_misplaced

def astar_algorithm_misplaced(puzzle, send_end):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle], 0, heuristic_misplaced(puzzle))]
    solution_node = None
    max_number_of_nodes_stored = 0

    while frontier:
        #Calculate the maximum number of nodes stored in memory (frontier)
        if max_number_of_nodes_stored < len(frontier):
            max_number_of_nodes_stored = len(frontier)

        minn = math.inf
        index_of_min = 0
        for i in range(len(frontier)):
            node = frontier[i]
            if node.f < minn:
                minn = node.f
                index_of_min = i
        
        
        current = frontier.pop(index_of_min)

        if current.state.puzzle == current.state.goal_state:
            solution_node = current
            break
        
        inExpanded = False
        for expand in expanded:
            if current == expand:
                inExpanded = True
        if inExpanded:
            continue

        expanded.append(current)
        actions = current.state.get_possible_actions()
        for action in actions:
            if action[0].puzzle in expanded:
                continue
            h = heuristic_misplaced(action[0])
            g = 0
            if current.parent == None:
                g = action[1]
            else:
                g = current.g + action[1]
            new_path = current.path + [action[0]]
            frontier.append(Node(parent=current, state=action[0], path=new_path, g=g , h=h))

    for node in solution_node.path:
        node.render()
    print("The cost of the solution found", solution_node.g)
    print("The total number of expanded nodes : ", len(expanded))
    print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)

    send_end.send([solution_node, len(expanded), max_number_of_nodes_stored])

