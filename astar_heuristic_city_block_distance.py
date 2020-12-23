from puzzle15 import *

def heuristic_city_block_distance(puzzle):
    total_distance = 0
    for x in range(0, puzzle.number_of_rows):
        for y in range(0, puzzle.number_of_columns):
            total_distance += puzzle.distance_to_goal_state(puzzle.puzzle[x][y])
    
    return total_distance


def calculate_g(path):
    g = 0
    for i in range(len(path)):
        if i + 1 == len(path) - 1:
            break
        #print(i)
        x = path[i+1].get_coordinate(0)[0] - path[i].get_coordinate(0)[0]
        y = path[i+1].get_coordinate(0)[1] - path[i].get_coordinate(0)[1]
        if (x, y) == (1, 0) or (x, y) == (0, 1) or (x, y) == (-1, 0) or (x, y) == (0, -1):
            g += 1
        else:
            g += 3
        

    return g



def astar(puzzle):
    expanded = []
    frontier = [[heuristic_city_block_distance(puzzle), puzzle]]

    path = None
    num_expanded_nodes = 0
    while frontier:
        i = 0
        for j in range(1, len(frontier)):
            if frontier[i][0] > frontier[j][0]:
                i = j
        
        path = frontier[i]
        # first i elements // after the i+1
        frontier = frontier[:i] + frontier[i+1:]
        end_state = path[-1]


        #end_state.render()
        # Break if we reached goal state
        if end_state.puzzle == end_state.goal_state:
            break
        
        # If end state is expanded continue and then break
        if end_state.puzzle in expanded:
            continue
        
        actions = end_state.get_possible_actions()
        for action in actions:
            if action[0].puzzle in expanded:
                continue

            #print(path[1:])
            g = calculate_g(path[1:] + [action[0]])
            #print('-', g)
            path2 = [ g + heuristic_city_block_distance(action[0]) ] + path[1:] + [action[0]]
            #print(path[0], heuristic_city_block_distance(action[0]), heuristic_city_block_distance(end_state))
            #print(path2)
            expanded.append(end_state.puzzle)
            frontier.append(path2)
            #print(frontier)
        num_expanded_nodes += 1

        print(num_expanded_nodes)
        
    solution = path[1:]

    print(solution)
    for p in solution:
        p.render()

            


def main():
    puzzle = Puzzle15()
    astar(puzzle)

if __name__ == '__main__':
    main()


