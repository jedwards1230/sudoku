from random import sample
from copy import deepcopy

class SudokuGenerator:
    def __init__(self, size = 3, difficulty = 4):
        # allows for board size between 2x2 and 4x4
        if size not in range(2, 5):
            raise ValueError('Invalid board size')
        # difficulty measures how many spots are made blank in a puzzle. difficulty / 8 = percent hidden
        #if difficulty not in range(1, 8):
            #raise ValueError('Invalid difficulty')
        
        self.base = size
        self.side = self.base * self.base
        
        # generate board solution and puzzle
        self.board_solution = self.get_solution()
        self.board_puzzle = self.get_puzzle(difficulty)
    
    def get_solution(self):
        rBase = range(self.base) 
        # shuffle by inner groups (typically 3x3 in a 9x9 board)
        # range(base) = 0, 1, 2 = 3 inner groups
        # shuffle within inner groups to keep the sudoku integrity within the 3x3
        # do seperately for rows and columns
        rows  = [group * self.base + group_row for group in self.shuffle(rBase) for group_row in self.shuffle(rBase)] 
        cols  = [group * self.base + group_col for group in self.shuffle(rBase) for group_col in self.shuffle(rBase)]
        nums  = self.shuffle(range(1, self.side + 1))
        
        # produce board using randomized baseline pattern
        board_solution = [[nums[self.pattern(row,col)] for col in cols] for row in rows]
        
        return board_solution
    
    def get_puzzle(self, difficulty):
        max_difficulty = 8
        squares = self.side * self.side
        empties = squares * difficulty // max_difficulty
        puzzle = deepcopy(self.board_solution)
        
        for p in sample(range(squares), empties):
            puzzle[p // self.side][p % self.side] = 0
            
        return puzzle

    # pattern for a baseline valid solution
	# (3 * (row % 3) + row // 3 + col % 3) % 3
    def pattern(self, row, col): return (self.base * (row % self.base) + row // self.base + col) % self.side

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(self, s): return sample(s, len(s)) 

    def print_grid(self, grid):
        for row in grid:
            for x in row:
                if x == 0:
                    print('_  ', end='')
                else:
                    print(str(x) + '  ', end='')
            print()
            
    # format sudoku puzzle for django template
    def prepare_puzzle(self):
        puzzle = []
        id = 0
        for row in self.board_puzzle:
            new_row = []
            for val in row:
                new_row.append({
                    id : val
                })
                id += 1
            puzzle.append(new_row)
        return puzzle
    
    def shortSudokuSolve(self, board):
        size    = len(board)
        block   = int(size**0.5)
        board   = [n for row in board for n in row ]      
        span    = { (n,p): { (g,n)  for g in (n>0)*[p//size, size+p%size, 2*size+p%size//block+p//size//block*block] }
                    for p in range(size*size) for n in range(size+1) }
        empties = [i for i,n in enumerate(board) if n==0 ]
        used    = set().union(*(span[n,p] for p,n in enumerate(board) if n))
        empty   = 0
        while empty>=0 and empty<len(empties):
            pos        = empties[empty]
            used      -= span[board[pos],pos]
            board[pos] = next((n for n in range(board[pos]+1,size+1) if not span[n,pos]&used),0)
            used      |= span[board[pos],pos]
            empty     += 1 if board[pos] else -1
            if empty == len(empties):
                solution = [board[r:r+size] for r in range(0,size*size,size)]
                yield solution
                empty -= 1