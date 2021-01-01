import math


class Node:
    def __init__(self, parent=None, state=None, path=None, g=0):
        self.parent = parent
        self.state = state
        self.path = path
        self.g = g

    def __eq__(self, obj):
        try:
            if (self.parent == obj.parent and self.state == obj.state):
                return True
            else:
                return False
        except:
            return False


def iterative_lengthening_search(puzzle, send_end):
    g = 0
    length_limit = 0
    solution_node = None
    is_solved = False

    while 1:
        explored = []
        frontier = [Node(None, puzzle, [puzzle], g)]
        max_number_of_nodes_stored = 0

        while frontier:
            # Calculate the maximum number of nodes stored in memory (frontier)
            if max_number_of_nodes_stored < len(frontier):
                max_number_of_nodes_stored = len(frontier)

            minn = math.inf
            index_of_min = 0
            for i in range(len(frontier)):
                node = frontier[i]
                if node.g < minn:
                    minn = node.g
                    index_of_min = i

            current = frontier.pop(index_of_min)

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
                if action[0].puzzle in explored:
                    continue
                if current.parent == None:
                    g = action[1]
                else:
                    g = current.g + action[1]
                if g <= length_limit:
                    new_path = current.path + [action[0]]
                    frontier.append(Node(parent=current, state=action[0], path=new_path, g=g))
                else:
                    continue

        if is_solved:
            print("----------SOLUTION--------")
            for node in solution_node.path:
                node.render()
            print("The cost of the solution found", solution_node.g)
            print("The total number of expanded nodes : ", len(explored))
            print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)
            send_end.send([solution_node, len(explored), max_number_of_nodes_stored])
            break

        length_limit += 1

