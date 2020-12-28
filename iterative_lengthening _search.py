from puzzle15 import *
import math


class Node:
    def __init__(self, parent=None, state=None, path=None, length=0):
        self.parent = parent
        self.state = state
        self.path = path
        self.length = length

    def __eq__(self, obj):
        try:
            if (self.parent == obj.parent and self.state == obj.state):
                return True
            else:
                return False
        except:
            return False


def iterative_lengthening_search(puzzle):
    length = 0
    length_limit = 0
    solution_node = None
    is_solved = False
    number_of_explored_nodes_fei = []
    number_of_nodes_fei = []

    while 1:
        explored = []
        frontier = [Node(None, puzzle, [puzzle], length)]
        max_number_of_nodes_stored = 0

        while frontier:
            # Calculate the maximum number of nodes stored in memory (frontier)
            if max_number_of_nodes_stored < len(frontier):
                max_number_of_nodes_stored = len(frontier)

            minn = math.inf
            index_of_min = 0
            for i in range(len(frontier)):
                node = frontier[i]
                if node.length < minn:
                    minn = node.length
                    index_of_min = i

            current = frontier.pop(index_of_min)

            if (current.length >= length_limit):
                continue

            if current.state.puzzle == current.state.goal_state:
                is_solved = True;
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
                if current.parent == None:
                    length = action[1]
                else:
                    length = current.parent.length + action[1]
                new_path = current.path + [action[0]]
                frontier.append(Node(parent=current, state=action[0], path=new_path, length=length))

        if is_solved:
            print("----------SOLUTION--------")
            print(solution_node.path)
            for node in solution_node.path:
                node.render()

            print("The total number of expanded nodes : ", len(explored))
            print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)
            break

        number_of_explored_nodes_fei.append(len(explored))
        number_of_nodes_fei.append(max_number_of_nodes_stored)

        length = 0;
        length_limit += 1


def main():
    puzzle = Puzzle15(puzzle=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], goal_state=[[1, 2, 0, 3], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]])
    iterative_lengthening_search(puzzle)


if __name__ == '__main__':
    main()
