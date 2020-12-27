from puzzle15 import *
class Node:
    def __init__(self, parent=None, state=None, path=None, depth=0):
        self.parent = parent
        self.state = state
        self.path = path
        self.depth = depth

    def __eq__(self, obj):
        try:
            if(self.parent == obj.parent and self.state == obj.state):
                return True
            else:
                return False
        except:
            return False

def iterative_deepening_algorithm(puzzle):
    depth = 0
    depth_limit = 1
    solution_node = None
    isSolved = False
    while 1:
        expanded = []
        frontier = [Node(None, puzzle, [puzzle], depth)]
        temp_frontier = []

        while frontier:

            current = frontier.pop(0)
            # for node in current.path:
            #     node.render()
            # print(current.depth)
            # print("******")

            if current.state.puzzle == current.state.goal_state:
                isSolved = True
                solution_node = current
                break

            if isInExpanded(current, expanded):
                continue

            expanded.append(current)
            actions = current.state.get_possible_actions()

            if(current.depth != depth_limit):
                depth = current.depth + 1
            else:
                continue

            for action in actions:
                if isInExpanded(action[0], expanded):
                    continue

                new_path = current.path + [action[0]]
                temp_frontier.append(Node(parent=current, state=action[0], path=new_path, depth=depth))

            frontier = temp_frontier + frontier
            temp_frontier = []

        if(isSolved):
            print("----------SOLUTION--------")
            print(solution_node.path)
            for node in solution_node.path:
                node.render()
            break
        depth = 0
        depth_limit += 1


def isInExpanded(current, expanded):
    inExpanded = False
    for expand in expanded:
        if current == expand:
            inExpanded = True

    return inExpanded


def main():
    puzzle = Puzzle15(puzzle=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], goal_state=[[1, 2, 0, 3], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]])

    iterative_deepening_algorithm(puzzle)


if __name__ == '__main__':
    main()
