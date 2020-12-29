from node import *
import math


# the number of steps to take with without diagonal move - the number of steps saved using diagonal move
def heuristic_diagonal_distance(puzzle):
    diagonal_distance = 0
    d1 = 1
    d2 = 3

    for x in range(0, puzzle.number_of_rows):
        for y in range(0, puzzle.number_of_columns):
            for x1 in range(0, puzzle.number_of_rows):
                for y1 in range(0, puzzle.number_of_columns):
                    if puzzle.goal_state[x1][y1] == puzzle.puzzle[x][y]:
                        dx = abs(x - x1)
                        dy = abs(y - y1)
                        diagonal_distance += d1 * max(dx, dy) + (d2 - d1) * min(dx, dy)
    return diagonal_distance


def astar_algorithm_bonus_diagonal_distance(puzzle):
    explored = []
    frontier = [Node(None, puzzle, [puzzle], 0, heuristic_diagonal_distance(puzzle))]
    solution_node = None
    max_number_of_nodes_stored = 0

    while frontier:
        # Calculate the maximum number of nodes stored in memory (frontier)
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

        in_explored = False
        for expand in explored:
            if current == expand:
                in_explored = True
        if in_explored:
            continue

        explored.append(current)
        actions = current.state.get_possible_actions()
        for action in actions:
            h = heuristic_diagonal_distance(action[0])
            if current.parent == None:
                g = action[1]
            else:
                g = current.parent.g + action[1]
            new_path = current.path + [action[0]]
            frontier.append(Node(parent=current, state=action[0], path=new_path, g=g, h=h))

    for node in solution_node.path:
        node.render()
    print("The cost of the solution found", solution_node.g)
    print("The total number of expanded nodes : ", len(explored))
    print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)

