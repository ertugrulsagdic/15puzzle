from astar_heuristic_bonus import *
from astar_heuristic_city_block_distance import *
from astar_heuristic_misplaced import *
from breadth_first_search import *
from depth_first_search import *
from iterative_deepening_search import *
from iterative_lengthening_search import *
from uniform_cost_search import *

from puzzle15 import *
from random_puzzle_generator import generate_random_instance_of_puzzle

import multiprocessing
import time


def mainpart2():
    puzzle_a = Puzzle15(puzzle=[[0, 1, 3, 4], [12, 13, 2, 5], [11, 14, 15, 6], [10, 9, 8, 7]],
                        goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])

    puzzle_b = Puzzle15(puzzle=[[1, 3, 5, 4], [2, 13, 14, 15], [11, 12, 9, 6], [0, 10, 8, 7]],
                        goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])

    puzzle_c = Puzzle15(puzzle=[[1, 13, 3, 4], [12, 11, 2, 5], [9, 8, 15, 7], [10, 6, 14, 0]],
                        goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])
    
    puzzles = [puzzle_a, puzzle_b, puzzle_c]
    algorithms = [uniform_cost_search, 
                    iterative_lengthening_search, 
                    astar_algorithm_misplaced, 
                    astar_algorithm_city_block_distance,
                    astar_algorithm_bonus_diagonal_distance,
                    bfs_algorithm,
                    dfs_algorithm,
                    iterative_deepening_algorithm]


    time_limit_cycle = 300
    jobs = []
    pipe_list = []
    puzzle_name_list = ['puzzle_a', 'puzzle_b', 'puzzle_c']

    puzzle_name_list_counter = 0
    for puzzle in puzzles:

        for algorithm in algorithms:
            print('\n\n##### Algorithm : {} ##### Puzzle : {} ######'.format(algorithm, puzzle_name_list[puzzle_name_list_counter]))
            counter = 0
            recv_end, send_end = multiprocessing.Pipe(False)
            p = multiprocessing.Process(target=algorithm, args=(puzzle, send_end))
            p.start()

            while counter < time_limit_cycle:
                time.sleep(2)
                if p.is_alive():
                    print(p, " is running... ", counter)
                else:
                    print(p, " is done... ")
                    break
                counter += 1

            if p.is_alive():
                print(" is running... let's kill it...")
                p.terminate()
            else:
                jobs.append(p)
                pipe_list.append(recv_end)

        for process in jobs:
            process.join()

        result_list = [x.recv() for x in pipe_list]
        puzzle_name_list_counter += 1



if __name__ == '__main__':
    mainpart2()