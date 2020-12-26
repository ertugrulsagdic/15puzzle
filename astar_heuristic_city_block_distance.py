from puzzle15 import *
import math

class Node:
    def __init__(self, parent=None, state=None, path=None,  g=0, h=0):
        self.parent = parent
        self.state = state
        self.path = path
        self.g = g
        self.h = h
        self.f = g + h

    def __eq__(self, obj):
        # if(self.parent == "None" and obj.parent == "None"):
        #     return True
        # elif(self.parent == "None" and obj.parent != "None"):
        #     return False
        # elif(self.parent != "None" and obj.parent == "None"):
        #     return False
        try:
            if(self.parent == obj.parent and self.state == obj.state):
                return True
            else:
                return False
        except:
            return False
    

def heuristic_city_block_distance(puzzle):
    total_distance = 0
    for x in range(0, puzzle.number_of_rows):
        for y in range(0, puzzle.number_of_columns):
            total_distance += puzzle.distance_to_goal_state(puzzle.puzzle[x][y])
    
    return total_distance


def calculate_g(path):
    g = 0
    for i in range(len(path)):
        if i + 1 == len(path):
            break
        #print(i)
        x = path[i+1].get_coordinate(0)[0] - path[i].get_coordinate(0)[0]
        y = path[i+1].get_coordinate(0)[1] - path[i].get_coordinate(0)[1]
        if (x, y) == (1, 0) or (x, y) == (0, 1) or (x, y) == (-1, 0) or (x, y) == (0, -1):
            g += 1
        else:
            g += 3

    # print("GGGGG", path[-1].render(), g)
    # y = input()
        

    return g

def astar_algorithm(puzzle):
    expanded = []
    frontier = [Node(None, puzzle, [puzzle], 0, heuristic_city_block_distance(puzzle))]
    solution_node = None
    while frontier:
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
        
        # ??????????
        inExpanded = False
        for expand in expanded:
            # if current.parent == None or expand.parent == None:
            #     continue
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





# def astar(puzzle):
#     expanded = []
#     frontier = [[heuristic_city_block_distance(puzzle), puzzle]]

#     path = None
#     num_expanded_nodes = 0
#     while frontier:
#         i = 0
#         for j in range(1, len(frontier)):
#             if frontier[i][0] > frontier[j][0]:
#                 i = j
        
#         path = frontier[i]
#         # first i elements // after the i+1
#         frontier = frontier[:i] + frontier[i+1:]
#         end_state = path[-1]


#         #end_state.render()
#         # Break if we reached goal state
#         if end_state.puzzle == end_state.goal_state:
#             break
        
#         # If end state is expanded continue and then break
#         if end_state.puzzle in expanded:
#             continue
        
#         actions = end_state.get_possible_actions()
#         for action in actions:
#             if action[0].puzzle in expanded:
#                 continue

#             #print(path[1:])
#             g = calculate_g(path[1:] + [action[0]])

#             #print('-', g)
#             path2 = [heuristic_city_block_distance(action[0]) ] + path[1:] + [action[0]]
#             #print(path[0], heuristic_city_block_distance(action[0]), heuristic_city_block_distance(end_state))
#             #print(path2)
#             expanded.append(end_state.puzzle)
#             frontier.append(path2)
#             #print(frontier)
#         num_expanded_nodes += 1

#         print(num_expanded_nodes)
        
#     solution = path[1:]

#     print(solution)
#     for p in solution:
#         p.render()


def main():
    puzzle = Puzzle15(puzzle=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])
    astar_algorithm(puzzle)

if __name__ == '__main__':
    main()


