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


def foo(n):
    for i in range(10000 * n):
        print("Tick")
        time.sleep(1)

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

    total_expanded_nodes = 0
    total_max_number_of_nodes_stored = 0
    i = 0
    for graph in random_puzzle_solution_depth_2:
        _, expanded_nodes, max_number_of_nodes_stored = uniform_cost_search(graph)
        print('done', i)
        i += 1

        total_expanded_nodes += expanded_nodes
        total_max_number_of_nodes_stored += max_number_of_nodes_stored

    print("average number of expanded nodes", total_expanded_nodes/10)
    print("average max number of nodes stored", total_max_number_of_nodes_stored/10)



if __name__ == '__main__':
    main()
