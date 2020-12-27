from puzzle15 import *
from node import *
import math

def heuristic_city_block_distance(puzzle):
    total_distance = 0
    for x in range(0, puzzle.number_of_rows):
        for y in range(0, puzzle.number_of_columns):
            total_distance += puzzle.distance_to_goal_state(puzzle.puzzle[x][y])
    
    return total_distance

def astar_algorithm(puzzle):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle], 0, heuristic_city_block_distance(puzzle))]
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
            h = heuristic_city_block_distance(action[0])
            g = 0
            if current.parent == None:
                g = action[1]
            else:
                g = current.parent.g + action[1]
            new_path = current.path + [action[0]]
            frontier.append(Node(parent=current, state=action[0], path=new_path, g=g , h=h))

    print(solution_node.path)
    for node in solution_node.path:
        node.render()
    print("The total number of expanded nodes : ", len(expanded))
    print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)

def main():
    puzzle = Puzzle15(puzzle=[[1, 3, 5, 4], [2, 13, 14, 15], [11, 12, 9, 6], [0, 10, 8, 7]], goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])
    astar_algorithm(puzzle)

if __name__ == '__main__':
    main()


