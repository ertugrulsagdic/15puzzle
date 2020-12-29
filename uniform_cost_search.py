from puzzle15 import *
from node import *
import math

def uniform_cost_search(puzzle):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle], 0, 0)]
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
            g = 0
            if current.parent == None:
                g = action[1]
            else:
                g = current.parent.g + action[1]
            new_path = current.path + [action[0]]
            frontier.append(Node(parent=current, state=action[0], path=new_path, g=g, h=0))


    for node in solution_node.path:
        node.render()
    print("The cost of the solution found", solution_node.g)
    print("The total number of expanded nodes : ", len(expanded))
    print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)

    return solution_node, len(expanded), max_number_of_nodes_stored
