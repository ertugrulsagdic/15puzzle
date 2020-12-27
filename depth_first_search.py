from puzzle15 import *

class Node:
    def __init__(self, parent=None, state=None, path=None):
        self.parent = parent
        self.state = state
        self.path = path

    def __eq__(self, obj):
        try:
            if(self.parent == obj.parent and self.state == obj.state):
                return True
            else:
                return False
        except:
            return False

def dfs_algorithm(puzzle):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle])]
    solution_node = None

    while frontier:
        current = frontier.pop(0)

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
            inExpanded = False
            for expand in expanded:
                if action[0] == expand:
                    inExpanded = True

            if inExpanded:
                continue

            new_path = current.path + [action[0]]
            frontier.append(Node(parent=current, state=action[0], path=new_path))

    print(solution_node.path)
    for node in solution_node.path:
        node.render()


# def dfs(puzzle):
#     frontier = [[puzzle]]
#     expanded = []
#     num_expanded_nodes = 0
#     path = None

#     print("dfs")
#     print(frontier[0])

#     while frontier:
#         path = frontier[0]
#         frontier.pop(0)  # defrontier (FIFO)
#         end_state = path[-1]

#         print(end_state.puzzle, expanded)
#         if end_state.puzzle in expanded:
#             continue

#         for move in end_state.get_possible_actions():
#             if move[0].puzzle in expanded:
#                 continue
#             frontier.append(path + [move])  # add new path at the end of the frontier

#         expanded.append(end_state.puzzle)
#         num_expanded_nodes += 1

#         if end_state.puzzle == end_state.goal_state:
#             break

#     print(num_expanded_nodes)
#     print(path[1:])

def main():
    puzzle = Puzzle15(puzzle=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])
    dfs_algorithm(puzzle)

if __name__ == '__main__':
    main()
