import multiprocessing
import time

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


def call_algorithms(depth_limited_graph):
    astar_algorithm_bonus_diagonal_distance(depth_limited_graph)
    astar_algorithm_city_block_distance(depth_limited_graph)
    astar_algorithm_misplaced(depth_limited_graph)
    bfs_algorithm(depth_limited_graph)
    dfs_algorithm(depth_limited_graph)
    iterative_deepening_algorithm(depth_limited_graph)
    iterative_lengthening_search(depth_limited_graph)
    uniform_cost_search(depth_limited_graph)


def main():

    goal_puzzle = Puzzle15(puzzle=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]],
                           goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])

    puzzle_bundles = []

    random_puzzle_solution_depth_2 = []
    random_puzzle_solution_depth_4 = []
    random_puzzle_solution_depth_6 = []
    random_puzzle_solution_depth_8 = []
    random_puzzle_solution_depth_10 = []
    random_puzzle_solution_depth_12 = []
    random_puzzle_solution_depth_16 = []
    random_puzzle_solution_depth_20 = []
    random_puzzle_solution_depth_24 = []
    random_puzzle_solution_depth_28 = []

    for i in range(0, 10):
        random_puzzle_solution_depth_2.append(generate_random_instance_of_puzzle(goal_puzzle, 2))
        random_puzzle_solution_depth_4.append(generate_random_instance_of_puzzle(goal_puzzle, 4))
        random_puzzle_solution_depth_6.append(generate_random_instance_of_puzzle(goal_puzzle, 6))
        random_puzzle_solution_depth_8.append(generate_random_instance_of_puzzle(goal_puzzle, 8))
        random_puzzle_solution_depth_10.append(generate_random_instance_of_puzzle(goal_puzzle, 10))
        random_puzzle_solution_depth_12.append(generate_random_instance_of_puzzle(goal_puzzle, 12))
        random_puzzle_solution_depth_16.append(generate_random_instance_of_puzzle(goal_puzzle, 16))
        random_puzzle_solution_depth_20.append(generate_random_instance_of_puzzle(goal_puzzle, 20))
        random_puzzle_solution_depth_24.append(generate_random_instance_of_puzzle(goal_puzzle, 24))
        random_puzzle_solution_depth_28.append(generate_random_instance_of_puzzle(goal_puzzle, 28))

    puzzle_bundles.append(random_puzzle_solution_depth_2)
    puzzle_bundles.append(random_puzzle_solution_depth_4)
    puzzle_bundles.append(random_puzzle_solution_depth_6)
    puzzle_bundles.append(random_puzzle_solution_depth_8)
    puzzle_bundles.append(random_puzzle_solution_depth_10)
    puzzle_bundles.append(random_puzzle_solution_depth_12)
    puzzle_bundles.append(random_puzzle_solution_depth_16)
    puzzle_bundles.append(random_puzzle_solution_depth_20)
    puzzle_bundles.append(random_puzzle_solution_depth_24)
    puzzle_bundles.append(random_puzzle_solution_depth_28)

    depths = (2,4,6,8,10,12,16,20,24,28)
    # it waits 10 seconds if the time limit cycle is 6 then it will wait 1 minutes
    time_limit_cycle = 60

    avg_expanded_nodes = []
    avg_max_number_of_nodes_stored = []
    depth_counter = 0

    for puzzle_bundle in puzzle_bundles:
        total_expanded_nodes = 0
        total_max_number_of_nodes_stored = 0
        jobs = []
        pipe_list = []
        for graph in puzzle_bundle:
            counter = 0
            recv_end, send_end = multiprocessing.Pipe(False)
            p = multiprocessing.Process(target=iterative_deepening_algorithm, args=(graph, send_end))
            p.start()

            while counter < time_limit_cycle:
                time.sleep(10)
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
        result_list_len = len(result_list)
        print(result_list_len)
        print(result_list)

        for result in result_list:
            total_expanded_nodes += result[1]
            total_max_number_of_nodes_stored += result[2]

        avg_expanded = total_expanded_nodes/result_list_len
        avg_stored = total_max_number_of_nodes_stored/result_list_len

        avg_expanded_nodes.append(avg_expanded)
        avg_max_number_of_nodes_stored.append(avg_stored)
        print("average number of expanded nodes", avg_expanded)
        print("average max number of nodes stored", avg_stored)

    print("---------------------------------------------------------")
    print("Current depth = ")
    print(depths[depth_counter])
    depth_counter += 1
    print("Average expanded nodes")
    for i in range(0, len(avg_expanded_nodes)):
        print(avg_expanded_nodes[i])

    print("---------------------------------------------------------")
    print("Average stored nodes")
    for i in range(0, len(avg_max_number_of_nodes_stored)):
        print(avg_max_number_of_nodes_stored[i])


if __name__ == '__main__':
    main()
