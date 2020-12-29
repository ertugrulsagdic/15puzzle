from puzzle15 import *
class Node:
    def __init__(self, parent=None, state=None, path=None, depth=0, g=0):
        self.parent = parent
        self.state = state
        self.path = path
        self.depth = depth
        self.g = g

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
    max_number_of_nodes_stored = 0

    while 1:
        expanded = []
        frontier = [Node(None, puzzle, [puzzle], depth, 0)]
        temp_frontier = []

        while frontier:
            #Calculate the maximum number of nodes stored in memory (frontier)
            if max_number_of_nodes_stored < len(frontier):
                max_number_of_nodes_stored = len(frontier)

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

                if current.parent == None:
                    g = action[1]
                else:
                    g = current.parent.g + action[1]

                new_path = current.path + [action[0]]
                temp_frontier.append(Node(parent=current, state=action[0], path=new_path, depth=depth, g=g))

            frontier = temp_frontier + frontier
            temp_frontier = []

        if(isSolved):
            print("----------SOLUTION--------")
            print(solution_node.path)
            for node in solution_node.path:
                node.render()
            print("The total number of expanded nodes : ", len(expanded))
            print("The maximum number of nodes stored in memory : ", max_number_of_nodes_stored)
            break
        depth = 0
        depth_limit += 1


def isInExpanded(current, expanded):
    inExpanded = False
    for expand in expanded:
        if current == expand:
            inExpanded = True

    return inExpanded