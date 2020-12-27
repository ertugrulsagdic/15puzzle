from puzzle15 import *
from node import *


def dfs_algorithm(puzzle):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle])]
    temp_frontier = []
    solution_node = None

    while frontier:
        current = frontier.pop(0)

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

            new_path = current.path + [action[0]]
            temp_frontier.append(Node(parent=current, state=action[0], path=new_path))

        # print(frontier)
        # print(temp_frontier)
        frontier = temp_frontier + frontier
        # print(frontier)
        temp_frontier = []
        # print("----------")
    print(solution_node.path)
    for node in solution_node.path:
        node.render()


def isInExpanded(current, expanded):
    inExpanded = False
    for expand in expanded:
        if current == expand:
            inExpanded = True

    return inExpanded


def main():
    puzzle = Puzzle15(puzzle=[[15, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [
                      12, 13, 14, 0]], goal_state=[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    dfs_algorithm(puzzle)


if __name__ == '__main__':
    main()
