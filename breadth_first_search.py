from puzzle15 import *
from node import *

def bfs_algorithm(puzzle):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle])]
    solution_node = None

    while frontier:
        current = frontier.pop(0)

        if current.state.puzzle == current.state.goal_state:
            solution_node = current
            break

        # inExpanded = False
        # for expand in expanded:
        #     if current == expand:
        #         inExpanded = True

        if isInExpanded(current, expanded):
            continue

        expanded.append(current)
        actions = current.state.get_possible_actions()
        for action in actions:
            # inExpanded = False
            # for expand in expanded:
            #     if action[0] == expand:
            #         inExpanded = True

            # if inExpanded:
            #     continue
            if isInExpanded(action[0], expanded):
                continue

            new_path = current.path + [action[0]]
            frontier.append(
                Node(parent=current, state=action[0], path=new_path))

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
    puzzle = Puzzle15(puzzle=[[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [
                      12, 13, 14, 0]], goal_state=[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    bfs_algorithm(puzzle)


if __name__ == '__main__':
    main()
