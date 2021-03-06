class Puzzle15:
    def __init__(self, puzzle, goal_state):
        #state of the puzzle
        self.puzzle = puzzle

        self.number_of_rows = len(puzzle)
        self.number_of_columns = len(puzzle[0])

        #goal state
        # 0 is the blank space
        self.goal_state = goal_state

    def get_coordinate(self, tile):
        for i in range(0, self.number_of_rows):
            for j in range(0, self.number_of_columns):
                if self.puzzle[i][j] == tile:
                    return i, j
    
    def distance_to_goal_state(self, tile):
        x1, y1 = self.get_coordinate(tile)
        for x in range(0, self.number_of_rows):
            for y in range(0, self.number_of_columns):
                if self.goal_state[x][y] == tile:
                    return abs(x - x1) + abs(y - y1)


    def copy_puzzle(self):
        copy_puzzle = []
        for row in self.puzzle:
            copy_puzzle.append(list(row))
        return copy_puzzle

    # Swap the square with the blank space
    def swap(self, x1, y1, x2, y2):
        new_puzzle = self.copy_puzzle()
        temp = new_puzzle[x1][y1]
        new_puzzle[x1][y1] = new_puzzle[x2][y2]
        new_puzzle[x2][y2] = temp

        return new_puzzle

    def get_possible_actions(self):
        actions = []
        x, y = self.get_coordinate(0)

        # UP
        if x > 0:
            actions.append((Puzzle15(self.swap(x, y, x-1, y), self.goal_state), 1))
        # DOWN
        if x < (self.number_of_rows - 1):
            actions.append( (Puzzle15(self.swap(x, y, x+1, y), self.goal_state), 1)  )
        # LEFT
        if y > 0:
            actions.append((Puzzle15(self.swap(x, y, x, y-1), self.goal_state), 1))
        # RIGHT
        if y < (self.number_of_columns - 1):
            actions.append((Puzzle15(self.swap(x, y, x, y+1), self.goal_state), 1))
        # UP - LEFT
        if x > 0 and y > 0:
            actions.append((Puzzle15(self.swap(x, y, x-1, y-1), self.goal_state), 3))
        # DOWN - LEFT
        if x < (self.number_of_rows - 1) and y > 0:
            actions.append((Puzzle15(self.swap(x, y, x+1, y-1), self.goal_state), 3))
        # UP - RIGHT
        if x > 0 and y < (self.number_of_columns - 1):
            actions.append((Puzzle15(self.swap(x, y, x-1, y+1), self.goal_state), 3))
        # DOWN - RIGHT
        if x < (self.number_of_rows - 1) and y < (self.number_of_columns - 1):
            actions.append((Puzzle15(self.swap(x, y, x+1, y+1), self.goal_state), 3))
        
        return actions
        

        


    def render(self):
        print()
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                if self.puzzle[i][j] < 10:
                    print('  {}'.format(self.puzzle[i][j]), end='')
                else:
                    print(' {}'.format(self.puzzle[i][j]), end='')
            print()



# puzzle = Puzzle15(puzzle=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], goal_state=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])
# puzzle.render()

# actions = puzzle.get_possible_actions()
# for action in actions:
#     print(action)
#     action[0].render()