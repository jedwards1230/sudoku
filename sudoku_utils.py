import itertools
from math import sqrt

from django.forms import formset_factory

import app.forms as sf

from sudoku import SudokuGenerator


def print_grid(grid, label=None):
    if label:
        print('\n** ' + label + ' **\n')
    for row in grid:
        for x in row:
            if x == None:
                raise ValueError('Invalid cell input')
            if x == 0 or x == None:
                print('_  ', end='')
            else:
                print(str(x) + '  ', end='')
        print()
    print()

# convert sudoku board from POST request to list of lists
def to_python(request, size):
    board = []
    row = []
    counter = 0
    
    l = size ** 2
    
    # extract puzzle from request
    for i, k in enumerate(request):
        if '-col_' in k:
            counter += 1
            value = request.getlist(k)
            if value[0]:
                row.append(int(value[0]))
            else:
                row.append(0)
            
            # new row based on size
            if counter % l == 0 and counter > 0:
                board.append(row)
                row = []
                
    # check if board is malformed
    for row in board:
        if len(row) != l:
            return None
    
    return board

# convert sudoku board to be processed by Django formset_factory
def to_web(board):
    converted_board = []
    for row in board:
        id = 0
        puzzle = {}
        for val in row:
            n = 'col_' + str(id)
            puzzle[n] = val
            id += 1
        converted_board.append(puzzle)
    return converted_board

# check if puzzle is solved
def check_solution(board):
    def valid_line(line):
        return (len(line) == size and sum(line) == sum(set(line)))
    
    size = len(board)
    side = int(sqrt(size))
    
    # check rows
    for row in board:
        for x in row:
            # check every value is int
            if not isinstance(x, int): return False
            # check value within proper range
            if not 0 < x <= size: return False
        # check values are unique
        if not valid_line(row): return False
    
    # check cols
    board = list(zip(*board))
    for col in board:
        # check values are unique
        if not valid_line(col): return False
    
    # check subgrids
    squares = []
    for i in range(0, size, side):
        for j in range(0, size, side):
            square = list(itertools.chain(row[j:j+3] for row in board[i:i+3]))
            squares.append(square)
    bad_squares = [square for square in squares if not valid_line(square)]
    if not bad_squares: return False
            
    return True

def new_sudoku_formset(size, difficulty, puzzle=None):
    if not puzzle:
        gen = SudokuGenerator(size=size, difficulty=difficulty)
        puzzle, _ = gen.get_sudoku()
    puzzle = to_web(puzzle)
    
    if size == 2:
        PuzzleFormSet = formset_factory(sf.PuzzleForm2)
    elif size == 3:
        PuzzleFormSet = formset_factory(sf.PuzzleForm3)
    elif size == 4:
        PuzzleFormSet = formset_factory(sf.PuzzleForm4)
        
    formset = PuzzleFormSet(initial=puzzle, auto_id=False)
    
    return formset