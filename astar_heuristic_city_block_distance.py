from puzzle15 import *

def heuristic_city_block_distance(puzzle):
    total_distance = 0
    for x in range(0, puzzle.number_of_rows):
        for y in range(0, puzzle.number_of_columns):
            total_distance = puzzle.distance_to_goal_state(puzzle.puzzle[x][y])
    
    return total_distance

def astar(puzzle):
    expanded = []
    queue = [[heuristic_city_block_distance(puzzle), puzzle]]

    path = None
    while queue:
        i = 0
        for j in range(i, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j
        
        path = queue[i]
        queue = queue[:i] + queue[i+1:]
        end_state = path[-1]

        # Break if we reached goal state
        if end_state.puzzle == end_state.goal_state:
            break
        
        # If end state is expanded continue and then break
        if end_state.puzzle in expanded:
            continue
        
        actions = end_state.get_possible_actions()
        for action in actions:
            if action.puzzle in expanded:
                continue

            path2 = [path[0] + (heuristic_city_block_distance(action.puzzle) - heuristic_city_block_distance(end_state.puzzle))] + path[1:] + [action]
            
            expanded.append(end_state.puzzle)
            queue.append(path2)
        
        solution = path[1:]

        print(solution)
            


def main():
    puzzle = Puzzle15()
    astar(puzzle)

if __name__ == '__main__':
    main()


