from node import *


def dfs_algorithm(puzzle, send_end):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle], 0)]
    temp_frontier = []
    solution_node = None
    max_number_of_nodes_stored = 0

    while frontier:
        #Calculate the maximum number of nodes stored in memory (frontier)
        if max_number_of_nodes_stored < len(frontier):
            max_number_of_nodes_stored = len(frontier)

        current = frontier.pop(0)
        # for node in current.path:
        #     node.render()

        # print("******")

        if current.state.puzzle == current.state.goal_state:
            solution_node = current
            break

        if isInExpanded(current, expanded):
            continue

        expanded.append(current)
        actions = current.state.get_possible_actions()
        for action in actions:
            if isInExpanded(action[0], expanded):
                continue

            if current.parent == None:
                g = action[1]
            else:
                g = current.g + action[1]

            new_path = current.path + [action[0]]
            temp_frontier.append(Node(parent=current, state=action[0], path=new_path, g=g))

        frontier = temp_frontier + frontier
        temp_frontier = []

    print("----------")
    print(solution_node.path)
    for node in solution_node.path:
        node.render()
    print("The total number of expanded nodes : ", len(expanded))
    print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)

    send_end.send([solution_node, len(expanded), max_number_of_nodes_stored])

def isInExpanded(current, expanded):
    inExpanded = False
    for expand in expanded:
        if current == expand:
            inExpanded = True

    return inExpanded